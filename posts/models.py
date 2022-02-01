from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(blank=False, null=False, max_length=128)
    description = models.TextField(blank=False, null=False)
    post = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='post_covers')
    created_at = models.DateField(editable=False, default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
