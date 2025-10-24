from flask import Blueprint, request , jsonify
from core.professor.professor_service import ProfessorService
from core.professor.aluno import Aluno
from core.autenticacao.autenticacao import autenticacao

professor_service = AlunoService()

professor_controller = Blueprint('professor',__name__, url_prefix= '/professor')

@aluno_controller.route('/', methods=['GET'])
@autenticacao
def listar_professor():
    alunos = professor_service.listar_alunos()
    return jsonify(alunos)


@aluno_controller.route ( '/', methods = ['POST'])
@autenticacao
def adicionar_professor():
    dados = request.get_json()
    obj_professor = Professor(0, dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
    professor = professor_service.adicionar_professor(obj_professor)
    return professor, 201


@aluno_controller.route("/<int:id>", methods=['GET'])
@autenticacao
def obter_professor(id):
    professor = professor_service.obter_professor_por_id(id)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro:professor não encontrado"}), 404
def remover_professor(id):
     sucesso = professor_service.remover_professor(id)
     return jsonify(sucesso)
def atualizar_professor():
    dados = request.get_json()
    obj_professor = professor(id=dados["id"], nome=dados["nome"],
                   idade=dados["idade"], cpf=dados["cpf"])
    professor = professor_service.atualizar_professor(obj_professor)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro":"professor não encontrado"})