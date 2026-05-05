import chardet
 
def oppdagKoding(filRefferanse:str):
    """
    Funksjon for å oppdage koding i fil
    """
    with open(filRefferanse, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]
 
 
fil = "05994_20240126-145813-csv.csv"
# Windows-1252
#fil = "05994_20240126-145813-json.json"
# cp1250

koding = oppdagKoding(fil)
print(koding)
