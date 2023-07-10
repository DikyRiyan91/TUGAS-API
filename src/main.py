import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_host = os.getenv('DB_HOST')
db_username = os.getenv('DB_USERNAME') 
db_name = os.getenv('DB_NAME')

conn = mysql.connector.connect(
    host=db_host,
    user=db_username,
    password="",
    database=db_name
)

# Buat objek kursor untuk menjalankan query
cursor = conn.cursor()

# penggunaan - menjalankan query SELECT
query = "SELECT * FROM mahasiswa"
cursor.execute(query)

# Mendapatkan semua baris hasil query
result = cursor.fetchall()

# Menampilkan hasil query
for row in result:
    print(row)
    
# Menutup kursor dan koneksi ke database
cursor.close()
conn.close()