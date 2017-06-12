class nodolista(object):
	"""docstring for nodolista"""
	def __init__(self,dato,x,y):
		
		self.dato = dato
		self.left = None
		self.right = None
		self.up = None
		self.down = None
class matriz():
 	"""docstring for matriz"""
 	def __init__(self):

 		self.cabeza = None
 		

 	def crearMatriz(self,x,y):

 		for contx in range(x):

 			for conty in range(y):
 				nuevoNodo = nodolista(0,x,y)
 				if self.cabeza == None:
	 				self.cabeza = nuevoNodo
	 				temporal = self.cabeza
	 				temporal2 = self.cabeza
	 			else:
	 				self.temporal.right = nuevoNodo
	 				self.nuevoNodo.left = temporal
	 			if x>0 :
	 				self.nuevoNodo.up = temporal2
	 				self.temporal2.down=nuevoNodo
	 			self.temporal2=temporal2.down
	def setValor(self, valor,fila,columna):
		temp = self.cabeza
		if fila<x and columna<y:

			for contx in range(fila):
				temp = temp.down	
			for conty in range(columna):
				temp = temp.right
			temp.setValor()
	def getValor(self,fila , columna):
		temp = self.cabeza
		if fila<x and columna<y:
			for contx in range(fila):
				temp = temp.down	
			for conty in range(columna):
				temp = temp.right
			return temp.dato

mat = matriz()
mat.crearMatriz(3,3)
print mat.getValor(2,2)





				

 		




 		
 	

		