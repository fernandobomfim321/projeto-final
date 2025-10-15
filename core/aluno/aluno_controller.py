from flask import Blueprint, request , jsonify
from core.aluno.aluno_service import alunoservice
from core.aluno.aluno import Aluno

aluno_service = alunoservice()

aluno_controller = blueprint("aluno",__name__, url__prefix= "\alunos")

@aluno_controller.route("/", methods=["GET"])
def listar_alunos():
    alunos = aluno_service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route ( "/", methods = ["POST"])
def adicionar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(0, dados["nome"])
    aluno_service.adicionar_aluno(obj_aluno)