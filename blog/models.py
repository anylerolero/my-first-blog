from django.db import models
from django.utils import timezone

class Post(models.Model): #Class -> para definir un objeto
# Post es el nombre del modelo
# models.Model indica que Post es un modelo de Django, entonces este lo guarda
# en la base de datos
    author = models.ForeignKey('auth.User') # es una relación con otro modelo
    title = models.CharField(max_length=200) # Texto con número limitado de caracteres
    text = models.TextField() #Sin limitación de caracteres
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #método publish de la clase Post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
