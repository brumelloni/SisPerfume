import sqlite3
path=r'C:\sqlite\databases'
#O nome do banco criado foi dbperfumes-v2.db. Se você criar com outro nome, troque aqui
banco=sqlite3.connect(path+r'\dbperfumes-v2.db')
'''
Essa função insere um marca no banco de dados, recebendo como parâmetro o nome da marca
'''
def inserirMarca(nome_marca):
    sql="insert into Marcas (nome) values('{0}')".format(nome_marca)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
'''
Essa função atualiza uma marca no banco de dados, recebendo como parâmetros
o id e o nome. O id é necessário para ser usado na instrução update
'''
def atualizarMarca(id,nome):
    sql="update Marcas set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
'''
Essa função localiza uma marca pelo seu nome, partindo do pressuposto que não
existirão marcas com nomes iguais
'''
def localizarMarcaPorNome(nome):
    sql="select * from Marcas where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    marca=cursor.fetchone()
    cursor.close()
    return marca
'''
Essa função retorna uma lista Python com todas as marcas cadastradas no banco de dados,
trazendo o id o nome da marca
'''
def listarMarca():
    sql="select * from Marcas"
    cursor=banco.cursor()
    cursor.execute(sql)
    marcas=cursor.fetchall()
    cursor.close()
    return marcas
'''
Essa função retorna uma lista Python contendo o nome de todas marcas,
ordenadas pelo nome
'''
def listarMarcaNome():
    sql="select nome from Marcas order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_marcas=cursor.fetchall()
    cursor.close()
    marcas=[]
    for nome_marca in nome_marcas:
        marcas.append(nome_marca[0])
    return marcas