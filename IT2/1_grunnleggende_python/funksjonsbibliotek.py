def bytt(tabell:list,indeks:int,fra_verdi,til_verdi) -> list:
  """
    Går gjennom en todimensjonal liste, og bytter ut en verdi i hver rad basert på indeks og fra_verdi

    Inn: 
      tabell: list - en todimensjonal struktur av "rader" og "kolonner"
      indeks: int  - hvilken "kolonne" som skal sjekkes i hver "rad"
      fra_verdi    - hvilken verdi som skal byttes ut, kan være tekst, tall, ...
      til_verdi    - hvilken verdi det skal byttes til, kan være tekst, tall, ...

    Ut:
      returnerer en liste med samme struktur som originalen, men med enkelte verdier byttet ut
  """
  for rad in tabell:
    if rad[indeks] == fra_verdi:
      rad[indeks] = til_verdi
  return tabell