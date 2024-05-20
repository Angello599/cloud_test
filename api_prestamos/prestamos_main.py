from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "54.81.5.255"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "api_prestamos"  

@app.get("/")
def get_success():
    return {"message": "success"}

@app.get("/prestamos")
def get_prestamos():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Prestamos")
    result = cursor.fetchall()
    mydb.close()
    return {"prestamos": result}

@app.get("/prestamos/{id}")
def get_prestamo(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM Prestamos WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"prestamo": result}

@app.post("/prestamos")
def add_prestamo(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    usuario_id = item.usuario_id
    libro_id = item.libro_id
    fecha_prestamo = item.fecha_prestamo
    fecha_devolucion = item.fecha_devolucion
    cursor = mydb.cursor()
    sql = "INSERT INTO Prestamos (usuario_id, libro_id, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)"
    val = (usuario_id, libro_id, fecha_prestamo, fecha_devolucion)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Préstamo agregado exitosamente"}

@app.put("/prestamos/{id}")
def update_prestamo(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    usuario_id = item.usuario_id
    libro_id = item.libro_id
    fecha_prestamo = item.fecha_prestamo
    fecha_devolucion = item.fecha_devolucion
    cursor = mydb.cursor()
    sql = "UPDATE Prestamos set usuario_id=%s, libro_id=%s, fecha_prestamo=%s, fecha_devolucion=%s where id=%s"
    val = (usuario_id, libro_id, fecha_prestamo, fecha_devolucion, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Préstamo modificado exitosamente"}

@app.delete("/prestamos/{id}")
def delete_prestamo(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM Prestamos WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Préstamo eliminado exitosamente"}
