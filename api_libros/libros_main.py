from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "54.81.5.255"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "api_libros"  

@app.get("/")
def get_success():
    return {"message": "success"}

@app.get("/libros")
def get_libros():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Libros")
    result = cursor.fetchall()
    mydb.close()
    return {"libros": result}

@app.get("/libros/{id}")
def get_libro(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM Libros WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"libro": result}

@app.post("/libros")
def add_libro(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    titulo = item.titulo
    autor = item.autor
    genero = item.genero
    disponibilidad = item.disponibilidad
    cursor = mydb.cursor()
    sql = "INSERT INTO Libros (titulo, autor, genero, disponibilidad) VALUES (%s, %s, %s, %s)"
    val = (titulo, autor, genero, disponibilidad)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Libro agregado exitosamente"}

@app.put("/libros/{id}")
def update_libro(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    titulo = item.titulo
    autor = item.autor
    genero = item.genero
    disponibilidad = item.disponibilidad
    cursor = mydb.cursor()
    sql = "UPDATE Libros set titulo=%s, autor=%s, genero=%s, disponibilidad=%s where id=%s"
    val = (titulo, autor, genero, disponibilidad, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Libro modificado exitosamente"}

@app.delete("/libros/{id}")
def delete_libro(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM Libros WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Libro eliminado exitosamente"}
