class aluno:
     def __init__(self, id=0, nome=''):
       self.__id = id 
       self.__nome = nome

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