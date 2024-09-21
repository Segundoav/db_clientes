import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='root',
                            host='127.0.0.1',
                            database='db_clientes')

cursor = conexion.cursor()

# Solicitar ID y nuevos datos al usuario
id_cliente = input("Ingrese ID de la persona a editar: ")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")

# Definir la consulta SQL
sql = "UPDATE clientes SET nombre = %s, apellido = %s, edad = %s WHERE idcliente = %s"
datos = (nombre, apellido, edad, id_cliente)

# Ejecutar la consulta
cursor.execute(sql, datos)

# Guardar los cambios
conexion.commit()

print("Cliente actualizado correctamente.")

cursor.close()
conexion.close()
