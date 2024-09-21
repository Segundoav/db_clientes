import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='root',
                            host='127.0.0.1',
                            database='db_clientes')

cursor = conexion.cursor()

# Solicitar datos al usuario
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")

# Definir la consulta SQL
sql = "INSERT INTO clientes (nombre, apellido, edad) VALUES (%s, %s, %s)"
datos = (nombre, apellido, edad)

# Ejecutar la consulta
cursor.execute(sql, datos)

# Guardar los cambios
conexion.commit()

print("Cliente insertado correctamente.")

cursor.close()
conexion.close()
