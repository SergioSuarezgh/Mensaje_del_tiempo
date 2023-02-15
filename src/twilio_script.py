

import os
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime
from utils import request_wapi,get_forecast,create_df,send_message,get_date

####ARMANDO DE LA URL#####

query = 'Bogotá'    #Ponemos la ciudad a consultar
api_key = API_KEY_WAPI  #Ponemos la key de la API

input_date= get_date()  ##llamamos a la función que nos trae el día actual
response = request_wapi(api_key,query)  ##llamos a la función de conexión

datos = []

for i in tqdm(range(24),colour = 'green'):

    datos.append(get_forecast(response,i))  ##AÑADIMOS EN LA LISTA LOS DATOS QUE OBTENEMOS DE LA API


##CREAMOS EL DF CON LOS DATOS
df_rain = create_df(datos)


# ENVIAMOS MENSAJE POR TWILIO
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_rain,query)


print('Mensaje Enviado con exito ' + message_id)
