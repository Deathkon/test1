from django.db import models


# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.full_name} --- {self.email}'

    class Meta:
        verbose_name_plural = 'Contact'
