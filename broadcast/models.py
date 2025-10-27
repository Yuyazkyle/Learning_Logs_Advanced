from django.db import models
from django.contrib.auth.models import User

class BTopic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class BEntry(models.Model):
    owner = models.ForeignKey(BTopic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Broadcast Entries'
    
    def __str__(self):
        if len(self.text) > 55:
            print(self.text[55]) + '....'
        else:
            print(self.text)