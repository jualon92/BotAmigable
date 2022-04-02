# BotAmigable
Bot de discord, hosteado en  https://repl.it/  .  
Uptimerobot.com lo mantiene activo mediante pings cada 5 minutos.

## Como funciones que se buscaban lograr son:
### Responder a ciertos comandos:

Se utiliza aiohttp para que pedir detalles a la api sea no-bloqueante

!plex  devuelve valor compra y venta de moneda virtual Plex, se utiliza api https://api.evemarketer.com/ec/  en formato JSON

!precio nombre_item devuelve precio item en mercado principal. Si no hay valor de venta alli, aumenta la busqueda a otros mercados. Se utiliza pattern de guardas para evitar una ensalada de if-elif

!help devuelve lista de comandos

### Responder a cierto mensaje, mediante listener de discord py, segun la Persona:

Me parecio buena idea utilizar clase Persona, con su nombre, sus posibles ID de discord, junto a las bromas con las que ya se familiariza.
ej: Si el autor.id coincide con persona.id, preguntar a la persona las bromas a las que es sujeto y elegir una random, o preguntar si esta de animo para bromas para no hacerlo enojar en primer lugar.

### Avisar de evento en diferentes dias y/o horarios, junto a cada cierto intervalo de tiempo. 
Utilizo libreria aiocron y task 
 
 
 

Basado en FreeCodeAcademy: https://www.youtube.com/watch?v=SPTfmiYiuok

