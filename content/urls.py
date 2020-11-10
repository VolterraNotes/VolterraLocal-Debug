from django.urls import path
from .views import ProfessoriLista, subjects_list, main_upload, image_upload, pdf_upload, notes_by_year_subject, notes_by_prof_subject, upvote, downvote, notes_by_subject, research, notes_by_year,\
form_segnalazione, audio_upload

urlpatterns = [
    path("profs/", ProfessoriLista.as_view(), name="professori"),
    path("upload/", main_upload, name="main_upload"),
    path("image-upload/", image_upload, name="image_upload"),
    path("pdf-upload/", pdf_upload, name="pdf_upload"),
    path("audio-upload/", audio_upload, name="audio_upload"),
    path("research/", research, name="research"),
    path("<str:year>/subjects/", subjects_list, name="materie"),
    path("<str:year>/<str:subject>/notes-year-subject/", notes_by_year_subject, name="notes_by_year_subject"),
    path("<str:prof>/<str:subject>/notes-prof-subject/", notes_by_prof_subject, name="notes_by_prof_subject"),
    path("<str:subject>/notes-subject/", notes_by_subject, name="notes_by_subject"),
    path("<str:year>/notes-year/", notes_by_year, name="notes_by_year"),
    path("<int:nota_pk>/upvote/", upvote, name="upvote"),
    path("<int:nota_pk>/downvote/", downvote, name="downvote"),
    path("<int:nota_pk>/form_segnalazione/", form_segnalazione, name="form_segnalazione")
]
