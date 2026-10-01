from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="API Data Mahasiswa",
    description="Tugas 1 Integrasi Sistem - CRUD Data Mahasiswa"
)

# Struktur Data Objek (Model)
class Mahasiswa(BaseModel):
    id: int
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# Database sementara di memori (In-Memory Database)
db_mahasiswa: List[Mahasiswa] = [
    Mahasiswa(
        id=1,
        nama="Zen",
        alamat="Salatiga",
        ipk=3.85,
        semester=5,
        hobi="Coding"
    )
]

# 1. GET: Ambil Semua Data Mahasiswa
@app.get("/mahasiswa", response_model=List[Mahasiswa], summary="Tampilkan Semua Data")
def get_all_mahasiswa():
    return db_mahasiswa

# 2. GET: Ambil Data Mahasiswa Berdasarkan ID
@app.get("/mahasiswa/{mhs_id}", response_model=Mahasiswa, summary="Tampilkan Data by ID")
def get_mahasiswa_by_id(mhs_id: int):
    for mhs in db_mahasiswa:
        if mhs.id == mhs_id:
            return mhs
    raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")

# 3. POST: Tambah Data Mahasiswa Baru
@app.post("/mahasiswa", response_model=Mahasiswa, status_code=201, summary="Tambah Data Baru")
def create_mahasiswa(mhs: Mahasiswa):
    for item in db_mahasiswa:
        if item.id == mhs.id:
            raise HTTPException(status_code=400, detail="ID Mahasiswa sudah ada")
    db_mahasiswa.append(mhs)
    return mhs

# 4. PUT: Perbarui Data Mahasiswa Berdasarkan ID
@app.put("/mahasiswa/{mhs_id}", response_model=Mahasiswa, summary="Update Data by ID")
def update_mahasiswa(mhs_id: int, updated_mhs: Mahasiswa):
    for index, mhs in enumerate(db_mahasiswa):
        if mhs.id == mhs_id:
            db_mahasiswa[index] = updated_mhs
            return updated_mhs
    raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")

# 5. DELETE: Hapus Data Mahasiswa Berdasarkan ID
@app.delete("/mahasiswa/{mhs_id}", summary="Hapus Data by ID")
def delete_mahasiswa(mhs_id: int):
    for index, mhs in enumerate(db_mahasiswa):
        if mhs.id == mhs_id:
            db_mahasiswa.pop(index)
            return {"message": f"Data mahasiswa dengan ID {mhs_id} berhasil dihapus"}
    raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")