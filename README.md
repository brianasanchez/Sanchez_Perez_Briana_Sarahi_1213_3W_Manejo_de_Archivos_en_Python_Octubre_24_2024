# Sanchez_Perez_Briana_Sarahi_1213_3W_Manejo_de_Archivos_en_Python_Octubre_24_2024
Prueba de envio de codigo y de screenshot

![image](https://github.com/user-attachments/assets/9573600c-cef1-485a-8fe8-9d1b0599f08e)

![image](https://github.com/user-attachments/assets/f68da076-3095-4f14-8d30-487e7c5ccd17)

![image](https://github.com/user-attachments/assets/1da7f80c-bd13-4654-bff4-f1583cccaacb)


DE LECTURA 
1
Abrir un archivo en el servidor
Supongamos que tenemos el siguiente archivo, ubicado en la misma carpeta que Python:

archivo de demostración.txt
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck

2
Para abrir el archivo, utilice la función incorporada open().
La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:
EjemploObtenga su propio servidor Python
f = open("demofile.txt", "r")
print(f.read())

3
Si el archivo se encuentra en una ubicación diferente, deberá especificar la ruta del archivo, de esta manera:
Ejemplo
Abrir un archivo en una ubicación diferente:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

4
Leer solo partes del archivo
De forma predeterminada, el read()método devuelve el texto completo, pero también puedes especificar cuántos caracteres quieres devolver:
Ejemplo
Devuelve los 5 primeros caracteres del archivo:
f = open("demofile.txt", "r")
print(f.read())

![image](https://github.com/user-attachments/assets/6b0b261e-90ab-4846-9e3b-7226d6c3228c)

![image](https://github.com/user-attachments/assets/7bf8b8f5-4d2f-4ba9-88ad-99f3777ec665)

![image](https://github.com/user-attachments/assets/e0d7194e-149e-445a-b7b0-cd157bd74234)



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

![image](https://github.com/user-attachments/assets/ab70d964-bc90-4772-a96f-ce8a4a7a8f89)

![image](https://github.com/user-attachments/assets/8091953c-df09-4785-8030-80c61db62f50)

![image](https://github.com/user-attachments/assets/7c317f39-e63c-452e-9396-9642530543b3)

6
Ejemplo
Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

![image](https://github.com/user-attachments/assets/34d82d07-d23b-4b7a-97a8-9d39cb6aaf7c)

![image](https://github.com/user-attachments/assets/9e3bb037-a913-49ca-a871-67453128407b)

![image](https://github.com/user-attachments/assets/ec6ab9fb-97d2-49ee-8d49-ee10ce8479a2)


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

![image](https://github.com/user-attachments/assets/1e19464f-bc1e-4642-a47d-19e4c3cdc80a)

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

![image](https://github.com/user-attachments/assets/f9d894a3-ade5-48ff-8d5d-aeef1d09d1fb)


![image](https://github.com/user-attachments/assets/cf332a83-3082-4fd8-a81a-23dd914c2473)


9
Eliminar carpeta
Para eliminar una carpeta entera, utilice el os.rmdir()método:
Ejemplo
Eliminar la carpeta "myfolder":
import os
os.rmdir("myfolder")

![image](https://github.com/user-attachments/assets/52311917-e568-4a89-bb72-7b0143840e11)

![image](https://github.com/user-attachments/assets/c8ce4553-0f45-4dbe-a6e2-af3252971a6a)

![image](https://github.com/user-attachments/assets/b947e322-947b-46f7-a15c-680d6915776a)

![image](https://github.com/user-attachments/assets/cc6b0eb3-c114-43ee-8166-44a7e20fc0a5)





