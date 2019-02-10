# Análisis de datos y un poco de IoT
## Data Analytics and a few of IoT

Repo del taller "Análisis de datos y un poco de IoT" para PyCon Colombia 2019.
Bienvenidos a este taller . Aqui encontrarán todo el material necesario para ir desarrollando las etapas de este workshop que preparamos para ustedes.

### Consideraciones
P
Para el desarrollo de este taller haremos uso de algunos programas,paquetes y librerías. Por favor descarga 

- ARDUINO IDE https://www.arduino.cc/en/main/software 

Para el caso de las librerías y paquetes crearemos una carpeta en nuestro Escritorio o en el home llamada **Taller** y allá configuraremos un entorno virtual. Para eso realiza los siguientes pasos :  

1. Ingresar al directorio que creamos desde la terminal 
`cd Taller`

2. Crearemos nuestro entorno virtual llamado myvenv
`python -m venv myvenv` Windows
`python3 -m venv myvenv` Linux - OS X

3. Activar el entorno virtual
`cd myvenv\Scripts\activate` Windows
`source myvenv/bin/activate` Linux - OS X

4. Regresar al directorio original Taller 
`cd ..`

5. Crear un archivo en el bloc de notas llamado "requirements.txt" y pegar el siguiente texto :
` Flask==1.0.2
pyserial==3.4
requests==2.21.0
matplotlib==3.0.2
numpy==1.16.1
scipy==1.2.0
pandas==0.24.1 `

6. Instalar los recursos necesarios en el entorno virtual con el comando 
`pip install -r requirements.txt `

7. Sigue con el resto del taller !
