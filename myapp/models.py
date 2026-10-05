from django.db import models

class Blog(models.Model):

    CATEGORY_CHOICES = [
        ("Educational", "Educational"),
        ("Technology", "Technology"),
        ("Sports", "Sports"),
    ]

    title = models.CharField(
        max_length=200
    )

    author_name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
