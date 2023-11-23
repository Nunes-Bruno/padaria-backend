from django.http import HttpResponse
from django.shortcuts import render
from .forms import MeuFormulario
import sqlite3

# Create your views here.
def home(request):
    if request.method == "POST":
        print("Ação realizada com sucesso")
        items = request.POST.getlist('item[]')
        print(f"Lista de compras: {items}")
    return render(request, 'painel_inicial/home.html')


def cadastro(request):
    connection = sqlite3.connect('clientes-sqlite.db')

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes(
                   cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   telefone TEXT
                        )
                    ''')
    
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        telefone_digitado = request.POST.get('telefone')
        print(f"nome digitado: {nome_digitado}")
        print(f"telefone digitado: {telefone_digitado}")
        cliente_cadastrado = [(nome_digitado, telefone_digitado)]
        cursor.executemany('''
                            INSERT INTO Clientes (nome, telefone) VALUES(?,?)
                            ''', cliente_cadastrado)
        cursor.execute("SELECT * FROM Clientes ")
        print(cursor.fetchall())
        connection.commit()
        connection.close()
        return render(request, 'painel_inicial/cadastro.html', {'nome': nome_digitado, 'telefone':telefone_digitado})
    return render(request, 'painel_inicial/cadastro.html')

