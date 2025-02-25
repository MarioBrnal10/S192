from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db"
    )
    cursor = conn.cursor()  # Crear el cursor correctamente
    cursor.execute("SELECT * FROM students")  # Ejecutar la consulta correctamente
    students = cursor.fetchall()  # Obtener los resultados

    cursor.close()  # Cerrar el cursor después de usarlo
    conn.close()  # Cerrar la conexión después de usarla

    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
