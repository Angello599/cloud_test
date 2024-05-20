from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "54.81.5.255"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "api_usuarios"  

@app.get("/")
def get_success():
    return {"message": "success"}

@app.get("/usuarios")
def get_usuarios():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    result = cursor.fetchall()
    mydb.close()
    return {"usuarios": result}

@app.get("/usuarios/{id}")
def get_usuario(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM Usuarios WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"usuario": result}

@app.post("/usuarios")
def add_usuario(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    nombre = item.nombre
    direccion = item.direccion
    cursor = mydb.cursor()
    sql = "INSERT INTO Usuarios (nombre, direccion) VALUES (%s, %s)"
    val = (nombre, direccion)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Usuario agregado exitosamente"}

@app.put("/usuarios/{id}")
def update_usuario(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    nombre = item.nombre
    direccion = item.direccion
    cursor = mydb.cursor()
    sql = "UPDATE Usuarios set nombre=%s, direccion=%s where id=%s"
    val = (nombre, direccion, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Usuario modificado exitosamente"}

@app.delete("/usuarios/{id}")
def delete_usuario(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM Usuarios WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Usuario eliminado exitosamente"}
