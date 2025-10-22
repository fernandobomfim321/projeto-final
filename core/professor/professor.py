class Professor:
    def __init__(self,id=None, nome="",idade=""):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__formacao = formacao

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
        def idade(self):
            return self.idade
        @idade.setter
        def idade (self,novo_idade):
            self.__idade = novo_idade

        @property
        def formacao(self):
            return self.formacao
        @formacao.setter
        def formacao (self,novo_formacao):
            self.__formacao = novo_id