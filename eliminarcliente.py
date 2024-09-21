import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='root',
                            host='127.0.0.1',
                            database='db_clientes')

cursor = conexion.cursor()

# Borrar cliente
sql = 'DELETE FROM clientes WHERE idcliente = %s'

# Solicitar ID al usuario
id_cliente = int(input("Ingrese ID de la persona a eliminar: "))

# Ejecutar la consulta
try:
    cursor.execute(sql, (id_cliente,))
    conexion.commit()
    
    registro_eliminado = cursor.rowcount
    print(f'Registros eliminados: {registro_eliminado}')
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    cursor.close()
    conexion.close()
