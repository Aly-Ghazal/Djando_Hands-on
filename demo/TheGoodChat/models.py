from django.db import models

# Create your models here.
class car(models.Model):
    name=       models.CharField(max_length=60)
    price=      models.DecimalField(max_digits=7,decimal_places=2)
    color=      models.CharField(max_length=25)
    image=      models.ImageField(upload_to='images/%y/%m/%d')
    descripion= models.TextField(null=True, blank=True)
    model=      models.CharField(max_length=100,default="2000",choices=[("2022","2022"),("2021","2021"),("1975","1975")])
    def __str__(self):
        return self.name
