from models.medicoModel import Medico
from flask import jsonify, request

def create_medico():
    data = request.get_json()
    new_medico = Medico(nome=data['nome'], especialidade=data['especialidade'])
    new_medico.save()
    return jsonify({"message": "Médico criado com sucesso!"}), 201

def get_medicos():
    medicos = Medico.query.all()
    return jsonify([medico.to_dict() for medico in medicos]), 200

def get_medico(id):
    medico = Medico.query.get(id)
    if medico:
        return jsonify(medico.to_dict()), 200
    return jsonify({"message": "Médico não encontrado!"}), 404

def update_medico(id):
    data = request.get_json()
    medico = Medico.query.get(id)
    if medico:
        medico.nome = data['nome']
        medico.especialidade = data['especialidade']
        medico.save()
        return jsonify({"message": "Médico atualizado com sucesso!"}), 200
    return jsonify({"message": "Médico não encontrado!"}), 404

def delete_medico(id):
    medico = Medico.query.get(id)
    if medico:
        medico.delete()
        return jsonify({"message": "Médico deletado com sucesso!"}), 200
    return jsonify({"message": "Médico não encontrado!"}), 404
