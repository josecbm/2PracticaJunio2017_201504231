class nodolista():
	def __init__(self,usuario,passw):
		self.usuario = usuario
		self.passw = passw
		self.siguiente = None
		self.anterior = None
class lista():
	def __init__(self):
		self.cabeza = None
	def add(self,usuario,passw):
		nuevoNodo = nodolista(usuario,passw) 

		if self.cabeza == None:
			nuevoNodo.siguiente = nuevoNodo
			nuevoNodo.anterior = nuevoNodo
			self.cabeza = nuevoNodo
			
		else:
			nodoTemporal = self.cabeza.anterior

			self.cabeza.anterior = nuevoNodo
			nuevoNodo.anterior = nodoTemporal
			nuevoNodo.siguiente = self.cabeza
			nodoTemporal.siguiente =nuevoNodo
	def recorrer(self):
		temporal = self.cabeza.anterior
		print self.cabeza.usuario
		print self.cabeza.passw	
		while temporal!=self.cabeza:
			print temporal.usuario
			print temporal.passw
			temporal = temporal.anterior

listanueva = lista()
listanueva.add("nowell0","123")
listanueva.add("nowell1","123")
listanueva.add("nowell2","123")
listanueva.add("nowell3","123")
listanueva.add("nowell4","123")

listanueva.recorrer()