from django.urls import path

from user.views import CreateUserView, ManageUserView, CreateTokenView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("my-profile/", ManageUserView.as_view(), name="my-profile"),
]

app_name = "user"
