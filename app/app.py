from turtle import title
from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
app = Flask(__name__)
DB_conf = { 'user': 'root', 'password': 'root', 'host': 'db',
            'port': '3306', 'database': 'images' }

def test_table():
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM images_tab')
   results = [c for c in cursor]
   cursor.close()
   connection.close()
   return results

def add_item(title, link, description):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"INSERT INTO images_tab (title, link, description) VALUES ('{title}', '{link}','{description}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

def delete_items(title):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"DELETE FROM images_tab WHERE title = ('{title}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

@app.route('/')
def index():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Images</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Image list</h1>\n"
   S += "      <table>\n"
   S += "      <tr><th>Title</th><th>Link</th><th>Description</th>\n"
   for (title, link, description) in test_table():
      S += f"        <tr><td>{title}</td><td> <a href={link}>{link}</a></td><td> {description}</td></tr>\n"
   S += "      </table>\n"
   S += "      <p><a href='/addform'>Add new image</a></p>\n"
   S += "      <p><a href='/deleteform'>Delete a image</a></p>\n"
   S += "      <p><a href='/list'>List images</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/add')
def add():
   title = request.args.get("title", "", str)
   link = request.args.get("link", "", str)
   description = request.args.get("description", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Added a new image</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Added a new image</h1>\n"
   if title != "" and link != "" and description != "":
      S += add_item(title, link, description)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/delete')
def delete():
   title = request.args.get("title", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Removed an image from the list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Removed an image from the list</h1>\n"
   if title != "":
      S += delete_items(title)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/list')
def list():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Image list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Image list</h1>\n"
   S += "      <ul>\n"
   for ((title, link, description)) in test_table():
      S += f"         <li><a href={link}><img src= {link} width=150></a> </li>\n"
   S += "      </ul>\n"
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/addform')
def addform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <head>\n"
    S += " <title>Entering a value</title>\n"
    S += style()
    S += " </head>\n"
    S += " <body>\n"
    S += " <h1>Entering a value</h1>\n"
    S += " <form action='/add'>\n"
    S += " <input type='text' name='title' value='Title'/>\n"
    S += " <input type='text' name='link' value='Link'/>\n"
    S += " <input type='text' name='description' value='Description'/>\n"
    S += " <input type='submit' value='Submit'/>\n"
    S += " </form>\n"
    S += " <p><a href='/'>Back!</a></p>\n"
    S += " </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <head>\n"
    S += " <title>Deleting an image</title>\n"
    S += style()
    S += " </head>\n"
    S += " <body>\n"
    S += " <h1>Deleting an image</h1>\n"
    S += " <form action='/delete'>\n"
    S += " <input type='text' name='title' value=''/>\n"
    S += " <input type='submit' value='Submit'/>\n"
    S += " </form>\n"
    S += " <p><a href='/'>Back!</a></p>\n"
    S += " </body>\n"
    S += "</html>\n"
    return S

def style():
    S = "<style>\n"
    S += " body {background-color: #FFEEDD; }\n"
    S += "</style>\n"
    return S

if __name__ == '__main__':
   app.run(host='0.0.0.0')