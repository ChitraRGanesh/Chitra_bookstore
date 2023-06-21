from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=250,default='Untitled')
    dept = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return self.name