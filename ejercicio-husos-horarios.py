''' Crear un programa que informe el horario en cualquier huso del mundo, hacerlo de la forma
más óptima posible, buscar las distintas posibilidades que hay '''

import pytz
from datetime import datetime
import re

def print_time(country):
    zonas = pytz.all_timezones

    patron = "/"
    contador = 0

    if re.search(patron,country):
        for letter in country:
            if letter == patron:
                contador = contador + 1

        if contador > 1:        
            for pais in zonas:
                if country == pais:
                    country_time_zone = pytz.timezone(country)
                    horario = datetime.now(country_time_zone)
                    prov = country.split("/")[2]
            
                    patron = "[_-]"
                    if re.search(patron, prov):

                        palabra = ""
                        for letra in prov:
                            if letra == "_" or letra == "-":
                                palabra += " "
                            else:
                                palabra += letra

                        pais = country.split("/")[1]
                        return horario.strftime(f"El horario en {pais}, {palabra} es %H:%M:%S en el día %D.")
                    else:
                        pais = country.split("/")[1]
                        prov = country.split("/")[2]
                        return horario.strftime(f"El horario en {pais}, {prov}, es  es %H:%M:%S en el día %D.")

        if contador == 1:
            for pais in zonas:
                if country == pais:
                    country_time_zone = pytz.timezone(country)
                    horario = datetime.now(country_time_zone)

                    pais = country.split("/")[0]
                    prov = country.split("/")[1]

                    patron = "[_-]"
                    if re.search(patron, prov):

                        palabra = ""
                        for letra in prov:
                            if letra == "_" or letra == "-":
                                palabra += " "
                            else:
                                palabra += letra    
                        return horario.strftime(f"El horario en {pais}, {palabra}, es %H:%M:%S en el día %D.")

                    else:
                        return horario.strftime(f"El horario en {pais}, {prov}, es %H:%M:%S en el día %D.")

    else:
        for pais in zonas:
                if country == pais:
                    country_time_zone = pytz.timezone(country)
                    horario = datetime.now(country_time_zone)
                    return horario.strftime(f"El horario en {country_time_zone} es %H:%M:%S en el día %D.")


print(print_time("America/Argentina/Cordoba"))
print(print_time("Africa/Kampala"))
print(print_time("America/Boa_Vista"))
print(print_time("Turkey"))