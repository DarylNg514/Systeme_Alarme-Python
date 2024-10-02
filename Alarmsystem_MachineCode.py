from flask import Flask, request
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="alarmsystem"
)

if(mydb):
    print("Successfully Connected to Database")

mycursor = mydb.cursor()

# Endpoint pour recevoir les données des zones de la Raspberry Pi
@app.route('/receive_zones_data', methods=['POST'])
def receive_zones_data():
    # Récupérer les données des zones depuis la requête POST
    zones_data = request.json

    # Afficher les données des zones
    print("Données des zones reçues :")
    print("Zone1 :", zones_data["Zone1"])
    print("Zone2 :", zones_data["Zone2"])
    print("Zone3 :", zones_data["Zone3"])
    print("Zone4 :", zones_data["Zone4"])
    sql = "UPDATE zones SET Zone1=%s, Zone2=%s, Zone3=%s, Zone4=%s WHERE id=1"
    val = (zones_data["Zone1"],zones_data["Zone2"],zones_data["Zone3"],zones_data["Zone4"])
    mycursor.execute(sql,val)
    mydb.commit()
    print("Mise à jour réussie.")

    return "Données des zones reçues avec succès."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
