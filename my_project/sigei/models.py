from django.db import models

class Sigei(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  #image = models.ImageField()