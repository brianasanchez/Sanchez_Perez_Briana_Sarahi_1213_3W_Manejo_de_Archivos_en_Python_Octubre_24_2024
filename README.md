# Sanchez_Perez_Briana_Sarahi_1213_3W_Manejo_de_Archivos_en_Python_Octubre_24_2024
Prueba de envio de codigo y de screenshot

![image](https://github.com/user-attachments/assets/c76f33bd-d123-4ebd-8dd9-0f8e8df544ec)
![image](https://github.com/user-attachments/assets/49180440-26e2-4da0-8665-5db90c04d183)
![image](https://github.com/user-attachments/assets/f9b64b33-7cfb-4dee-a637-3bb3643fa8dd)


DE LECTURA1
Abrir un archivo en el servidor
Supongamos que tenemos el siguiente archivo, ubicado en la misma carpeta que Python:

archivo de demostración.txt
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

![image](https://github.com/user-attachments/assets/d2acc089-8eba-4068-a39e-509c34c4f754)

2
Para abrir el archivo, utilice la función incorporada open().
La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:
EjemploObtenga su propio servidor Python
f = open("demofile.txt", "r")
print(f.read())

![image](https://github.com/user-attachments/assets/33e891a5-760d-4636-aab8-2e74be8f37d4)
![image](https://github.com/user-attachments/assets/cad9fa9e-03a5-4cfc-8052-3fa21b7efbe8)


ESCRITURA

5
Escritura de archivos en Python
❮ AnteriorPróximo ❯Escribir en un archivo existente
Para escribir en un archivo existente, debe agregar un parámetro a la open()función:
"a"- Anexar - se agregará al final del archivo
"w"- Escribir: sobrescribirá cualquier contenido existente

Ejemplo:
Abra el archivo "demofile2.txt" y agregue contenido al archivo:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

![image](https://github.com/user-attachments/assets/dfa755bf-e72f-42bd-907d-25ab03796058)
![image](https://github.com/user-attachments/assets/9bb1c895-509a-421e-a579-66967ee73a2a)
![image](https://github.com/user-attachments/assets/b19e9789-49bf-4eb4-91c2-58377982fb69)


6
Ejemplo
Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

![image](https://github.com/user-attachments/assets/b31dea16-61f2-488f-8087-020ae97ffd0e)
![image](https://github.com/user-attachments/assets/f2d88318-f974-4bad-9100-69741b43b0fe)
![image](https://github.com/user-attachments/assets/26f3c52c-55b0-4a71-b85b-ee1f3b848dda)


ELIMINAR ARCHIVO

7
liminar archivo de Python
❮ AnteriorPróximo ❯Eliminar un archivo
Para eliminar un archivo, debes importar el módulo del sistema operativo y ejecutar su os.remove()función:
Ejemplo
Eliminar el archivo "demofile.txt":
import os
os.remove("demofile.txt")

![image](https://github.com/user-attachments/assets/30d40be8-2c11-4109-8927-a8b32e14ef4d)
![image](https://github.com/user-attachments/assets/1fa5f4d1-cf62-41a0-a118-1bafc6bf416d)
![image](https://github.com/user-attachments/assets/221bdb8a-c4a0-43c9-b991-5601c0590062)
![image](https://github.com/user-attachments/assets/fcccba87-6376-49b4-adf1-3a05bf6a514b)


8
Comprobar si el archivo existe:
Para evitar obtener un error, es posible que desees verificar si el archivo existe antes de intentar eliminarlo:
Ejemplo
Comprueba si el archivo existe  elimínalo:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

![image](https://github.com/user-attachments/assets/cf0700cb-5c03-4420-b958-7080cfb9f56f)
![image](https://github.com/user-attachments/assets/cf332a83-3082-4fd8-a81a-23dd914c2473)


9
Eliminar carpeta
Para eliminar una carpeta entera, utilice el os.rmdir()método:
Ejemplo
Eliminar la carpeta "myfolder":
import os
os.rmdir("myfolder")

![image](https://github.com/user-attachments/assets/52311917-e568-4a89-bb72-7b0143840e11)
![image](https://github.com/user-attachments/assets/1d5f3d72-9056-44e1-b88f-2e80b5f1f928)
![image](https://github.com/user-attachments/assets/b947e322-947b-46f7-a15c-680d6915776a)
![image](https://github.com/user-attachments/assets/cc6b0eb3-c114-43ee-8166-44a7e20fc0a5)





