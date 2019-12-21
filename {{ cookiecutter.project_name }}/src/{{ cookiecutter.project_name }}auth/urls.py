from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "{{ cookiecutter.project_name }}auth"

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
