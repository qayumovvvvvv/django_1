from django.db import models


class Featured_works(models.Model):
    img = models.ImageField()

    def __str__(self):
        return self.img.name


class Lates_blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.title
    

class Menu_price(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    

class Contact_info(models.Model):
    telephone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
class SignUp(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.fullname