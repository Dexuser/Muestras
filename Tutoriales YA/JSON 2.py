# Con los datos que envia la pagina 
# https://jsonplaceholder.typicode.com/users
# recuperarlos y mostrarlos en la terminal
#[
#  {
#    "id": 1,
#    "name": "Leanne Graham",
#    "username": "Bret",
#    "email": "Sincere@april.biz",
#    "address": {
#      "street": "Kulas Light",
#      "suite": "Apt. 556",
#      "city": "Gwenborough",
#      "zipcode": "92998-3874",
#      "geo": {
#        "lat": "-37.3159",
#        "lng": "81.1496"
#      }
#    },
#    "phone": "1-770-736-8031 x56442",
#    "website": "hildegard.org",
#    "company": {
#      "name": "Romaguera-Crona",
#      "catchPhrase": "Multi-layered client-server neural-net",
#      "bs": "harness real-time e-markets"
#    }
#  },
#]

from urllib import request
import json

pagina = request.urlopen("https://jsonplaceholder.typicode.com/users")
informacion = pagina.read().decode("utf-8")
data = json.loads(informacion)

for dicc in data:
	print( f"id: { dicc['id'] }" )
	print( f"name: { dicc['name'] }" )
	print( f"username: { dicc['username'] }" )
	print( f"email: { dicc['email'] }" )
	print( f"street: { dicc['address']['street'] }" )
	print( f"suite: { dicc['address']['suite'] }" )
	print( f"city: { dicc['address']['city'] }" ) 
	print( f"zipcode: { dicc['address']['zipcode']}" )
	print( f"lat: { dicc['address']['geo']['lat'] }" )
	print( f"lng: { dicc['address']['geo']['lng'] }" )
	print( f"phone: { dicc['phone'] }" )
	print( f"website: { dicc['website'] }" )
	print( f"company: { dicc['company']['name'] }" )
	print( f"catchPhrase: { dicc['company']['catchPhrase'] }" )
	print( f"bs: { dicc['company']['bs'] }" )
	print("-" * 80)
