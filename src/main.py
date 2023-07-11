import mysql.connector
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

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

app = FastAPI()


@app.get("/mahasiswa")
def read_mahasiswa():
    # Membuat kursor untuk eksekusi query
    cursor = conn.cursor()

    # Eksekusi query untuk membaca data dari tabel
    cursor.execute("SELECT * FROM mahasiswa")

    # Mendapatkan hasil query
    results = cursor.fetchall()

    # Mengembalikan hasil dalam bentuk list
    return results


@app.get("/mahasiswa/{nim}")
def read_mahasiswa(nim: int):
    # Membuat kursor untuk eksekusi query
    cursor = conn.cursor()

    # Eksekusi query untuk membaca data dari tabel berdasarkan NIM
    query = "SELECT * FROM mahasiswa WHERE nim_mhs = %s"
    cursor.execute(query, (nim,))

    # Mendapatkan hasil query
    result = cursor.fetchone()

    # Jika data tidak ditemukan, raise HTTPException dengan status 404
    if not result:
        raise HTTPException(status_code=404, detail="Mahasiswa not found")

    # Mengembalikan hasil dalam bentuk dictionary
    return {
        "nim_mhs": result[0],
        "nama_lengkap": result[1],
        "program_studi": result[2],
        "no_telepon": result[3]
    }
