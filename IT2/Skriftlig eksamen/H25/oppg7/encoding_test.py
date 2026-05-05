import chardet
 
def oppdagKoding(filRefferanse:str):
    """
    Funksjon for å oppdage koding i fil
    """
    with open(filRefferanse, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]
 
 
fil = "Elever-fag.csv"
# utf-8
# fil = "Elever-fag.json"
# ascii

koding = oppdagKoding(fil)
print(koding)
