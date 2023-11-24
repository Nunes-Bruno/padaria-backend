from django.http import HttpResponse
from django.shortcuts import render
from .forms import MeuFormulario
import sqlite3
import json

# Create your views here.
def home(request):
    connection = sqlite3.connect('produtos-sqlite.db')

    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtos(
                   produtos_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   items TEXT
                    )           
                    ''')
    if request.method == "POST":
        print("Ação realizada com sucesso")
        items = request.POST.getlist('item[]')
        print(f"Lista de compras: {items}")
        if items:
            lista_compra = [(item,) for item in items]
            cursor.executemany('''
                            INSERT INTO Produtos (items) VALUES(?)
                            ''', lista_compra)
            cursor.execute("SELECT * FROM Produtos ")
            print(cursor.fetchall())
            connection.commit()
            connection.close()

        else:
            print('Lista de compras vazia!')
        
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

