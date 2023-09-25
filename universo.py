FROM abc import ABC, abstractclassmethod
class unidimensional(ABC):
  
  def __init__(self):
      self.volumen=0
      self.masa=0
      print("soy unidimensional")
    




if(__name__=="__main__"):
    print("estoy en el programa principal")
    c = unidimensional()
    