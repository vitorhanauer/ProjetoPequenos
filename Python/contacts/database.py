import sqlite3
from sqlite3 import Error

def connect(caminho):
    global con
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)

def create_table(table_name,col_name=[],col_properties=[]):
    command = "CREATE TABLE IF NOT EXISTS "+table_name+"("
    for index in range(len(col_name)):
        if index != len(col_name)-1:
            command+= f'{col_name[index]} {col_properties[index]},'
        else:
            command+= f'{col_name[index]} {col_properties[index]}'
    command+=");"

    try:
        c = con.cursor()
        c.execute(command)
    except Error as ex:
        print(ex)

def insert_itens(table_name,col_name=[],col_values=[]):
    command = f'insert into {table_name} ('
    for c_name in col_name:
        if c_name != col_name[len(col_name)-1]:
            command+= f'{c_name},'
        else:
            command+= f"{c_name}) values("

    for c_values in col_values:
        if c_values != col_values[len(col_values)-1]:
            command+= f"{c_values},"
        else:
            command+= f"{c_values})"
    try:
        c = con.cursor()
        c.execute(command)
        con.commit()
    except Error as er:
        print(er)
        return False

def delete(table_name,col_name,col_item):
    command = f'delete from {table_name} where {col_name} = {col_item}' 
    try:
        c = con.cursor()
        c.execute(command)
        con.commit()
    except Error as er:
        print(er)

def update_itens(table_name,col_upd,upd,col_aux,value_aux):
    command = f"update {table_name} set {col_upd} = {upd} where {col_aux} = {value_aux}"
    try:
        c = con.cursor()
        c.execute(command)
        con.commit()
    except Error as er:
        print(er)

def select(table_name):
    command = f'select * from {table_name}'
    c = con.cursor()
    c.execute(command)
    result = c.fetchall()
    return result

def select_especific(table_name,col_name,search):
    command = f"select * from {table_name} where {col_name} like '%{search}%'"
    c = con.cursor()
    c.execute(command)
    result = c.fetchall()
    return result
