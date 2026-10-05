from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog

        fields = [  
            "title",
            "author_name",
            "category",
            "content",
            "image",
        ]
# Shortcut:
# class BlogForm(forms.ModelForm):

#     class Meta:
#         model = Blog
#         fields = "__all__"
