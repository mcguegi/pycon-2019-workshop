import serial, requests, json,sys


URL_API = "http://localhost:12345/write_csv"
SERIAL_PORT = "COM3" #En caso de que seas usuario Linux cambia el COM3 por /dev/ttyACM0
#lee los datos del puerto serial
arduino_data = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=10.0)

while True:
    #lee las lineas de la salida del arduino
    arduino_scope = arduino_data.readline()
    leng = len(arduino_scope)
    decoded_bytes = float(arduino_scope[0:4].decode("utf-8"))
    data_to_request = {
        "temp": decoded_bytes
    }
    #Hace el request al api
    try:
        response = requests.post(
            URL_API, 
            json=data_to_request
        )
    except requests.exceptions.RequestException as error:  
        print(error)
        sys.exit(1) 