import serial

#En caso de que seas usuario Linux cambia el COM3 por /dev/ttyACM0
arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)

while True:
    try:
        line = arduino.readline()
        print(line)
    except KeyboardInterrupt:
        print("Exiting")
        break
