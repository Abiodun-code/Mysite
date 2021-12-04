from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Entry(models.Model):
    entry_title =  models.CharField(max_length=200)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.entry_title