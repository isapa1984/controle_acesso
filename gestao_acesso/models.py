from django.db import models

class Sistema(models.Model):
    nome = models.CharField(max_length=250)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class Perfil(models.Model):
    nome = models.CharField(max_length=250)
    sistema = models.ForeignKey("Sistema", on_delete=models.CASCADE)


class Acao(models.Model):
    perfil = models.ForeignKey("Perfil", on_delete=models.CASCADE)
    nome = models.CharField(max_length=250)
    identificador = models.CharField(max_length=50)


class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()


class Usuario(models.Model):
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=250)
    perfis = models.ManyToManyField("Perfil")