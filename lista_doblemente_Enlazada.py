import cola
class nodolista():
	def __init__(self,usuario,passw,cola):
		self.usuario = usuario
		self.passw = passw
		self.cola = cola
		self.matriz = None
		self.siguiente = None
		self.anterior = None
class lista():

	
	def __init__(self):
		self.cabeza = None
	def add(self,usuario,passw):
		cola2 = cola.listaCola()		

		nuevoNodo = nodolista(usuario,passw,cola2) 

		if self.cabeza == None:
			nuevoNodo.siguiente = nuevoNodo
			nuevoNodo.anterior = nuevoNodo
			self.cabeza = nuevoNodo
			bandera = True
			
		else:
			nodoTemporal = self.cabeza.anterior

			self.cabeza.anterior = nuevoNodo
			nuevoNodo.anterior = nodoTemporal
			nuevoNodo.siguiente = self.cabeza
			nodoTemporal.siguiente =nuevoNodo

		return True
	def addCola(self,usuario,objeto):
		buscarUsuarios(usuario).cola = objeto
	

	def recorrer(self):
		temporal = self.cabeza.anterior
		print self.cabeza.usuario
		print self.cabeza.passw	
		while temporal!=self.cabeza:
			print temporal.usuario
			print temporal.passw
			temporal = temporal.anterior

	def buscar(self,us):
		if self.cabeza.usuario== us :
			var = temporal
			return var
		while temporal!=self.cabeza:
			if temporal.usuario== us :
				return temporal
			else:return False
			temporal = temporal.anterior

	def login(self, usuario , password):
		temporal = self.cabeza.anterior
		#print self.cabeza.usuario
		#print self.cabeza.passw	
		if self.cabeza.usuario== usuario and self.cabeza.passw== password:
			return True
		while temporal!=self.cabeza:
			if temporal.usuario== usuario and temporal.passw== password:
				return True
			else:return False
			temporal = temporal.anterior

	def recorrerUsuarios(self):
		temporal = self.cabeza.anterior
		primero = self.cabeza.usuario+"->"
		print primero,
		while temporal!=self.cabeza:
			var = temporal.usuario+"->"
			print var,
			temporal = temporal.anterior
		print ""

	def buscarUsuarios(self, usua):
		print usua + "<-este "
		try:
			temporal = self.cabeza.anterior
		except Exception, e:
			print e

		
		primero = self.cabeza.usuario
		if primero == usua:
			return temporal
		while temporal!=self.cabeza:
			var = temporal.usuario
			if (var == usua ):
				return temporal
			else:
				return None
			temporal = temporal.anterior

			
	def recorrerPass(self):
		temporal = self.cabeza.anterior
		print self.cabeza.passw
		while temporal!=self.cabeza:

			print temporal.passw
			temporal = temporal.anterior		
	
#listanueva = lista()
#listanueva.add("nowell3","123")
#listanueva.add("nowell4","123")
#print listanueva.buscarUsuarios("nowell4").passw