import pygame
import random

# Farger som representerer tilstanden til en person
FARGER = {
  "frisk_uten_immunitet": (200, 200, 200), # Lys grå
  "smittet": (255, 182, 193),              # Rosa
  "syk": (255, 0, 0),                      # Rød
  "frisk_med_immunitet": (100, 100, 100),  # Mørk grå
  "død": (0, 0, 0),                        # Svart
}

# Konstanter (ting som ikke endres i programmet)
RUTE_STR = 15    # Størrelsen på hver "rute" i rutenettet
LINJEBREDDE = 1  # Tykkelse på linjer for å vise infeksjonstilstand
PRIKK_RADIUS = 2 # Radius på prikker for spesielle tilstander

class Person:
  """
  Denne klassen representerer en person i simuleringen.
  En person kan ha ulike statuser som frisk, smittet, syk, med immunitet eller død.
  """
  def __init__(self):
    self.status = "frisk_uten_immunitet"  # Alle starter som friske uten immunitet
    self.days_infected = 0  # Hvor lenge personen har vært smittet eller syk

  def bliSmittet(self):
    """
    Gjør personen smittet hvis den er frisk uten immunitet.
    """
    if self.status == "frisk_uten_immunitet":
      self.status = "smittet"
      self.days_infected = 0

  def oppdater(self):
    """
    Oppdaterer personens status basert på hvor lenge den har vært smittet eller syk.
    """
    if self.status == "smittet":
      self.days_infected += 1
      if self.days_infected >= 3:  # Etter 3 dager som smittet blir personen syk
        self.status = "syk"
        self.days_infected = 0
    elif self.status == "syk":
      self.days_infected += 1
      if random.random() < 0.01:  # 1% sjanse for å dø hver dag som syk
        self.status = "død"
      elif self.days_infected >= 4:  # Etter 4 dager blir personen frisk med immunitet
        self.status = "frisk_med_immunitet"

  def erSmittsom(self):
    """
    Sjekker om personen kan smitte andre (smittet eller syk).
    """
    return self.status in {"smittet", "syk"}

class Populasjon:
  """
  Denne klassen representerer hele rutenettet med personer.
  Den holder styr på alle personer og hvordan de påvirker hverandre.
  """
  def __init__(self, størrelse):
    """
    Lager en populasjon som er en kvadratisk grid med personer.
    Den midterste personen starter som syk, og naboene smittes.
    """
    self.størrelse = størrelse
    self.grid = []
    for i in range(størrelse):
      rad = []
      for j in range(størrelse):
        rad.append(Person())
      self.grid.append(rad)

    midten = størrelse // 2
    self.grid[midten][midten].status = "syk"  # Midten starter som syk

    # Smitt naboene til midten
    naboer = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in naboer:
      x, y = midten + dx, midten + dy
      self.grid[x][y].bliSmittet()

  def smitteNaboer(self, x, y):
    """
    Forsøker å smitte naboene til personen på posisjon (x, y).
    """
    naboer = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Opp, ned, venstre, høyre
    for dx, dy in naboer:
      nx, ny = x + dx, y + dy
      if 0 <= nx < self.størrelse and 0 <= ny < self.størrelse:  # Sjekk at vi er innenfor rutenettet
        nabo = self.grid[nx][ny]
        if nabo.status == "frisk_uten_immunitet" and random.random() < 0.3:  # 30% sjanse for smitte
          nabo.bliSmittet()

  def oppdater(self):
    """
    Oppdaterer hele rutenettet:
    1. Registrerer smittsomme personer.
    2. Oppdaterer status for alle personer.
    3. Smitter naboene til smittsomme personer.
    """
    smittsomme = []  # Liste over personer som kan smitte andre
    for x in range(self.størrelse):
      for y in range(self.størrelse):
        person = self.grid[x][y]
        if person.erSmittsom():
          smittsomme.append((x, y))
        person.oppdater()

    # Smitte naboene til alle smittsomme personer
    for x, y in smittsomme:
      self.smitteNaboer(x, y)

  def tegn(self, skjerm):
    """
    Tegner rutenettet på skjermen.
    Hver rute får en farge basert på status, og noen statuser får ekstra symboler.
    """
    for x in range(self.størrelse):
      for y in range(self.størrelse):
        person = self.grid[x][y]
        farge = FARGER[person.status]
        rect = pygame.Rect(x * RUTE_STR, y * RUTE_STR, RUTE_STR, RUTE_STR)

        # Tegn cellen med hvit ramme og farge inni
        pygame.draw.rect(skjerm, (255, 255, 255), rect, 1)  # Hvit ramme
        pygame.draw.rect(skjerm, farge, rect.inflate(-2, -2))

        # Tegn spesialelementer for enkelte statuser
        if person.status == "smittet":
          pygame.draw.line(
            skjerm,
            (0, 0, 0),  # Svart skråstrek
            rect.topleft,
            rect.bottomright,
            LINJEBREDDE,
          )
        elif person.status == "syk":
          pygame.draw.line(
            skjerm,
            (255, 255, 255),  # Hvit skråstrek
            rect.topright,
            rect.bottomleft,
            LINJEBREDDE,
          )
        elif person.status == "frisk_med_immunitet":
          pygame.draw.circle(
            skjerm,
            (0, 0, 0),  # Sort prikk
            rect.center,
            PRIKK_RADIUS,
          )
        elif person.status == "død":
          pygame.draw.circle(
            skjerm,
            (255, 255, 255),  # Hvit prikk
            rect.center,
            PRIKK_RADIUS,
          )

def simulerSmitte(størrelse=49, dager=50):
  """
  Starter simuleringen og viser hvordan smitten sprer seg dag for dag.
  """
  pygame.init()
  bredde, høyde = størrelse * RUTE_STR, størrelse * RUTE_STR
  skjerm = pygame.display.set_mode((bredde, høyde))
  pygame.display.set_caption("Simulering av smittespredning")
  klokke = pygame.time.Clock()

  populasjon = Populasjon(størrelse)

  dag = 0
  fortsett = True
  while fortsett and dag < dager:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        fortsett = False

    skjerm.fill((255, 255, 255))  # Hvit bakgrunn
    populasjon.tegn(skjerm)  # Tegn populasjonen
    pygame.display.flip()

    populasjon.oppdater()  # Oppdater tilstanden for hele populasjonen
    dag += 1
    klokke.tick(10)  # Vent 1 sekund mellom hver oppdatering

  pygame.quit()

# Start simuleringen
simulerSmitte(49, 200)