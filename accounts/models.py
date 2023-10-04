from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    data_nascimento = models.fields.DateField("Data de nascimento", blank=True, null=True)
    cpf= models.CharField("CPF", max_length=11, blank=True, null=True)
    imagem = models.FileField(upload_to='images', default=None, null=True)