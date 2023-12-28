from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64,default=f'file from {author}')
    full_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    download_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.full_file.name} by {self.author.username}'

@receiver(post_save, sender=File)
def generate_download_url(sender, instance, **kwargs):
    if not instance.download_url:
        instance.download_url = reverse('download_file', args=[str(instance.id)])
        instance.save()
