from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="kampus_db",
    user="postgres",
    password="PASSWORD_POSTGRESMU"
)

cur = conn.cursor()


# --- GET (tampilkan semua mahasiswa) ---
@app.route("/mahasiswa", methods=["GET"])
def get_mahasiswa():
    cur.execute("""
        SELECT m.nim, m.nama, m.tahun_masuk, m.alamat, m.tanggal_lahir, j.nama_jurusan
        FROM mahasiswa m
        JOIN jurusan j ON m.id_jurusan = j.id
    """)
    rows = cur.fetchall()

    data = []
    for r in rows:
        data.append({
            "nim": r[0],
            "nama": r[1],
            "tahun_masuk": r[2],
            "alamat": r[3],
            "tanggal_lahir": str(r[4]),
            "jurusan": r[5]
        })

    return jsonify(data)


# --- POST (tambah mahasiswa baru) ---
@app.route("/mahasiswa", methods=["POST"])
def add_mahasiswa():
    data = request.json

    cur.execute("""
        INSERT INTO mahasiswa (nim, nama, tahun_masuk, alamat, tanggal_lahir, id_jurusan)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data["nim"],
        data["nama"],
        data["tahun_masuk"],
        data["alamat"],
        data["tanggal_lahir"],
        data["id_jurusan"]
    ))

    conn.commit()

    return jsonify({"status": "success", "message": "Mahasiswa ditambahkan"})


if __name__ == "__main__":
    app.run(debug=True)
