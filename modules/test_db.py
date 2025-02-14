from db import conectar

conn = conectar()

if conn:
    conn.close()
