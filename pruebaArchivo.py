from xml.dom import minidom
mixml="""<archivo>
	<matriz>
		<x>2</x>
		<y>3</y>
	</matriz>
	<operaciones>
		<operacion>
			2 8 + 4 * 7 -
		</operacion>
		<operacion>
			2 6 +
		</operacion>
		<operacion>
			2 6 -
		</operacion>
		<operacion>
			27 26 - 7 4 + *
		</operacion>
	</operaciones>
</archivo> """
 
xmldoc = minidom.parseString(mixml)
 
# obtenemos el atributo line de <message line="...">
print ("Atributo")
print ("----------------------")

print ("Contenido")
print ("----------------------")
itemlist = xmldoc.getElementsByTagName("x")
for i in itemlist:
    print (i.firstChild.nodeValue)
itemlist = xmldoc.getElementsByTagName("y")
for i in itemlist:
    print (i.firstChild.nodeValue)
itemlist = xmldoc.getElementsByTagName("operacion")
for i in itemlist:
    print (i.firstChild.nodeValue)