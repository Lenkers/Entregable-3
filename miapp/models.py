from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class CuentaBancaria(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuenta = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Cuenta de {self.cliente.nombre}"

class Transaccion(models.Model):
    cuenta = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name="transacciones")
    canal = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacción de {self.cuenta.cliente.nombre}"
