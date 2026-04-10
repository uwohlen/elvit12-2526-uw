import array
import csv
import matplotlib.pyplot as plt

filnavn = "googleplaystore.csv"

# legger hele datasettet inn i lista innhold for videre programmering
# og kolonnenavnene inn i lista overskrifter for å ta en kikk
innhold = []
with open(filnavn, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        if rad[1] == '1.9': # feil i datasettet, beskjed fra udir: kan fjernes
            #pass
            print(rad)
        else:
            innhold.append(rad)

#print(overskrifter)
#print(innhold)
#print(len(innhold))
"""
App, Category: tekst
Rating: desimaltall
Reviews: heltall
Size: heltall og bokstav (antall kB eller MB)
Installs: tekst som inneholder heltall og + (størrelsesorden)
Type: boolsk ("paid" eller "free")
Price: heltall
Content Rating, Genres: tekst
Last Updated: dato
Current Ver, Android Ver: tekst

['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']

10841 rader med data
Sletter: 
['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
*** Mangler kategori, alle data forskjøvet, (kategori 1.9 er egentlig en rating)

10840 rader med data som brukes videre

Eksempel på data (siste linje):
['iHoroscope - 2018 Daily Horoscope & Astrology', 'LIFESTYLE', '4.5', '398307', '19M', '10,000,000+', 'Free', '0', 'Everyone', 'Lifestyle', 'July 25, 2018', 'Varies with device', 'Varies with device']

App (0):
9656 unike verdier
1184 dubletter


Category (1): 33 unike verdier, ingen mangler verdi
['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FAMILY', 'FINANCE', 'FOOD_AND_DRINK', 'GAME', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'TOOLS', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'WEATHER']

Rating (2): 40 unike verdier, mange har verdien NaN (not a number), ellers er det tall fra 1.0 til 5.0
['1.0', '1.2', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0', 'NaN']
9366 verdier er ikke 'NaN'

Reviews (3): Heltall fra 0 til 78158306, ingen mangler verdi

Size (4): desimaltall eller heltall mellom 1 og 1020 + bokstaven M eller k, eller 'Varies with device'
9145 verdier er ikke 'Varies with device'

Installs (5): 21 unike verdier: NB! , som 1000-skillemerke
['0', '0+', '1+', '1,000+', '1,000,000+', '1,000,000,000+', '10+', '10,000+', '10,000,000+', '100+', '100,000+', '100,000,000+', '5+', '5,000+', '5,000,000+', '50+', '50,000+', '50,000,000+', '500+', '500,000+', '500,000,000+']
Bare en rad som ikke har + (er 0, kan slås sammen med 0+)
['Command & Conquer: Rivals', 'FAMILY', 'NaN', '0', 'Varies with device', '0', 'NaN', '0', 'Everyone 10+', 'Strategy', 'June 28, 2018', 'Varies with device', 'Varies with device']
Omkodet:
[0.0, 1.0, 5.0, 10.0, 50.0, 100.0, 500.0, 1000.0, 5000.0, 10000.0, 50000.0, 100000.0, 500000.0, 1000000.0, 5000000.0, 10000000.0, 50000000.0, 100000000.0, 500000000.0, 1000000000.0]
['', '+']

Type (6): 3 unike verdier: 
['Free', 'NaN', 'Paid']
Bare en rad som er NaN (har prisen 0, så kan gå til kategorien Free)
['Command & Conquer: Rivals', 'FAMILY', 'NaN', '0', 'Varies with device', '0', 'NaN', '0', 'Everyone 10+', 'Strategy', 'June 28, 2018', 'Varies with device', 'Varies with device']

Price (7): $ + desimaltall, eller 0, ingen mangler verdi
[0.0, 0.99, 1.0, 1.04, 1.2, 1.26, 1.29, 1.49, 1.5, 1.59, 1.61, 1.7, 1.75, 1.76, 1.96, 1.97, 1.99, 2.0, 2.49, 2.5, 2.56, 2.59, 2.6, 2.9, 2.95, 2.99, 3.02, 3.04, 3.08, 3.28, 3.49, 3.61, 3.88, 3.9, 3.95, 3.99, 4.29, 4.49, 4.59, 4.6, 4.77, 4.8, 4.84, 4.85, 4.99, 5.0, 5.49, 5.99, 6.49, 6.99, 7.49, 7.99, 8.49, 8.99, 9.0, 9.99, 10.0, 10.99, 11.99, 12.99, 13.99, 14.0, 14.99, 15.46, 15.99, 16.99, 17.99, 18.99, 19.4, 19.9, 19.99, 24.99, 25.99, 
28.99, 29.99, 30.99, 33.99, 37.99, 39.99, 46.99, 74.99, 79.99, 89.99, 109.99, 154.99, 200.0, 299.99, 379.99, 389.99, 394.99, 399.99, 400.0]       
['', '$']

Content rating (8): 
['Adults only 18+', 'Everyone', 'Everyone 10+', 'Mature 17+', 'Teen', 'Unrated']

Genres (9): 119 blandingsgrupper... er tekst men kan lage 3D-array, separert med ;
['Action', 'Action;Action & Adventure', 'Adventure', 'Adventure;Action & Adventure', 'Adventure;Brain Games', 'Adventure;Education', 'Arcade', 'Arcade;Action & Adventure', 'Arcade;Pretend Play', 'Art & Design', 'Art & Design;Action & Adventure', 'Art & Design;Creativity', 'Art & Design;Pretend Play', 'Auto & Vehicles', 'Beauty', 'Board', 'Board;Action & Adventure', 'Board;Brain Games', 'Board;Pretend Play', 'Books & Reference', 'Books & Reference;Creativity', 'Books & Reference;Education', 'Business', 'Card', 'Card;Action & Adventure', 'Card;Brain Games', 'Casino', 'Casual', 'Casual;Action & Adventure', 'Casual;Brain Games', 'Casual;Creativity', 'Casual;Education', 'Casual;Music & Video', 'Casual;Pretend Play', 'Comics', 'Comics;Creativity', 'Communication', 'Communication;Creativity', 'Dating', 'Education', 'Education;Action & Adventure', 'Education;Brain Games', 'Education;Creativity', 'Education;Education', 'Education;Music & Video', 'Education;Pretend Play', 'Educational', 'Educational;Action & Adventure', 'Educational;Brain Games', 'Educational;Creativity', 'Educational;Education', 'Educational;Pretend Play', 'Entertainment', 'Entertainment;Action & Adventure', 'Entertainment;Brain Games', 'Entertainment;Creativity', 'Entertainment;Education', 'Entertainment;Music & Video', 'Entertainment;Pretend Play', 'Events', 'Finance', 'Food & Drink', 'Health & Fitness', 'Health & Fitness;Action & Adventure', 'Health & Fitness;Education', 'House & Home', 'Libraries & Demo', 'Lifestyle', 'Lifestyle;Education', 'Lifestyle;Pretend Play', 'Maps & Navigation', 'Medical', 'Music', 'Music & Audio;Music & Video', 'Music;Music & Video', 'News & Magazines', 'Parenting', 'Parenting;Brain Games', 'Parenting;Education', 'Parenting;Music & Video', 'Personalization', 'Photography', 'Productivity', 'Puzzle', 'Puzzle;Action & Adventure', 'Puzzle;Brain Games', 'Puzzle;Creativity', 'Puzzle;Education', 'Racing', 'Racing;Action & Adventure', 'Racing;Pretend Play', 'Role Playing', 'Role Playing;Action & Adventure', 'Role Playing;Brain Games', 'Role Playing;Education', 'Role Playing;Pretend Play', 'Shopping', 'Simulation', 'Simulation;Action & Adventure', 'Simulation;Education', 'Simulation;Pretend Play', 'Social', 'Sports', 'Sports;Action & Adventure', 'Strategy', 'Strategy;Action & Adventure', 'Strategy;Creativity', 'Strategy;Education', 'Tools', 'Tools;Education', 'Travel & Local', 'Travel & Local;Action & Adventure', 'Trivia', 'Trivia;Education', 'Video Players & Editors', 'Video Players & Editors;Creativity', 'Video Players & Editors;Music & Video', 'Weather', 'Word']

Last updated (10): format "Month dd, yyyy" 

Current ver (11): kaosverdier

Android ver (12): 34 unike verdier
['1.0 and up', '1.5 and up', '1.6 and up', '2.0 and up', '2.0.1 and up', '2.1 and up', '2.2 - 7.1.1', '2.2 and up', '2.3 and up', '2.3.3 and up', '3.0 and up', '3.1 and up', '3.2 and up', '4.0 and up', '4.0.3 - 7.1.1', '4.0.3 and up', '4.1 - 7.1.1', '4.1 and up', '4.2 and up', '4.3 and up', '4.4 and up', '4.4W and up', '5.0 - 6.0', '5.0 - 7.1.1', '5.0 - 8.0', '5.0 and up', '5.1 and up', '6.0 and up', '7.0 - 7.1.1', '7.0 and up', '7.1 
and up', '8.0 and up', 'NaN', 'Varies with device']
To rader med NaN:
['[substratum] Vacuum: P', 'PERSONALIZATION', '4.4', '230', '11M', '1,000+', 'Paid', '$1.49', 'Everyone', 'Personalization', 'July 20, 2018', '4.4', 'NaN']
['Pi Dark [substratum]', 'PERSONALIZATION', '4.5', '189', '2.1M', '10,000+', 'Free', '0', 'Everyone', 'Personalization', 'March 27, 2018', '1.1', 'NaN']


Sjekk: om Type Free (6) korresponderer med Price 0 (7) og Paid m pris > 0
Sjekk: unike genre (9) - 3D-array, ";" mellom genres
Sjekk: at datoer er datoer
"""

def procfreq(array2D,i):
    temp_kol = []
    unik_kol = []
    dobl_kol = []
    for j in range(len(array2D)):
        if array2D[j][i] == 'Varies with device':
            #pass
            print(innhold[j])
        else:
            temp_kol.append(array2D[j][i])
            try:
                x = unik_kol.index(array2D[j][i])
            except:
                unik_kol.append(array2D[j][i])
            else:
                dobl_kol.append(array2D[j][i])
    print(len(temp_kol))
    print(len(unik_kol))
    print(len(dobl_kol))
    unik_kol.sort()
    dobl_kol.sort()
    print(unik_kol)
    #print(dobl_kol)

    #Indeks 4: size M, k
    """
    unik_tall = []
    unik_boks = []
    for verdi in unik_kol:
        if verdi != 'Varies with device':
            tall = float(verdi[0:len(verdi)-1])
            bokstav = verdi[len(verdi)-1:len(verdi)]
            try:
                x = unik_tall.index(tall)
            except:
                unik_tall.append(tall)
            try:
                x = unik_boks.index(bokstav)
            except:
                unik_boks.append(bokstav)
    unik_tall.sort()
    unik_boks.sort()
    print(unik_tall)
    print(unik_boks)
    """
    #Indeks 5: Installs +
    """
    unik_tall = []
    unik_boks = []
    for verdi in unik_kol:
        verdi2 = ""
        if verdi != '0':
            for b in verdi:
                if b != ",":
                    verdi2 = verdi2 + b
            tall = float(verdi2[0:len(verdi2)-1])
            bokstav = verdi2[len(verdi2)-1:len(verdi2)]
        else:
            tall = float(verdi)
            bokstav = ""
        try:
            x = unik_tall.index(tall)
        except:
            unik_tall.append(tall)
        try:
            x = unik_boks.index(bokstav)
        except:
            unik_boks.append(bokstav)
    
    unik_tall.sort()
    unik_boks.sort()
    print(unik_tall)
    print(unik_boks)
    """
    #Indeks 7: $ Price
    """
    unik_tall = []
    unik_boks = []
    for verdi in unik_kol:
        #verdi2 = ""
        if verdi != '0':
            #for b in verdi:
            #    if b != ",":
            #        verdi2 = verdi2 + b
            tall = float(verdi[1:len(verdi)])
            bokstav = verdi[0:1]
        else:
            tall = float(verdi)
            bokstav = ""
        try:
            x = unik_tall.index(tall)
        except:
            unik_tall.append(tall)
        try:
            x = unik_boks.index(bokstav)
        except:
            unik_boks.append(bokstav)
    
    unik_tall.sort()
    unik_boks.sort()
    print(unik_tall)
    print(unik_boks)
    """

#procfreq(innhold,12)

for rad in innhold:
    if rad[7][0:1] == "$" and rad[7][1:2] == "0" and rad[7][2:3] != ".":
        print(rad) #ingen
    elif rad[6] == "Free" and rad[7][0:1] == "$":
        print("Free koster") #ingen
    elif rad[6] == "Paid" and rad[7] == "0":
        print("Paid gratis") #ingen