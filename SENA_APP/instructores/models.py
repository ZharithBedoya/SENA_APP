from django.db import models

class Instructor(models.Model):
   TIPO_DOC_CHOISES=[
    ('CC', 'Cédula de Ciudadanía'),
    ('CE', 'Cédula de Extranjería'),
    ('PA', 'Pasaporte'),
    ('TI', 'Tarjeta de Identidad'),
   ]
   NIVEL_EDUCACION_CHOISES=[
    ('TEC', 'Técnica'),
    ('TEG', 'Tecnológica'),
    ('PRE', 'Pregrado'),
    ('ESP', 'Especialización'),
    ('MAE', 'Maestría'),
    ('DOC', 'Doctorado'),
   ]
   documento_identidad = models.CharField(max_length=20, unique=True)
   tipo_documento = models.CharField(max_length=3, choices=TIPO_DOC_CHOISES, default='CC')
   nombre = models.CharField(max_length=100)
   apellido = models.CharField(max_length=100)
   telefono = models.CharField(max_length=15)
   correo = models.EmailField(unique=True)
   fecha_nacimiento = models.DateField()
   ciudad = models.CharField(max_length=100)
   direccion = models.CharField(max_length=200)
   nivel_educacion = models.CharField(max_length=3, choices=NIVEL_EDUCACION_CHOISES, default='PRE')
   especialidad = models.CharField(max_length=100)
   anos_experiencia = models.PositiveIntegerField()
   activo = models.BooleanField(default=True)
   fecha_vinculacion = models.DateField()
   fecha_registro = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
          return f"{self.nombre}-{self.apellido}-{self.especialidad}"
   def nombre_completo(self):
          return f"{self.nombre}-{self.apellido}"
   def documento_com(self):
          return f"{self.documento}-{self.tipo_documento}"
   def direccion_com(self):
          return f"{self.direccion}-{self.ciudad}"
   
# Create your models here.
