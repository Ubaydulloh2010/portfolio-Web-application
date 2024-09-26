from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=228)
    position = models.CharField(max_length=228)
    image = models.ImageField(upload_to="teacher_image/")
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name