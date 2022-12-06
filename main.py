import os
import time
from termcolor import colored
import requests
import sys


def main():
    def logo():
        print(colored(
            """
    @@@@@@@@@@@@@@@@@@@@@@@@@@**********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@*****************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@**************************************@@@@@@@@@@@@
    @@@@@@**************@@@@@@@@@@@@@@@@@@@@@@@**************@@@@@
    @@@***    *****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*****    ***@@
    @@***      **@@@@@@@@@@*****************@@@@@@@@@@**      **@@
    @@@****  ***@@@@@@***************************@@@@@@***  ***@@@
    @@@@@@@@@@@@*************@@@@@@@@@@@@@*************@@@@@@@@@@@
    @@@@@@@@@@***    ***@@@@@@@@@@@@@@@@@@@@@@@***    **@@@@@@@@@@
    @@@@@@@@@@@***  ***@@@@@@@***********@@@@@@@**   ***@@@@@@@@@@
    @@@@@@@@@@@@@@*@@@@@***********************@@@@*@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@**    *****@@@@@*****    **@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@***  ***@@@@@@@@@@@***  **@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@********@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    Created by Juan Romero
    dont use this for illegal purposes lmao 
    """, 'blue'))

    logo()

    time.sleep(1)

    print('1: Send sms')
    print('2: Exit')
    print('Only 1 messages per day')
    choice = input("\nChoose an option please: ")

    def SMS():
        os.system('clear')
        time.sleep(1)
        logo()
        time.sleep(1)
        smsnumb = input("Input the target number: ")
        message = input("Please input the message: ")
        url = "https://textbel.com/text"
        resp = requests.post(url, {
            'phone': f'{smsnumb}',
            'message': f'{message}',
            'key': 'textbelt',
        })

        print(resp)
        time.sleep(3)
        return main()

    if choice == '1':
        SMS()
    elif choice == '2':
        sys.exit()
    else:
        print('Invalid option')
        time.sleep(2)
        return main()
    
main()