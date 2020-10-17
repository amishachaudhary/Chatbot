from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title
