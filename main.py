"""
         ___     _,.---._    .-._        ,--.--------.                
  .-._ .'=.'\  ,-.' , -  `. /==/ \  .-._/==/,  -   , -\,--.-.  .-,--. 
 /==/ \|==|  |/==/_,  ,  - \|==|, \/ /, |==\.-.  - ,-./==/- / /=/_ /  
 |==|,|  / - |==|   .=.     |==|-  \|  | `--`\==\- \  \==\, \/=/. /   
 |==|  \/  , |==|_ : ;=:  - |==| ,  | -|      \==\_ \  \==\  \/ -/    
 |==|- ,   _ |==| , '='     |==| -   _ |      |==|- |   |==|  ,_/     
 |==| _ /\   |\==\ -    ,_ /|==|  /\ , |      |==|, |   \==\-, /      
 /==/  / / , / '.='. -   .' /==/, | |- |      /==/ -/  /==/._/       
 `--`./  `--`    `--`--''   `--`./  `--`      `--`--`  `--`-`        

       __.....__                         
   .-''         '.              .--./)   
  /     .-''"'-.  `.           /.''\\    
 /     /________\   \    __   | |  | |   
 |                  | .:--.'.  \`-' /    
 \    .-------------'/ |   \ | /("'`     
  \    '-.____...---.`" __ | | \ '---.   
   `.             .'  .'.''| |  /'""'.\  
     `''-...... -'   / /   | |_||     || 
                     \ \._,\ '/\'. __//  
                      `--'  `"  `'---'   
#############################################################################################
# This script is licensed under the Creative Commons Attribution 4.0 International License. #
# To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or      #
# send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.             #
#############################################################################################
"""

import requests
import os
import platform
import json
import time
import random
from art import *
from colorama import Fore, Style, init

start_time = time.time()
end_time = start_time + 3

init(autoreset=False)

print(Fore.GREEN)
while time.time() < end_time:
    char = random.choice(["1", "0"])
    print(char, end='')

montyText = "\n.------..------..------..------..------.\n"\
"|M.--. ||O.--. ||N.--. ||T.--. ||Y.--. |\n"\
"| (\/) || :/\: || :(): || :/\: || (\/) |\n"\
"| :\/: || :\/: || ()() || (__) || :\/: |\n"\
"| '--'M|| '--'O|| '--'N|| '--'T|| '--'Y|\n"\
"`------'`------'`------'`------'`------'\n"
print(montyText)
start_time = time.time()
end_time = start_time + 3

while time.time() < end_time:
    None

def returnConfig(key_to_check):
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
            if key_to_check in data:
                return data[key_to_check]
    except:
        print("Error occurred...")
        input()
        exit()

def changeConfig(key_to_change, new_value):
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
            if key_to_change in data:
                data[key_to_change] = new_value
                with open('config.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
    except:
        print("Error occurred...")
        input()
        exit()

def clear():
    system = platform.system()
    
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(color)

def getCountry():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        country = data.get('country')
        return country

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def cToF(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def mphToKph(mph):
    kph = mph * 1.60934
    return kph

def firstStart():
    clear()
    message = "###################################\n"\
    "# Welcome to Monty's Weather App. #\n"\
    "#   What color would you like?    #\n"\
    "###################################\n"\
    "# (1) White(Default) #\n"\
    "# (2) Green          #\n"\
    "# (3) Cyan           #\n"\
    "# (4) Purple         #\n"\
    "######################\n"
    print(message)
    resp = input("\n")
    if '2' in resp:
        changeConfig('color', 'Green')
    elif '3' in resp:
        changeConfig('color', 'Cyan')
    elif '4' in resp:
        changeConfig('color', 'Purple')
    else:
        changeConfig('color', 'White')
    getColor()
    clear()
    message = "########################################\n"\
    "# Would you like to use the metric(C°) #\n"\
    "# system or the imperial system(F°)?   #\n"\
    "########################################\n"\
    "# (1) Metric   #\n"\
    "# (2) Imperial #\n"\
    "################\n"
    print(message)
    resp = input('\n')
    if '1' in resp:
        changeConfig('units', 'Metric')
    else:
        changeConfig('units', 'Imperial')
    getUnit()
    clear()
    message = "##################################################\n"\
    "# Now enter a free API key from weatherstack.com #\n"\
    "#             (Right click to paste)             #\n"\
    "##################################################\n"
    print(message)
    resp = input('\n')
    request = requests.get(f'http://api.weatherstack.com/current?access_key={resp}&query=Greenville]').json()
    if 'success' in request:
        clear()
        print("Invalid API key try again later.\n\nPress enter to continue...\n")
        input()
        exit()
    else:
        changeConfig('apikey', resp)
        changeConfig('firstStart', 'False')
        clear()
        print("The weather app is all set up, you may now open it again after closing.\n\nPress enter to continue...\n")
        input()
        exit()

def getKey():
    global api_key
    api_key = returnConfig('apikey')

def getUnit():
    global imperial
    global unitSymbol
    unit = returnConfig('units')
    if unit == 'Imperial':
        imperial = True
        unitSymbol = 'F°'
    else:
        imperial = False
        unitSymbol = 'C°'

def getColor():
    global color
    color = returnConfig('color')
    if color == 'White':
        color = Fore.WHITE
    elif color == 'Green':
        color = Fore.GREEN
    elif color == 'Cyan':
        color = Fore.CYAN
    elif color == 'Purple':
        color = Fore.MAGENTA
    print(color)

def main():
    getColor()
    if returnConfig('firstStart') == 'True':
        firstStart()
    else:
        getKey()
        getUnit()
        getColor()
        
        while True:
            clear()
            header = "#######################\n"\
                     "# MONTY'S WEATHER APP #\n"\
                     "#######################\n\n"
            print(header)
            
            city = input("Enter a city (or type 'config' to change settings, or 'exit' to quit): ")
            
            if city.lower() == 'config':
                firstStart()
            elif city.lower() == 'exit':
                break
            else:
                request = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}]').json()
                
                if 'success' in request:
                    print("Invalid city, please try again.")
                else:
                    temp = request['current']['temperature']
                    feelslike = request['current']['feelslike']
                    windSpeed = request['current']['wind_speed']
                    humidity = request['current']['humidity']
                    weather = request['current']['weather_descriptions'][0]
                    
                    if imperial:
                        temp = cToF(temp)
                        feelslike = cToF(feelslike)
                    else:
                        windSpeed = mphToKph(windSpeed)
                    
                    bigAscii = city
                    bigAscii.replace(' ', '\n')
                    bigAscii = text2art(bigAscii)
                    clear()
                    print(bigAscii)
                    print("##############################\n")
                    if color == Fore.CYAN:
                        print(f"Weather: {Fore.GREEN}{weather}{color}\n")
                        print(f"Temperature: {Fore.GREEN}{temp} {unitSymbol}{color}\n")
                        print(f"Feels Like: {Fore.GREEN}{feelslike} {unitSymbol}{color}\n")
                        print(f"Humidity: {Fore.GREEN}{humidity}%{color}\n")
                    else:
                        print(f"Weather: {Fore.CYAN}{weather}{color}\n")
                        print(f"Temperature: {Fore.CYAN}{temp} {unitSymbol}{color}\n")
                        print(f"Feels Like: {Fore.CYAN}{feelslike} {unitSymbol}{color}\n")
                        print(f"Humidity: {Fore.CYAN}{humidity}%{color}\n")
                    
                    if imperial:
                        print(f"Wind Speed: {Fore.CYAN}{windSpeed} MPH{color}\n")
                    else:
                        print(f"Wind Speed: {Fore.CYAN}{windSpeed} KPH{color}\n")
                    
                    input("\nPress enter to continue...")

main()