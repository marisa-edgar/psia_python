from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import UserPost, Profile, ImagePost

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserPost)
admin.site.register(ImagePost, ImageAdmin)