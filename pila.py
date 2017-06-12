class nodosimple():
	"""docstring for nodosimple"""
	def __init__(self,dato,indice):
		
		self.dato = dato
		self.nodosiguiente	=  None
		self.indice = indice
class pila():
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		#print("entro push")
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			nuevo.nodosiguiente = self.cabeza
			self.cabeza = nuevo

	def pop(self):
		if self.cabeza != None:
			aux = None
			aux = self.cabeza
			self.cabeza = self.cabeza.nodosiguiente
			return aux.dato
		return "null"	
	def peek(self):
		if self.cabeza != None:
			return self.cabeza.dato

	def recorrerPila(self):
		
		while self.cabeza!= None:
			print self.cabeza.dato

		 	self.cabeza = self.cabeza.nodosiguiente

	def recorrerOperar(self , linea):
		lineaSplit = linea.split(" ")


		for x in range(len(lineaSplit)):
			if (lineaSplit[x] == "+" or lineaSplit[x] == "-" or lineaSplit[x] == "*" ):
					self.push(lineaSplit[x])
					print ( " op: " + lineaSplit[x])
					operando = self.pop()
					print  ( "op  : " + str(operando))
					a = self.pop()
					print  ( "num  : " + str(a))
					b = self.pop()
					print  ( "num  : " + str(b))
					c = 0
					if( operando == "+"):
						c = int(a) + int(b)
					elif(operando == "-"):
						c = int(b) - int(a)	
					elif(operando == "*"):
						c = int(a) * int(b)
					print  ( "respuesta  : " + str(c))	
					self.push(c)	

			else:		
				self.push(lineaSplit[x])

			
		

