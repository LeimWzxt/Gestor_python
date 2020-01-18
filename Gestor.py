import shutil
import os

def Obtener_tipo_de_archivo(tipo,num_tipo,w):
    pal=[]
    pal=w.split(".")
    #Cuenta el numero de elementos de un tipo
    #contenidos en la carpeta
    m=True
    for i in range(len(tipo)):
        if (pal[-1]==tipo[i]):
            num_tipo[i] += 1
            m=False
    if(m):
        tipo.append(pal[-1])
        num_tipo.append(1)
        if((tipo[-1]=="BIN")|(tipo[-1]=="Msi")):
            tipo.remove(tipo[-1])
            del(num_tipo[-1])
        
###VER QUE SON ARCHIVOS TIPO BIN Y MSI
###Averiguar cómo ver las propiedades de los archivos00210
#Funcion para ver el contenido de una carpeta
#Funcion para ver el contenido de una carpeta
def Contenido_carpeta(carpeta, imprimir, folders_,num_folders, tipo, num_tipo): 
    #IMPRIMIR: False= no mostrar contenido, True: mostrar
    files_in_folder = os.listdir(fuente)
    for w in files_in_folder:

    	#¿w es una carpeta?
        m=True
        for i in range(len(w)):
            if(w[i]=="."):
                m=False
                break
        #Si w es una carpeta
        if(m):
            folders_.append(w)
            num_folders+=1
            if(folders_[-1]=="System Volume Information"):
                folders_.remove(folders_[-1])
                num_folders-=1
        #Si w no es una carpeta
        else:
        	Obtener_tipo_de_archivo(tipo,num_tipo,w)
    
    total_folders=0
    for i in range(len(num_tipo)):
        total_folders += num_tipo[i]
    total_folders += num_folders
    
    if(imprimir):
        print("Carpetas: ",end="")
        print(folders_);            
        print("Numero de carpetas: "+str(num_folders))
        for i in range(len(tipo)):
            print("Numero de archivos "+str(tipo[i])+": "+str(num_tipo[i]))
        #Menos 3 por BIN, MSI y el System Volume Information
        print("Total de archivos: "+str(total_folders))
        
#----------------------------------------
#Crear una nueva carpeta en una direccion
def Crear_folder(carpeta, nombre):
    
    files_in_folder_ = os.listdir(carpeta)
    #print(files_in_folder_,len(files_in_folder_))
    
    for w in files_in_folder_:
        m=True
        for w in files_in_folder_:
            if(nombre==w):
                m=False
            files_in_folder_ = os.listdir(carpeta)
        if(m):
            #carpeta_=carpeta+"\\"+nombre
            os.mkdir(carpeta+"\\"+nombre)
            print("Carpeta creada: "+nombre )
        return carpeta+"\\"+nombre


#mover un archivo a un destino segun su tipo
def Mover_archivos_a_folder(carpeta,tipo,folder):
	
	#w: jpg, png, ...
	#l: ars.jpg, asdasd.png, ...
    #count=0
    
    for w in tipo:
        files_in_folder_ = os.listdir(carpeta)
        for l in files_in_folder_:
            pal=[]
            pal=l.split(".")
            m=True
            if(pal[-1]==pal[0]):
                #count+=1
                m=False
            if((pal[-1]==w)and(m)):
                #shutil.copy(carpeta+"\\"+l,carpeta+"\\"+w)
                shutil.move(carpeta+"\\"+l,carpeta+"\\"+w)

# Ordena los archivos en una carpeta según su tipo
def Ordenar_segun_tipo(carpeta, tipo):
    num=0
    #print(files_in_folder)
    for w in tipo:
        #Crear carpeta
        folder=Crear_folder(carpeta, w)
    for w in tipo:
        #Mover
        Mover_archivos_a_folder(carpeta,tipo,folder)
        
        
    print("Archivos movidos")

fuente = r"D:\\png - copia - copia"
#Crear listas con tipos de archivos y sus cantidades
folders_=[]
num_folders=0
tipo = []
num_tipo = []

Contenido_carpeta(fuente,0, folders_, num_folders, tipo, num_tipo)
Ordenar_segun_tipo(fuente,tipo)