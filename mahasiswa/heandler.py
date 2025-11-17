from mahasiswa.usecase import Usecase

class HandlerMahasiswa:

    @staticmethod
    def getAll():
        return Usecase.getAll()

    @staticmethod
    def getSingle(request):
        kode = request.json.get('kode')
        return Usecase.getSingle(kode)

    @staticmethod
    def update(request):
        data = request.json
        return Usecase.update(data)

    @staticmethod
    def delete(request):
        kode = request.json.get('kode')
        return Usecase.delete(kode)

    @staticmethod
    def post(request):
        data = request.json
        return Usecase.post(data)
