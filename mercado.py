
import requests 
import json



def obtener_plex_precio():
  # obtengo objeto Response
   response_API = requests.get("https://api.evemarketer.com/ec/marketstat/json?typeid=44992&usesystem=30000142")  
   data = response_API.json() #
   lista_buy = data[0].get("buy")
   lista_sell = data[0].get("sell") 
  
   precio_compra_avg = (lista_buy.get("wavg") * 500) / 1000000000 # convencion es hablar de  1.3Billones 
   precio_venta_avg = lista_sell.get("wavg") * 500  / 1000000000
   mensaje_header =  "Jita (4:4) -  x 500u Promedio Semanal"
   mensaje_plex_compra =  f"\nPlex para la Compra: {precio_compra_avg:.2f} Millones"
   mensaje_plex_venta = f"\nPlex para la Venta:    {precio_venta_avg:.2f} Millones"
   return (mensaje_header + mensaje_plex_venta +  mensaje_plex_compra )

def obtener_item_precio(nombre_item):
  # obtengo id del item a buscar en api de id
    response_API = requests.get(
        f"https://www.fuzzwork.co.uk/api/typeid.php?typename={nombre_item}&format=json")
    data = response_API.json()
    id_item = data.get("typeID")
    nombre_obtenido = data.get("typeName")

    response_API_mercado = requests.get(
        f"https://api.evemarketer.com/ec/marketstat/json?typeid={id_item}&usesystem=30000142")
    data_mercado = response_API_mercado.json()
    precio_compra_avg = int(data_mercado[0].get("buy").get("avg"))
    precio_venta_avg = int(data_mercado[0].get("sell").get("avg"))

 #   compra_con_espacios =  separar_partes(precio_compra_avg,3) #podria utilizarse la funcion junto a string interp pero no me parece muy legible
     
    if (nombre_obtenido != "bad item"): #rever, podria utilizarse una funcion que
      return (f"Precio promedio x unidad de {nombre_obtenido}\nPrecio venta: {precio_venta_avg}  \nPrecio compra: { precio_compra_avg}")
    else:
      return  f"item con nombre {nombre_item} no encontrado :(  "
