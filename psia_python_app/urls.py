from django.urls import path
from .views import profile_list, profile, dashboard, imagepost

app_name = "psia_python_app"

urlpatterns = [
    # path('index/', index, name='home'),
    path("", dashboard, name="dashboard"),
    path('profile_list', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('imageposts/<int:imagepost_id>', imagepost, name='imagepost')
]