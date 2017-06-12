import lista_doblemente_Enlazada

class Principal():
	"""docstring for Principal"""
	global ingresoSistema
	global crearUsuario
	global salirSistema
	global guardarUsuario
	def __init__(self ):
		hola = 0

	def crearUsuario(self):

		print(""" Ingrese usuario y password """)
		u = raw_input()
		print(u)
		p = raw_input()
		print(p)
		


	def ingresoSistema(self):
		print(""" Ingrese su usuario y password """)
		usr = input()
		pas = input()
		

	def salirSistema(self):
		print("salir sistema")
		
	def menuPrincipal(self):
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
			self.crearUsuario()
		elif opcion == 2:
			self.ingresoSistema()
		elif opcion == 3:
			self.salirSistema()
		else: menuPrincipal()
		
	

	def guardarUsuario(self ,usuario , password):
		menuPrincipal()
	def menuSistema(self):
		print(""" Bienvenido al menu del sistema
	1. Leer archivo
	2.Resolver Operaciones 
	3. Operar la matriz
	4. Mostrar usuarios
	5. Mostrar cola 
	6. Cerrar sesion""")
		opcionSistema = input()
	

	def comprobarDatos(self):
		print("entro comprobar")
		menuSistema()

menu = Principal()
menu.menuPrincipal()
