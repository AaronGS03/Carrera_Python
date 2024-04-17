#w=overwrite, r=read, a=append, w+=write+read, a+=append+read...
f=open("lecturaEscrituraFicheros/ejemplo1.txt","w")
f.write("Hey hey o/")
f.close()

#en una linea:
with open("lecturaEscrituraFicheros/ejemplo1.txt","r") as archivo:
    contenido=archivo.read()
print(contenido)