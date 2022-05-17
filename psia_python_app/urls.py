from django.urls import path
from .views import profile_list, profile, dashboard

app_name = "psia_python_app"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('profile_list', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
]