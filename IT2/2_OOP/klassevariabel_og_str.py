import dyreklasser as dk

mine_dyr = {
  "Heidi": dk.Hund("Heidi","Norsk buhund","Svart og hvit"),
  "Sniff": dk.Hund("Sniff","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Prikken": dk.Hund("Prikken","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Junior": dk.Hund("Junior","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Brumlemann": dk.Hund("Brumlemann","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Trulte": dk.Hund("Trulte","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Tott": dk.Hund("Tott","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Knoll": dk.Hund("Knoll","Blanding av buhund og elghund","Hvit med svarte og grå-brune flekker"),
  "Rita": dk.Hund("Rita","Schäferhund","Svart og brun"),
  "Silkesvarten": dk.Katt("Silkesvarten","Norsk skogkatt","Svart",liv=2),
  "Tigergutt": dk.Katt("Tigergutt","Norsk skogkatt","Stripete grå-svart",liv=1),
  "Lillesvarten": dk.Katt("Mini","Katt med ukjent far","Svart"), 
  "Kaisa": dk.Hund("Kaisa","Labrador retriever","Svart")
}

nabo_dyr = {
  "Festus": dk.Hund("Festus","Norsk elghund","Grå-brun")
}

for dyr in mine_dyr.values():
  print(dyr)

for dyr in nabo_dyr.values():
  print(dyr)

