from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    title = models.CharField(max_length=64,default=f'unnamed file')
    full_file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_file.name} in {self.uploaded_at}'

    def delete(self, *args, **kwargs):
        self.full_file.delete()
        super().delete(*args, **kwargs)
