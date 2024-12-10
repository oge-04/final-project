from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/productImages')
    def __str__(self):
        return self.name
