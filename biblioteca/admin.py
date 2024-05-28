from django.contrib import admin
from biblioteca.models import Livro
from biblioteca.models import Funcionario
from biblioteca.models import Cliente

# Register your models here.

class Livros(admin.ModelAdmin):
    list_display = ('id', 'Nome_Do_Livro', 'Autor', 'Editora', 'Paginas', 'Ano_Publicação', 'Gênero', 'Código', 'Observações', 'Data_de_Entrada_do_Livro')
    search_fields = ('Nome_Do_Livro',)

class Funcionarios(admin.ModelAdmin):
    list_display = ('id', 'Nome_Do_Funcionario', 'CPF_Funcionario', 'Data_de_Nascimento', 'Data_de_Contratação', 'Endereço', 'Telefone')
    search_fields = ('CPF_Funcionario',)

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'Nome_Do_Cliente', 'CPF_Cliente', 'Data_de_Nascimento', 'Endereço', 'Telefone', 'Email', 'Data_de_Cadastro', 'Status_do_Cliente', 'Forma_de_Pagamento', 'Livro_Emprestado', 'Data_de_Entrega_do_Livro', 'Data_de_Devolução')
    search_fields = ('CPF_Cliente',)



admin.site.register(Livro, Livros)
admin.site.register(Funcionario, Funcionarios)
admin.site.register(Cliente, Clientes)
