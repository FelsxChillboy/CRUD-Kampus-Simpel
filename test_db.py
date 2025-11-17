from mahasiswa.repo import get_db_connection

conn = get_db_connection()
if conn:
    print("✅ Koneksi ke database kampus_db BERHASIL!")
    conn.close()
else:
    print("❌ Gagal konek ke database.")
