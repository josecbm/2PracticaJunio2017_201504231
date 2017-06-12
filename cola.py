import pila
class nodoLista(object):
	"""docstring for listaCola"""
	def __init__(self,dato):
		
		self.dato =dato 
		self.siguiente = None
		self.aux = None
class listaCola():
	global listapila
	listapila = pila.pila()

	def __init__(self):
		self.cabeza = None
	def add(self , dato):
		nuevoNodo = nodoLista(dato)

		if self.cabeza == None:
			nuevoNodo.siguiente = None
			self.cabeza = nuevoNodo
		else:
			self.aux = self.cabeza
			while self.aux.siguiente!=None:
				self.aux = self.aux.siguiente
			self.aux.siguiente=nuevoNodo
			
	def recorrer(self):
		self.aux = self.cabeza
		while self.aux!=None:
			print self.aux.dato
			listapila.recorrerOperar(self.aux.dato)
			self.aux = self.aux.siguiente
	def desencolar(self):
		if self.cabeza!=None:
			aux = self.cabeza
			self.cabeza = self.cabeza.siguiente
			return aux.dato


#listita = listaCola()
#listita.add("1")

#listita.add("2")
#listita.add("3")
#listita.add("4")
#listita.recorrer()