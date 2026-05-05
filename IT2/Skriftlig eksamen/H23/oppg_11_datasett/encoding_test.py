import chardet
 
def oppdagKoding(filRefferanse:str):
    """
    Funksjon for å oppdage koding i fil
    """
    with open(filRefferanse, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]
 
 
#fil = "Global YouTube Statistics.csv"
# ISO-8859-9
fil = "Global YouTube Statistics.json"
# utf-8

koding = oppdagKoding(fil)
print(koding)
