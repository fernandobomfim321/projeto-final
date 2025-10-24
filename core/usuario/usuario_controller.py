from flask import Blueprint, request, jsonify
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario

service = UsuarioService()

usuario_controller = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_controller.route('/', methods=['GET'])
def listar():
    objeto = service.listar_usuarios()
    return jsonify(objeto)

@usuario_controller.route('/', methods=['POST'])
def adicionar():
    dados = request.get_json()
    obj = Usuario(id=0, usuario=dados["usuario"],
                      senha=dados["senha"],
                      ativo=dados["ativo"])
    objeto = service.adicionar_usuario(obj)
    return jsonify(objeto), 201

@usuario_controller.route('/<int:id>', methods=['GET'])
def obter(id):
    objeto = service.obter_usuario_por_id(id)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404

@usuario_controller.route('/<int:id>', methods=['DELETE'])    
def remover(id):
    sucesso = service.remover_usuario(id)
    return jsonify(sucesso)

@usuario_controller.route('/', methods=['PUT'])
def atualizar():
    dados = request.get_json()
    obj = Usuario(id=dados["id"], usuario=dados["usuario"],
                      senha=dados["senha"], ativo=dados["ativo"])
    objeto = service.atualizar_usuario(obj)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404