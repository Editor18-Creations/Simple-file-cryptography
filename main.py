#imput
from cryptography.fernet import Fernet
import sys
import json
from pathlib import Path
######
#json
def json_f(data,extension):
    print("json_f")
    json_data = {
        "extension":extension,
        "data":data
    }
    name = input("name:")
    with open(name+".json",'w') as json_file:
        json.dump(json_data,json_file,indent=4)
    pass
#####
#cryptography
def encrypt_f(file,passworld):
    f = Fernet(passworld)
    with open(file,'rb') as arquivo:
        datos = arquivo.read()
    encrypt_data = f.encrypt(datos)
    extension = Path(arquive)
    extension = extension.suffix
    json_f(encrypt_data,extension)
    pass
#############
#input
arquive = input("arquive: ")
passworld = input("passworld: ")
option = int(input("""decrypt(0)
encrypt(1)
: """))
if not option:
    sys.exit()
    pass
if option == 1:
    encrypt_f(arquive,passworld)
######