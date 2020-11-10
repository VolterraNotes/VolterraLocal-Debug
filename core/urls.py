from django.urls import path
from .views import homepage, register, profile_view, other_profiles, add_profile_image

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", register, name="register"),
    path("profile/", profile_view, name="profile"),
    path("other-profiles/<int:user_pk>/", other_profiles, name="other_profiles"),
    path("add-profile-image/", add_profile_image, name="add_profile_image"),       
]
