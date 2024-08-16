from django.db import models

# Create your models here.
class movie(models.Model):


    name=models.CharField(max_length=240)
    des=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='downloads')


    def __str__(self):
        return self.name

