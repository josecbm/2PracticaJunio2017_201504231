import lista_doblemente_Enlazada
import operadorArchivo
import cola
import sys
class practica_1():
	"""docstring for practica_1"""
	usuario = ""
	password = ""
	global lista 
	global opArchivo
	global cola
	
	opArchivo = operadorArchivo.archivo()
	lista = lista_doblemente_Enlazada.lista()
	
	def __init__(self):
		self.hola = 0
	
	def crearUsr(self):
		print("Ingrese un usuario")
		usuario = raw_input()
		print("Ingrese una pass")
		password = raw_input()
		#print(usuario +""+password)

		if lista.add(usuario,password): 
			print("Usuario registrado")
			

		else:
			print("Usuario ya ingresado")
				
	def leerArchivo(self,u,lista):
		# En primer lugar debemos de abrir el fichero que vamos a leer.
		# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
		print("Ingrese ruta del archivo xml")
		ruta = raw_input()

		infile = open(ruta, 'r')

		# Mostramos por pantalla lo que leemos desde el fichero
		print("Lectura del fichero linea a linea")
		#for line in infile:
		    #print(line)

		opArchivo.operadorLinea(infile.read(),u,lista)
		# Cerramos el fichero.
		infile.close()
	def login(self):
		print("Ingrese sus credenciales")
		usuario = raw_input()
		contra = raw_input()
		if	lista.login(usuario,contra):
			self.ingresoSistema(usuario)
		else:
			print("Credenciales incorrectas")
			self.inicio()
	def ingresoSistema(self,u):
		
		while True:
			print("usuario logeado: "+u)
			print(""" Bienvenido al menu del sistema 
	1. Leer archivo
	2. Resolver Operaciones 
	3. Operar la matriz
	4. Mostrar usuarios
	5. Mostrar cola 
	6. Cerrar sesion""")
			opcionSistema = input()
			if opcionSistema == 1:
				self.leerArchivo(u,lista)
			if opcionSistema == 2:
				opArchivo.operando(u,lista)
			if opcionSistema == 4:
			 	print("-------usuarios-------")
			 	lista.recorrerUsuarios()
			 	
			if opcionSistema == 6:
				self.inicio()
				
				break
			
	def inicio(self):
		while True:
			print("")
			print("_____________________________________________________")
			print("Nombre: Jose Carlos Bautista Mazariegos")
			print("carnet : 201504231")
			print("")
			print("""
	Practica # 1
	1. Crear Usuario
	2. Ingresar al sistema
	3. Salir del programa
	""")

			opcion = input()
			if opcion == 1:
				self.crearUsr()
			
			if opcion == 2:
				self.login()
			if opcion ==3:
				sys.exit()
			
			#else:
			 #print("estupido idiota mi sintaxis hueco")


menu = practica_1()
menu.inicio()

