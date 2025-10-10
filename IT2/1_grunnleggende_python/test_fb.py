def bytt(liste:list,indeks:int,fra_hva,til_hva) -> None:
  """
  Bytter ut en verdi i en todimensjonal tabell basert på indeks pr rad
  """
  for rad in liste:
    if rad[indeks] == fra_hva:
      rad[indeks] = til_hva


