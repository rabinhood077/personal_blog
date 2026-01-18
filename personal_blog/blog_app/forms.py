from django import forms

from blog_app.models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "featured_image", "content", "category", "tag"]
        widgets = {
            "content": SummernoteWidget(),
            "category": forms.Select(attrs={"class": "form-control"}),
            "tag": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
