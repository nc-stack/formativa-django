from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)
    total = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"
