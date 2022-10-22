'''En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será 
de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.'''
import sqlite3


def main():
    conn = sqlite3.connect('miDB.db')
    cursor = conn.cursor()
    try:   
        cursor.execute('''CREATE TABLE Alumnos
        (
            ID INT PRIMARY KEY,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL
        )''')     

        lista = [
        (1,'Jesus','Dominguez'),
        (2,'Miguel','Dominguez'),
        (3,'Jesus','Lotito'),
        (4,'Zamantha','Ruiz'),
        (5,'Imalu','Reyes'),
        (6,'Nancy','Lotito'),
        (7,'Coromoto','Rincones'),
        (8,'Miguel Angel','Dominguez')
        ]

        cursor.executemany("INSERT INTO Alumnos VALUES(?,?,?)",lista) 
        conn.commit()
    except:
        pass
    cursor.close()
    conn.close()

    buscar_alumno('Miguel Angel')

def buscar_alumno(nombre):
   
    conn = sqlite3.connect('miDB.db')
    cursor = conn.cursor()
        
    rows = cursor.execute(f'SELECT * FROM Alumnos WHERE Nombre="{nombre}"')

    print(rows.fetchone())
        
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
