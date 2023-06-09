import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
   orig = input("Ingrese ciudad de origen: (o presione 'q' para salir): ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Ingrese ciudad de destino: (o presione 'q' para salir): ")
   if dest == "quit" or dest == "q":
        break
   key = "LPjVDchgTyc0FnsjpZFKkJXL7HYrecsY"
   url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
   json_data = requests.get(url).json()
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
      print("=============================================")
      print("Direccion desde " + (orig) + " to " + (dest))
      print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
      print("kilometros:           " + str("{: .2f}".format((json_data["route"]["distance"])*1.61 )))
      print("=============================================")
      for each in json_data["route"]["legs"][0]["maneuvers"]:
          print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
      print("=============================================\n")
