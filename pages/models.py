from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100)
    content = models.TextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
