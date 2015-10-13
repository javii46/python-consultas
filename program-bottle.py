#!/usr/bin/env python
#coding:utf-8
import bottle
import bottle_mysql
import bottle_pgsql
import MySQLdb
import psycopg2
import cx_Oracle
import pymongo
from pymongo import MongoClient
from bottle import route, run, template, debug, static_file, TEMPLATE_PATH, request

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@route('/')
def search():
    return template('inicio')

DB_HOST_mysql = '172.22.202.217'
DB_USER_mysql = 'cliente2'
DB_PASS_mysql = 'usuario'
DB_NAME_mysql = 'remoto'



def consultamysql(query=''): 
    datos = [DB_HOST_mysql, DB_USER_mysql, DB_PASS_mysql, DB_NAME_mysql] 
  
    conectar = MySQLdb.connect(*datos) 
    cursor = conectar.cursor()
             
    datos= cursor.execute(query)          
 
    datos = cursor.fetchall()   
 
    cursor.close()                 
    conectar.close()                   
    return datos
 

@route('/mysql')
def mysql():
    query = "select * from clientes;"
    resultado = consultamysql(query)
    return template('buscarmysql', resultado=resultado)
	


def consultapostgres(query1=''): 
 
    conectar1 = psycopg2.connect(host="172.22.202.249",
                                 user="javier",
                                 password="usuario",
                                 database="acceso")
    cursor1 = conectar1.cursor()         
    cursor1.execute(query1)          
 
    datos = cursor1.fetchall()   

    cursor1.close()                
    conectar1.close()                  
    return datos

@route('/postgres') 
def postgres():
    query1 = "select * from clientes;"
    resultado1 = consultapostgres(query1)
    return template('buscarpostgres', resultado1=resultado1)

@route('/login')
def login():
    return template ('login')


@route('/login',method='POST') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=="javier" and password=="javier":
        return template ('logincorrecto')
    else:
        return template ('denegado')

def consultaoracle(query2=''): 

    conexion='javier/javier@10.10.10.2:1521/orcl'
    db_conn = cx_Oracle.connect(conexion)
    cursor_2 = db_conn.cursor()
    cursor_2.execute(query2)
    registros = cursor_2.fetchall()
      
    cursor_2.close()
    db_conn.close()
    return registros

@route('/oracle')
def oracle():
    tabla  = raw_input('Escribe el nombre de la tabla: ') 
    print tabla
    query2 = "select * from %s" % (tabla)
    print query2
    resultado2 = consultaoracle(query2)
    return template('buscaroracle', resultado2=resultado2)
      
@route('/Mongodb')
def consultamongo():
    host = '11.0.0.2'
    cliente = MongoClient('mongodb://'+host+':27017/')
    base_datos = cliente["practica"]
    coleccion = base_datos["remoto"]
    resultado3 = coleccion
    return template('buscarmongo', resultado3=resultado3)


debug='TRUE'
run(host='localhost', port=8080)