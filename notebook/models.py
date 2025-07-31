from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField(null=True, blank=True)
    scheduled_time = models.TimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='note_photos/', null=True, blank=True)
    attachment = models.FileField(upload_to='note_attachments/', null=True, blank=True)

    def __str__(self):
        return self.title
