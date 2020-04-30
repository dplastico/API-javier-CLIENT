#!/usr/bin/env python3
import requests
import json
import sys

#disable https warnings
requests.packages.urllib3.disable_warnings()

#request function
def get_sample(url, headers, data):
    try: #checks connection
        http = requests.post(url, headers=headers, data=json.dumps(data), verify=False) #post request
        return http.json()
    except:
        print("No connection to server... or API unavailable")
        sys.exit(1)

#downloader function
def download(download_url):
    downloader = requests.get(download_url,verify=False)
    fileName = input("[*] TYPE FILENAME (WITHOUT EXTENSION)\t>")
    fileName = fileName + ".pdf"
    try:
        f = open(fileName, 'wb')
        f.write(downloader.content)
        print(f"\n**** document {fileName} saved on current folder ****\n") #maybe I can add the option to specify the name, I dont know....
        f.close()
    except:
        print("Cannot write document to disk")
        sys.exit(1)

#choose flavour function
def choose_flavour():
    print("[*] SELECTING FLAVOUR")
    print("[*] Please select one of the following options by entering the corresponding number")
    print("[*] Enter Q to quit")
    print("\t[1] Salesforce")
    print("\t[2] GSuite")
    print("\t[3] Generic Storage")
    print("\t[4] Dropbox")
    print("\t[5] O365")

    option = ''
    keepAsking = True

    while keepAsking:
        userInput = input("[*] ENTER OPTION:")
        if userInput == "1":
            option = 'salesforce'
            keepAsking = False
        elif userInput == "2":
            option = 'salesforce'
            keepAsking = False
        elif userInput == "3":
            option = 'salesforce'
            keepAsking = False
        elif userInput == "4":
            option = 'salesforce'
            keepAsking = False
        elif userInput == "5":
            option = 'salesforce'
            keepAsking = False
        elif userInput.lower() == "q":
            print("[*] TERMINATING SCRIPT...")
            sys.exit(1)
        else:
            print("[!] INVALID INPUT")

    return option

#choose language function
def choose_language():
    print("[*] SELECTING LANGUAGE")
    print("[*] Please select one of the following options by entering the corresponding number")
    print("[*] Enter Q to quit")
    print("\t[1] English")
    print("\t[2] Spanish")

    option = ''
    keepAsking = True

    while keepAsking:
        userInput = input("[*] ENTER OPTION:")
        if userInput == "1":
            option = 'en'
            keepAsking = False
        elif userInput == "2":
            option = 'es'
            keepAsking = False
        elif userInput.lower() == "q":
            print("[*] TERMINATING SCRIPT...")
            sys.exit(1)
        else:
            print("[!] INVALID INPUT")

    return option

#choose password function
def choose_password():
    print("[*] SETTING UP PASSWORD")
    print("[*] Please select one of the following options by entering the corresponding number")
    print("[*] Enter Q to quit")
    print("\t[1] Set up password")
    print("\t[2] Do not set up password")

    option = ''
    keepAsking = True

    while keepAsking:
        userInput = input("[*] ENTER OPTION:")
        if userInput == "1":
            option = input("[*] PLEASE ENTER YOUR PASSWORD\n>")
            keepAsking = False
        elif userInput == "2":
            option = 'no'
            keepAsking = False
        elif userInput.lower() == "q":
            print("[*] TERMINATING SCRIPT...")
            sys.exit(1)
        else:
            print("[!] INVALID INPUT")

    return option

#choose phishing url function
def choose_phishingUrl():
    print("[*] SETTING UP PHISHING URL")
    print("[*] Please select one of the following options by entering the corresponding number")
    print("[*] Enter Q to quit")
    print("\t[1] Type phishing URL")
    print("\t[2] Use a random URL")

    option = ''
    keepAsking = True

    while keepAsking:
        userInput = input("[*] ENTER OPTION:")
        if userInput == "1":

            option = input("[*] PLEASE ENTER A PHISHING URL\n>")
            if option.startswith('http') == True:
                keepAsking = False
            else:
                print("[!] INVALID PHISHING URL")

        elif userInput == "2":
            option = 'random'
            keepAsking = False

        elif userInput.lower() == "q":
            print("[*] TERMINATING SCRIPT...")
            sys.exit(1)

        else:
            print("[!] INVALID INPUT")

    return option

if __name__ == '__main__':
    #Variables estaticas
    URL = "https://c9w9xreptl.execute-api.us-east-1.amazonaws.com/v2/createdocument"
    HEADERS = {'Content-Type': 'application/json'}
    TEMPLATE = 'qrcode_activelink'

    flavour = choose_flavour()
    language = choose_language()
    password = choose_password()
    phishing_url = choose_phishingUrl()

    data = {
    'flavour' : flavour,
    'language' : language,
    'password' : password,
    'phishing_url' : phishing_url,
    'template' :TEMPLATE
    }

    print("**** Sending data to API ****")
    response = get_sample(URL, HEADERS, data)

    print("*** Generating Report ****")
    download_url = response['download_url']

    print("**** You can access the sample malicious document on ****\n",download_url)
    save = input("\n[*] Press Y/y to download the file or any key to exit\n")
    if save == "Y":
        download(download_url)
    elif save == "y":
        download(download_url)
    else:
        print("closing...")
        sys.exit(1)
