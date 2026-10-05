from django.shortcuts import render, redirect

from .forms import BlogForm
from .models import Blog


def home(request):

    if request.method == "POST":

        form = BlogForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            return redirect("home")

    else:
        form = BlogForm()

    blogs = Blog.objects.all().order_by("-created_at")

    context = {
        "form": form,
        "blogs": blogs,
    }

    return render(
        request,
        "home.html",
        context
    )
