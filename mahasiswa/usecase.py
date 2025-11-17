from mahasiswa.repo import RepoData

class Usecase:

    @staticmethod
    def getAll():
        return RepoData.getAllData()

    @staticmethod
    def getSingle(nim):
        return RepoData.getSingle(nim)

    @staticmethod
    def update(data):
        nim = data.get('nim')
        nama = data.get('nama')
        tahun_masuk = data.get('tahun_masuk')
        alamat = data.get('alamat')
        tanggal_lahir = data.get('tanggal_lahir')
        id_jurusan = data.get('id_jurusan')
        return RepoData.updateData(nim, nama, tahun_masuk, alamat, tanggal_lahir, id_jurusan)

    @staticmethod
    def delete(nim):
        return RepoData.deleteData(nim)

    @staticmethod
    def post(data):
        nim = data.get('nim')
        nama = data.get('nama')
        tahun_masuk = data.get('tahun_masuk')
        alamat = data.get('alamat')
        tanggal_lahir = data.get('tanggal_lahir')
        id_jurusan = data.get('id_jurusan')
        return RepoData.insertData(nim, nama, tahun_masuk, alamat, tanggal_lahir, id_jurusan)
