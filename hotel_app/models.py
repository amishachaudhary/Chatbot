from django.db import models

# Create your models here.


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='img')
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     image_url = models.CharField(max_length=1000, null=True, blank=True)
#     price = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return self.title


class Order(models.Model):
    Hotel = models.ForeignKey(Hotel, max_length=200,
                              null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Hotel.title
