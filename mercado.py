import aiohttp

import requests
import aiohttp

# f auxiliares
async def get_data(link):  # no bloqueante
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            return await response.json()


def reduce_cifras(palabra):  # cuando se trata de billones, se utiliza 1.3b
    return round(int(palabra) / 1000000000, 2)


def separar_partes(item, n_partes):
    item_str = str(item)
    partes = [item_str[i:i+n_partes]
              for i in range(0, len(item_str), n_partes)]  # [123,342,532]
    return " ".join(partes)  # 123 342 532






async def get_item_price(ctx, *args):
    data_formato = "fivePercent"  # 95th.  podria ser avg, o wavg
    nombre_item = " ".join(args)

   # obtengo id del item a buscar en api de id
    async def obtener_id():
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.fuzzwork.co.uk/api/typeid.php?typename={nombre_item}") as response:
                return await response.json(content_type='text/html')  # custom

    data_item = await obtener_id()
    id_item = data_item.get("typeID")
    nombre_obtenido = data_item.get("typeName")

  
    # obtengo info del item
    data_mercado = await get_data(f"https://api.evemarketer.com/ec/marketstat/json?typeid={id_item}&usesystem=30000142")
    precio_compra_info = float(data_mercado[0].get("buy").get(data_formato))
    precio_venta_info = float(data_mercado[0].get("sell").get(data_formato))
    historia = await obtener_historia(ctx, id_item)

  # como el bot se comporta segun el resultado
    async def logica_respuesta():  # guardas, busco evitar if-elif hell, utilizo return para salir
        if (nombre_obtenido == "bad item"):
            return await ctx.send(f"item con nombre {nombre_item} no encontrado :(  ")

        if (precio_venta_info == 0):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.evemarketer.com/ec/marketstat/json?typeid={id_item}") as response:
                    dato_all = await response.json()  # custom
                    precio_venta_todas = reduce_cifras(dato_all[0].get("sell").get(data_formato))
                    precio_compra_todas = reduce_cifras(dato_all[0].get("buy").get(data_formato))
                    return await ctx.send(f"Precio todas las regiones de {nombre_item} {historia}\nPrecio venta: {precio_venta_todas} B \n Precio Compra {precio_compra_todas} B")
        if (precio_venta_info > 0):
          precio_venta_data = round((precio_venta_info / 1000000),2)
          precio_compra_data = round((precio_compra_info / 1000000),2)
        
          return await ctx.send(f"Precio de {nombre_obtenido}  {historia} \nPrecio venta: {precio_venta_data} Millones \nPrecio compra: {precio_compra_data} Millones")
 

    await logica_respuesta()





async def get_plex_price(ctx):#obtener precio de plex
    data_formato = "fivePercent"

    # es convencion que el precio sea 500 unidades de plex, en 1B. ej:1.3B
    def procesar_plex(numero):
        return (numero * 500) / 1000000000
    # obtengo objeto Response

    data = await get_data("https://api.evemarketer.com/ec/marketstat/json?typeid=44992&usesystem=30000142")
    lista_buy = data[0].get("buy")
    lista_sell = data[0].get("sell")

    # convencion es hablar de  1.3Billones
    precio_compra_avg = procesar_plex(lista_buy.get(data_formato))
    precio_venta_avg = procesar_plex(lista_sell.get(data_formato))

    #string, html
    mensaje_header = "Jita (4:4) -  x 500u "
    mensaje_plex_compra = f"\nPlex para la Compra: {precio_compra_avg:.2f} B"
    mensaje_plex_venta = f"\nPlex para la Venta:    {precio_venta_avg:.2f} B"
    await ctx.send(mensaje_header + mensaje_plex_venta + mensaje_plex_compra)


async def obtener_historia(ctx,id):
  TIEMPO_ULTIMA_MEDICION = 30
  def get_diferencia():
    diferencia = avg_hoy - avg_inicial
    porcentaje_diff = (diferencia * 100) / avg_inicial
    return porcentaje_diff

    
  def get_simbolo():
    if get_diferencia() > 0:
      return "+" 
    return ""

    
  def normalizar(numero):
    return float(numero,2)

 
  data = await get_data(f"https://esi.evetech.net/latest/markets/10000002/history/?datasource=tranquility&type_id={id}")
  avg_hoy = data[-1].get("average")
  fecha_hoy = data[-1].get("date")
   
  avg_inicial = data[-TIEMPO_ULTIMA_MEDICION].get("average") #15 dias atras
  fecha_inicial = data[-TIEMPO_ULTIMA_MEDICION].get("date")
  #frase = f"{avg_inicial}  {fecha_inicial}  \n  {avg_hoy}   {fecha_hoy} "

  frase = f"{get_simbolo()} {round(get_diferencia(),2)} %   |   Desde {fecha_inicial[5:]} al {fecha_hoy[5:]} "
  return frase
   
  