from flask import Flask, request, jsonify, send_from_directory
import csv, json, os , sys

DOWNLOAD_DIRECTORY = os.getcwd()
FILE_PATH = os.getcwd() + "/data.csv"

app = Flask(__name__)

#Endpoint para escribir el archivo
@app.route('/write_csv', methods=['POST'])
def write_csv():
    #obteniendo los valores del request
    data_request = request.get_json()
    try:
        #Abre el archivo para sobrescribirlo
        with open(FILE_PATH,"a", newline='') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([data_request["temp"]])
        return "Escribiendo archivo"
    except Exception as e:
        print(e)
        return "Error en escritura"

#Endpoint para escribir el archivo
@app.route("/files/<path:path>")
def get_file(path):
    try:
        #Descarga el archivo
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except Exception as e:
        print(e)
        return 0
    

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) 
    except:
        port = 12345

    app.run(port=port, debug=True)