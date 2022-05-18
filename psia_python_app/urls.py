from django.urls import path, include
from .views import profile_list, profile, dashboard, index

app_name = "psia_python_app"

urlpatterns = [
    path('index/', index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", dashboard, name="dashboard"),
    path('profile_list', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
]