from django.contrib import admin
from django.db import models
from datetime import datetime 


class Livro(models.Model):
    Nome_Do_Livro = models.CharField(max_length=50, null=True, blank=True)
    Autor = models.CharField(max_length=50, null=True, blank=True)
    Editora = models.CharField(max_length=50, null=True, blank=True)
    Paginas = models.IntegerField(null=True, blank=True)  
    Ano_Publicação = models.CharField(max_length=4, null=True, blank=True)  
    Gênero = models.CharField(max_length=50, null=True, blank=True)
    Código = models.CharField(max_length=20, null=True, blank=True)
    Observações = models.TextField(null=True, blank=True)  
    Data_de_Entrada_do_Livro = models.DateTimeField(default=datetime.now, null=True, blank=True)

class Funcionario(models.Model):
    Nome_Do_Funcionario = models.CharField(max_length=50, null=True, blank=True)
    CPF_Funcionario = models.CharField(max_length=14, null=True, blank=True)
    Data_de_Nascimento = models.DateField(auto_now=False, null=True, blank=True)
    Data_de_Contratação = models.DateField(auto_now=False, null=True, blank=True)
    Endereço = models.CharField(max_length=50, null=True, blank=True)
    Telefone = models.CharField(max_length=13, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)


class Cliente(models.Model):
    Nome_Do_Cliente = models.CharField(max_length=50, null=True, blank=True)
    CPF_Cliente = models.CharField(max_length=14, null=True, blank=True)
    Data_de_Nascimento = models.DateField(auto_now=False, null=True, blank=True)
    Endereço = models.CharField(max_length=50, null=True, blank=True)
    Telefone = models.CharField(max_length=13, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Data_de_Cadastro = models.DateTimeField(default=datetime.now, null=True, blank=True)
    Status_do_Cliente = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('pago', 'Pago'),
        ('em debito', 'Em Débito'),
    ])
    Forma_de_Pagamento = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('pix', 'Pix'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
    ])
    Livro_Emprestado = models.CharField(max_length=50, null=True, blank=True)
    Data_de_Entrega_do_Livro = models.DateField(auto_now=False, null=True, blank=True)
    Data_de_Devolução = models.DateField(auto_now=False, null=True, blank=True)
    
