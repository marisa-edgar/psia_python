from django import forms
from django.forms import ModelForm
from .models import UserPost

class UserPostForm(forms.ModelForm):
      body = forms.CharField(
      required=True,
      widget=forms.widgets.Textarea(
          attrs={
              "placeholder": "Post something...",
              "class": "textarea is-success is-medium",
          }
      ),
      label="",
  )

      class Meta:
        model = UserPost
        # fields = ('body', 'image')
        exclude = ("user", )