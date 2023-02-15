# Mensaje_del_tiempo
Envió Automático Mensaje del tiempo

![tiempo|50](./tiempo.png)

##DESCRIPCION
Proyecto donde usando las librerias de twilio, bs4, pandas y request principalmente vamos a realizar a coger datos de una API (en este caso del tiempo) y vamos a enviar un mensaje a nuestro movil
Este sistema se puede automatizar si instalamos el programa en un servidor en la nube o podemos programarlo en nuestro PC para que se ejecute al abrir

![python|50](./python.png)

##FICHEROS
El proyecto se compone de 3 ficheros aunque uno de ellos no se ha subido ya que es de claves:
1. twilio_config: donde iría toda la info sobre las claves de twilio y las de la API que vayamos a usar (este fichero no esta subido)
2. utils: donde tendremos todas las funciones que vamos a necesitar para sacar la info de la API, montarla en un DataFrame y enviarla por mensaje
3. twilio_script: el programa principal que va a ejecutar la acción
Los dos archivos subidos están comentados indicando que hace cada paso


![twilio|20](./twilio.png)

##TWILIO
Usaremos esta aplicación para el envío de mensajes. Esta plataforma nos provee de un número de movil para hacer los envios

