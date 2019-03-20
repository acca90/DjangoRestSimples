from django.db import models


class Contato(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	telefone = models.CharField(max_length=15)
