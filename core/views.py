from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib import messages
from content.models import Nota
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import core.models
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_image = form.cleaned_data["profile_image"]
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Attiva il tuo account"
            message = render_to_string('acc_act_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, "registration/activation-toconfirm.html")
        else:
            print(form.errors)
            messages.error(request, list(form.errors.values())[0])
            return render(request, "registration/register.html", {"form": CustomUserCreationForm})

    else:
        return render(request, "registration/register.html", {"form": CustomUserCreationForm})


def activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, "registration/activation-confirmed.html")
    else:
        return render(request, "registration/activation-refused.html")


@login_required
def profile_view(request):
    user = request.user
    note = Nota.objects.filter(studente=user).order_by('-data_pubblicazione')
    ratio_pos, ratio_neg = user.get_val_ratio()
    paginator = Paginator(note, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user":user, "page_obj":page_obj, "ratio_pos":ratio_pos, "ratio_neg":ratio_neg}

    return render(request, "registration/profile_view.html", context)


def add_profile_image(request):
    if request.method == "POST":
        profile_image = request.FILES['profile_image']
        user = request.user
        user.profile_image = profile_image
        user.save()
        return redirect(reverse('profile'))


def other_profiles(request, user_pk):
    user = get_object_or_404(core.models.CustomUser, pk=user_pk)
    note = Nota.objects.filter(studente=user).order_by('-data_pubblicazione')
    ratio_pos, ratio_neg = user.get_val_ratio()
    paginator = Paginator(note, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"user":user, "page_obj":page_obj, "ratio_pos":ratio_pos, "ratio_neg":ratio_neg}

    return render(request, "registration/other_profiles.html", context)
