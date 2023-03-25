from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Proje(models.Model):
    name = models.CharField(max_length=200, verbose_name="Proje Adi", help_text="Proje adini yaziniz")
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="Projects/%Y/%m/%d/")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
 
    def __str__(self):
        return self.name