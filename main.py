from flask import Flask, request, jsonify
from mahasiswa.heandler import HandlerMahasiswa

app = Flask(__name__)

@app.route(' ', methods=['GET'])
def get_all():
    return jsonify(HandlerMahasiswa.getAll())

@app.route('/mahasiswa/get-single', methods=['POST'])
def get_single():
    return jsonify(HandlerMahasiswa.getSingle(request))

@app.route('/mahasiswa/update', methods=['PUT'])
def update():
    return jsonify(HandlerMahasiswa.update(request))

@app.route('/mahasiswa/delete', methods=['DELETE'])
def delete():
    return jsonify(HandlerMahasiswa.delete(request))

@app.route('/mahasiswa/post', methods=['POST'])
def post():
    return jsonify(HandlerMahasiswa.post(request))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8005, debug=True)
