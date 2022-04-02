# BotAmigable
Bot de discord, hosteado en  https://repl.it/  .  
Uptimerobot.com lo mantiene activo mediante pings cada 5 minutos.

## Problemas a resolver

Tener que consultar detalles del valor de moneda virtual en juego implicaba interrumpir lo que uno estaba haciendo y abrir el juego. 
Se expandio para que busque todo los items del mercado, que extienda la busqueda a diferentes mercados, y que muestre si el item esta bajando o subiendo de precio desde un periodo, mostrado diferencia en % 


![image](https://user-images.githubusercontent.com/46230600/161393355-06334e6f-1863-4d28-a8f6-e902df43dc1e.png)


 
### Responder a ciertos comandos:

Se utiliza aiohttp para que peticiones sobre mercado a las api sean no-bloqueante

!plex  devuelve valor compra y venta de moneda virtual Plex, se utiliza api https://api.evemarketer.com/ec/  en formato JSON

!precio nombre_item devuelve precio item en mercado principal. Si no hay valor de venta alli, aumenta la busqueda a otros mercados. Se utiliza pattern de guardas para evitar una ensalada de if-elif. 

Se utiliza import para que la logica al consultar detalles de mercado no dificulten la lectura

!Ademas del precio, se agrego Tendencia, para conocer si subio o bajo el precio del item en los ultimos n dias. Se utiliza api con historial de mercado https://esi.evetech.net/ 
 

!help devuelve lista de comandos

### Responder a cierto mensaje, mediante listener de discord py, segun la Persona:

Me parecio buena idea utilizar clase Persona, con su nombre, sus posibles ID de discord, junto a las bromas con las que ya se familiariza.
ej: Si el autor.id coincide con persona.id, preguntar a la persona las bromas a las que es sujeto y elegir una random, o preguntar si esta de animo para bromas para no hacerlo enojar en primer lugar.

### Avisar de evento en diferentes dias y/o horarios, junto a cada cierto intervalo de tiempo. 
Utilizo libreria aiocron y task 
 
 
 

Basado en FreeCodeAcademy: https://www.youtube.com/watch?v=SPTfmiYiuok

