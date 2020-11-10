from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.list import ListView
from .models import Professore, Materia, Classe, Nota
from .forms import CreaNota, CreaNotaPDF, CreaNotaAudio, FormSegnalazione
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
class ProfessoriLista(ListView):

    model = Professore
    paginate_by = 25
    template_name = "professori_lista.html"

def subjects_list(request, year):
    classe = get_object_or_404(Classe, grado=int(year[0]))
    materie = Materia.objects.filter(classi__id__exact=classe.id).order_by('nome')

    context = {'materie':materie, 'year': classe}

    return render(request, "materie_list.html", context)

def notes_by_subject(request, subject):
    notes = Nota.objects.filter(materia__nome=subject).order_by('-data_pubblicazione')
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj, "subject":subject}

    return render(request, "notes_by_subject.html", context)

def notes_by_year(request, year):
    notes = Nota.objects.filter(classe__grado=year.split('a')[0]).order_by('-data_pubblicazione')
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj, "year":year}

    return render(request, "notes_by_year.html", context)

def notes_by_year_subject(request, year, subject):
    notes = Nota.objects.filter(classe__grado=year.split('a')[0], materia__nome=subject).order_by('-data_pubblicazione')
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj, "year":year, "subject":subject}

    return render(request, "notes_by_year_subject.html", context)

def notes_by_prof_subject(request, prof, subject):
    notes = Nota.objects.filter(professore__cognome=prof, materia__nome=subject).order_by('-data_pubblicazione')
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj, "prof":prof, "subject":subject}

    return render(request, "notes_by_prof_subject.html", context)

@login_required
def main_upload(request):
    return render(request, 'main_upload.html')

@login_required
def image_upload(request):
    if request.method == "POST":
        form = CreaNota(request.POST, request.FILES)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.studente = request.user
            new_note.save()
            return redirect(reverse("profile"))
        else:
            messages.error(request, list(form.errors.values())[0])
            return render(request, "image_upload.html", {"form": CreaNota()})

    form = CreaNota()
    return render(request, "image_upload.html", {"form": form})

@login_required
def pdf_upload(request):
    if request.method == "POST":
        form = CreaNotaPDF(request.POST, request.FILES)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.studente = request.user
            new_note.save()
            return redirect(reverse("profile"))
        else:
            messages.error(request, list(form.errors.values())[0])
            return render(request, "pdf_upload.html", {"form": CreaNotaPDF()})

    form = CreaNotaPDF()
    return render(request, "pdf_upload.html", {"form": form})

@login_required
def audio_upload(request):
    if request.method == "POST":
        form = CreaNotaAudio(request.POST, request.FILES)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.studente = request.user
            new_note.save()
            return redirect(reverse("profile"))
        else:
            messages.error(request, list(form.errors.values())[0])
            return render(request, "audio_upload.html", {"form": form})

    form = CreaNotaAudio()
    return render(request, "audio_upload.html", {"form": form})

@login_required
def form_segnalazione(request, nota_pk):
    nota = Nota.objects.get(pk=nota_pk)
    if not request.user in nota.segnalanti.all():
        if request.method == "POST":
            form = FormSegnalazione(request.POST)
            if form.is_valid():
                nuova_segnalazione = form.save(commit=False)
                nuova_segnalazione.nota = nota
                nuova_segnalazione.user = request.user
                nuova_segnalazione.save()
                messages.success(request, "La tua segnalazione è avvenuta con successo!")
                return redirect(reverse("homepage"))
            else:
                messages.error(request, list(form.errors.values())[0])
                return render(request, "form_segnalazione.html", {"form":form})

        form = FormSegnalazione()
        return render(request, "form_segnalazione.html", {"form":form})
    else:
        messages.error(request, "Hai già segnalato il post!")
        return redirect(reverse("homepage"))

@login_required
def upvote(request,nota_pk):
    nota = Nota.objects.get(pk=nota_pk)
    if not request.user in nota.votanti.all():
        nota.utile += 1
        nota.votanti.add(request.user)
        user = nota.studente
        user.val_pos += 1

        nota.save()
        user.save()

    url = request.GET.get("next")
    try:
        return HttpResponseRedirect(url)
    except:
        raise Http404

@login_required
def downvote(request,nota_pk):
    nota = Nota.objects.get(pk=nota_pk)
    if not request.user in nota.votanti.all():
        nota.non_utile += 1
        nota.votanti.add(request.user)
        user = nota.studente
        user.val_neg += 1

        nota.save()
        user.save()

    url = request.GET.get("next")
    try:
        return HttpResponseRedirect(url)
    except:
        raise Http404

def research(request):
    if request.method == "GET":
        filter = request.GET.get("research")
        notes = Nota.objects.filter(Q(titolo__icontains=filter) | Q(professore__cognome__icontains=filter) | Q(materia__nome__icontains=filter)).order_by('-data_pubblicazione')[:10]
        subjects = Materia.objects.filter(nome__icontains=filter)[:10]
        profs = Professore.objects.filter(Q(cognome__icontains=filter) | Q(nome__icontains=filter))[:10]

        context = {"filter":filter, "page_obj": notes, "subjects":subjects, "profs": profs}
        return render(request, "research_list.html", context)
    else:
        raise Http404
