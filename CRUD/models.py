from django.db import models

# Create your models here.

class produto(models.Model):
    nome = models.CharField(max_length = 100)
    descrição = models.TextField()






