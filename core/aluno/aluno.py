class Aluno:
     def __init__(self, id=0, nome='', idade=0, cpf=""):
       self.__id = id 
       self.__nome = nome
       self.__idade = idade
       self.__cpf = cpf

     @property
     def id (self):
          return self.__id
     @id.setter
     def id(self, novo__id):
          self.__id = novo__id
     @property
     def nome (self):
          return self.__nome
     @nome.setter
     def nome (self, novo__nome):
         self.__nome = novo__nome

     @property
     def idade (self):
          return self.__idade 
     @idade.setter
     def idade(self, novo__idade):
         self.__idade = novo__idade

     @property
     def cpf (self):
          return self.__cpf
     @cpf.setter
     def cpf(self, novo__cpf):
         self.__cpf = novo__cpf