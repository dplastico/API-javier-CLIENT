#!/usr/bin/env python
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
    try:
        f = open('sample_report.pdf', 'wb')
        f.write(downloader.content)
        print("\n**** document sample_report.pdf saved on current folder ****\n") #maybe I can add the option to specify the name, I dont know....
        f.close()
    except:
        print("Cannot write document to disk")
        sys.exit(1)
#static variables
url = "https://c9w9xreptl.execute-api.us-east-1.amazonaws.com/v2/createdocument"
headers = {'Content-Type': 'application/json'}
template = 'qrcode_activelink'
#user input variables (need to ad more error control, im a n00b in python so... I just "if" the shit out it)
#menu for user requests maybe I should add a While True to keep the menu but not sur if it would add something to the script
flavour = input("[*] Type a flavour: salesforce, gsuite, generic_storage, dropbox, onedrive, o365\n")
if flavour == 'salesforce':
    pass 
elif flavour == 'gsuite':
    pass
elif flavour == 'generic_storage':
    pass
elif flavour == 'dropbox':
    pass
elif flavour == 'o365':
    pass
elif flavour == 'O365':
    pass
else:
    print("[*] Type a valid option\n")
    print("closing...")
    sys.exit(1)
language = input("[*] Type a Language: en, es\n")
if language == 'en':
    pass 
elif language == 'es':
    pass
else:
    print("[*] Type a valid option en/es\n")
    print("closing...")
    sys.exit(1)
password = input("[*] Do you want to setup a password Y/N?\n")

if password == "n":
    password = 'no'
elif password == "N":
    password = 'no'
elif password == "Y":
    password = input("[*] Type your password\n")
elif password == "y":
    password = input("[*] Type your password\n")
else:
    print("Type a valid option Yy/Nn")
    print("closing...")
    sys.exit(1)
phishing_url = input("[*] Type a phishing URL or type random if you dont know one\n")
if phishing_url.startswith('http') == True:
    pass
elif phishing_url == 'random':
    pass
else:
    print("Type a valid optipn (URL, or random\n")
    print("closing....")
    sys.exit(1)
#data array
data = {
    'flavour' : flavour,
'language' : language,
'password' : password,
'phishing_url' : phishing_url,
'template' :template
}
print("**** Sending data to API to generate report.... *****")
response = get_sample(url, headers, data)
download_url = response['download_url']
print("**** You can access the sample malicious document on ****\n",download_url)
#!/usr/bin/env python
save = input("\n[*] Press Y/y to download the file or any key to exit\n")
if save == "Y":
    download(download_url)
elif save == "y":
    download(download_url)
else:
    print("closing...")
    sys.exit(1)



