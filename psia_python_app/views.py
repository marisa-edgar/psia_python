from contextvars import Context
from django.shortcuts import render, redirect
from .forms import UserPostForm
from .models import UserPost, Profile
from django.http import HttpResponse

def dashboard(request):
  if request.method == "POST":
    form = UserPostForm(request.POST or None)
    if form.is_valid():
      userpost = form.save(commit=False)
      userpost.user = request.user
      userpost.save()
      return redirect("psia_python_app:dashboard")

  followed_userposts = UserPost.objects.filter(
    user__profile__in=request.user.profile.follows.all()
  ).order_by("-created_at")
  form = UserPostForm()
  return render(
    request, 
    "psia_python_app/dashboard.html", 
    {'form': form, 'userposts': followed_userposts}
  )

def profile_list(request):
  profiles = Profile.objects.exclude(user=request.user)
  return render(
    request, 
    'psia_python_app/profile_list.html', 
    {'profiles': profiles}
  )

def profile(request, pk):
  if not hasattr(request.user, 'profile'):
      missing_profile = Profile(user=request.user)
      missing_profile.save()

  profile = Profile.objects.get(pk=pk)
  if request.method == "POST":
    current_user_profile = request.user.profile
    data = request.POST
    action = data.get("follow")
    if action == "follow":
        current_user_profile.follows.add(profile)
    elif action == "unfollow":
        current_user_profile.follows.remove(profile)
    current_user_profile.save()
  return render(request, "psia_python_app/profile.html", {"profile": profile})

def index(request):
  return render(request, 'psia_python_app/index.html', Context)