import chardet
 
def oppdagKoding(filRefferanse:str):
    """
    Funksjon for å oppdage koding i fil
    """
    with open(filRefferanse, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]
 
 
#fil = "Datasett_fodselstall_komma.csv"
fil = "Datasett_fodselstall.json"
 
koding = oppdagKoding(fil)
print(koding)
#eksempel: utf-8