from flask import Flask, jsonify, request 

app = Flask(__name__)

Alunos = "C:\Users\Administrador\Documents\T.F\API_Flask\northwind.sql"; 

# Rota para listar todos os Alunos
@app.route('', methods=['GET'])
def obter_alunos():
    return jsonify(Alunos)

# Rota para obter um Alunos específico
@app.route('/Alunos/<int:aluno_id>', methods=['GET'])
def obter_alunos(aluno_id):
    alunos = next((a for a in alunos if a["id"] == aluno_id), None)
    if alunos:
        return jsonify(alunos)
    return jsonify({"erro": "Aluno não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)