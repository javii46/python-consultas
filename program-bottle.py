#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias python necesarios para crear las conexiones 
# con los distintos SGBD 

import bottle
import bottle_mysql 
import bottle_pgsql 
import MySQLdb                                               # conexión MySQL
import psycopg2                                              # conexión PostgreSQL
import cx_Oracle                                             # conexión Oracle
import pymongo                                               # conexión  mongo
from pymongo import MongoClient
from bottle import route, run, template, debug, static_file, TEMPLATE_PATH, request

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

# definimos la ruta raiz en bottle que nos mostrara el template inicio

@route('/')
def search():
    return template('inicio')

# definimos las variables de conexion de MySQL.

DB_HOST_mysql = '172.22.202.217'
DB_USER_mysql = 'cliente2'
DB_PASS_mysql = 'usuario'
DB_NAME_mysql = 'remoto'



def consultamysql(query=''): 
    datos = [DB_HOST_mysql, DB_USER_mysql, DB_PASS_mysql, DB_NAME_mysql] 
  
    conectar = MySQLdb.connect(*datos)                        # conecta a la base de datos con los parametros de las variables.
    cursor = conectar.cursor()                                # creamos cursor.
             
    datos= cursor.execute(query)                              # cursor ejecuta la consulta.         
 
    datos = cursor.fetchall()                                 # Con la funcion fetchall nos traemos los datos.
 
    cursor.close()                                            # cierra el cursor.            
    conectar.close()                                          # cierra la conexion con la base de datos.                
    return datos
 

@route('/mysql')
def mysql():
    query = "select * from clientes2;"
    resultado = consultamysql(query)
    return template('buscarmysql', resultado=resultado)
	


def consultapostgres(query1=''): 
 
    conectar1 = psycopg2.connect(host="172.22.202.249",        # definimos las variables para la conexión
                                 user="javier",                # con la base de datos
                                 password="usuario",
                                 database="acceso")
    cursor1 = conectar1.cursor()                               # creamos cursor      
    cursor1.execute(query1)                                    # ejecutamos la consulta  
 
    datos = cursor1.fetchall()                                 # Trae el resultado de la consulta

    cursor1.close()                                            # cierra cursor          
    conectar1.close()                                          # cierra la conexion              
    return datos

@route('/postgres') 
def postgres():
    query1 = "select * from clientes;"
    resultado1 = consultapostgres(query1)
    return template('buscarpostgres', resultado1=resultado1)

@route('/login')
def login():
    return template ('login')


@route('/login',method='POST')                                 # función para autenticarse en la base de datos oracle
def do_login():
    username = request.forms.get('username')                   # obtenemos a partir de la plantilla un nombre de usuario
    password = request.forms.get('password')                   # obtenemos a partir de la plantilla una password
    if username=="javier" and password=="javier":
        return template ('logincorrecto')
    else:
        return template ('denegado')

def consultaoracle(query2=''): 

    conexion='javier/javier@10.10.10.2:1521/orcl'              # cadena de conexion.
    db_conn = cx_Oracle.connect(conexion)                      # conecta con la base de datos.
    cursor_2 = db_conn.cursor()                                # abre cursor.
    cursor_2.execute(query2)                                   # ejecuta la consulta.
    registros = cursor_2.fetchall()                            # se trae el resultado.
      
    cursor_2.close()                                           # cierra cursor.
    db_conn.close()                                            # cierra la conexion.
    return registros

@route('/oracle')
def oracle():
    tabla  = raw_input('Escribe el nombre de la tabla: ') 
    query2 = "select * from %s" % (tabla)
    resultado2 = consultaoracle(query2)
    return template('buscaroracle', resultado2=resultado2)
      
@route('/Mongodb')
def consultamongo():
    host = '11.0.0.2'                                          # define el host del servidor mongo (se encuentra alojado en maquina vagrant.)
    cliente = MongoClient('mongodb://'+host+':27017/')         # conexión base de datos.
    base_datos = cliente["practica"]                           # indica la base de datos
    coleccion = base_datos["remoto"]                           # indica la colección 
    resultado3 = coleccion                                     # introduce la coleccion en una 
    return template('buscarmongo', resultado3=resultado3)


debug='TRUE'
run(host='localhost', port=8080)