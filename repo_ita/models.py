from django.contrib.auth.models import User
from django.db import models

TYPES_OF_DOCS = (
    ('articulo', 'Articulo'),
    ('evidencia', 'Evidencia'),
    ('tesis', 'Tesis'),
)


def user_directory_path(instance, filename):
    return 'docs/user_{0}/{1}/{2}'.format(
        instance.user.username, instance.type_of_articule, filename)


class Articulo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    type_of_articule = models.CharField(
        max_length=20, choices=TYPES_OF_DOCS,
        verbose_name='Tipo de Documento')
    tags = models.CharField(max_length=50)
    file_path = models.FileField(
        upload_to=user_directory_path, verbose_name='Archivo a Subir')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Articulo: {self.name}"
