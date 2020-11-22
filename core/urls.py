from django.urls import path
from .views import homepage, register, profile_view, other_profiles, add_profile_image, activation

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>/", activation, name="activate"),
    path("profile/", profile_view, name="profile"),
    path("other-profiles/<int:user_pk>/", other_profiles, name="other_profiles"),
    path("add-profile-image/", add_profile_image, name="add_profile_image"),
]
