from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=228)
    email = models.EmailField()
    subject = models.CharField(max_length=228)
    text = models.TextField()

    def __str__(self):
        return self.name

