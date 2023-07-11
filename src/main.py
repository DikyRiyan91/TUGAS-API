import mysql.connector
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel

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
    cursor.execute(query, (nim_mhs))

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
    
    
# Model untuk Mahasiswa
class Mahasiswa(BaseModel):
    nim_mhs: int
    nama_lengkap: str
    program_studi: str
    no_telepon: str


# Endpoint untuk membuat data mahasiswa
@app.post("/create_mahasiswa")
def create_mahasiswa(mahasiswa: Mahasiswa):
    cursor = conn.cursor()
    query = "INSERT INTO mahasiswa (nim_mhs, nama_lengkap, program_studi, no_telepon) VALUES (%s, %s, %s, %s)"
    values = (
        mahasiswa.nim_mhs,
        mahasiswa.nama_lengkap,
        mahasiswa.program_studi,
        mahasiswa.no_telepon,
    )
    cursor.execute(query, values)
    conn.commit()
    return {"message": "Data mahasiswa berhasil ditambahkan"}

# Endpoint untuk melakukan update data mahasiswa berdasarkan nim
@app.put("/update_mahasiswa/{nim_mhs}")
def update_mahasiswa(nim_mhs: int, mahasiswa: Mahasiswa):
    cursor = conn.cursor()
    update_query = """
        UPDATE mahasiswa
        SET nama_lengkap = %s, program_studi = %s, no_telepon = %s
        WHERE nim_mhs = %s
    """
    update_data = (mahasiswa.nama_lengkap, mahasiswa.program_studi, mahasiswa.no_telepon, nim_mhs)

    try:
        cursor.execute(update_query, update_data)
        conn.commit()
        if cursor.rowcount < 1:
            raise HTTPException(status_code=404, detail="Mahasiswa not found")
        return {"message": "Mahasiswa updated successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        cursor.close()