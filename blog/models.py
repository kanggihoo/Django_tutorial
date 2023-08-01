from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # author =

    def __str__(self):
        return f"[{self.pk}]{self.title}"

    def get_absolute_url(self):
        url = f"/blog/{self.pk}/"
        return url


# Create your models here.
