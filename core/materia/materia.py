class Materias:
    def __init__(self,id=None, nome="",sigla_curricular="",descricao=""):
        self.__id = id
        self.__nome = nome
        self.__sigla_curricular = sigla_curricular
        self.__descricao = descricao


        @property
        def id(self):
            return self.id
        @id.setter
        def id (self,novo_id):
            self.__id = novo_id

        @property
        def nome(self):
            return self.nome
        @nome.setter
        def nome (self,novo_nome):
            self.__nome = novo_nome

        @property
        def sigla_curricular(self):
            return self.__sigla__curricular
        @sigla__curricular.setter
        def sigla__curricular (self,nova_sigla__curricular):
            self.__sigla__curricular = nova_sigla__curricular

        @property
        def descricao(self):
            return self.__descricao
        @descricao.setter
        def descricao(self,nova_descricao):
            self.__descricao = nova_descricao