import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(user='postgres',  # Cambié 'use' a 'user'
                            password='root',
                            host='127.0.0.1',  # Asegúrate de que esto esté correcto
                            database='db_clientes')

# Usar cursor
cursor = conexion.cursor()

sql = 'SELECT * FROM clientes'

cursor.execute(sql)

registro = cursor.fetchall()

print(registro)

cursor.close()
conexion.close()
