//Til å sortere tall i arrays
//Funksjonen settes inn i .sort()
//.sort(sortNumStigende)
function sortNumStigende(a,b) {
    return a - b
}

//Til å sortere tall i arrays
//Funksjonen settes inn i .sort()
//.sort(sortNumSynkende)
function sortNumSynkende(a,b) {
    return b - a
}

//Regner ut summen av tallverdiene i en array
//arrayen - inneholder tallverdier
function summer(arrayen) {
    var sum = 0
    for (var i=0; i<arrayen.length; i++) {
        sum += arrayen[i]
    }
    return sum
}

//Regner ut gjennomsnitt for tallverdiene i en array
//arrayen - inneholder tallverdier
//benytter funksjonen summer(arrayen) definert over
function gjennomsnitt(arrayen) {
    var snitt = summer(arrayen) / arrayen.length
    return snitt
}

/*  Sjekk om en verdi finnes i en array
    arrayen - en array med lik type verdier for alle elementer
    verdi - en verdi av samme type som verdiene i arrayen
    Funksjonen virker for både tall og tekst separat, men ikke en blanding
    Returnerer true hvis verdien er i arrayen, false hvis ikke
*/
function verdiFinnes(arrayen,verdi) {
    var finnes = false
    for (var i=0; i<arrayen.length; i++) {
        if (arrayen[i] === verdi) {
            finnes = true
        }
    }
    return finnes
}


/*  Sjekk om en verdi ikke finnes i en array
    arrayen - en array med lik type verdier for alle elementer
    verdi - en verdi av samme type som verdiene i arrayen
    Funksjonen virker for både tall og tekst separat, men ikke en blanding
    Returnerer true hvis verdien ikke er i arrayen, false hvis den er der
*/
function verdiFinnesIkke(arrayen,verdi) {
    var finnesIkke = true
    for (var i=0; i<arrayen.length; i++) {
        if (arrayen[i] === verdi) {
            finnesIkke = false
        }
    }
    return finnesIkke
}


/*  Lag en array med tilfeldige verdier, basert på en originalarray
    Man kan bruke hele eller deler av originalarrayen
    Verdier kan ikke brukes om igjen

    fraArray - originalarrayen
    hvorMange - hvor mange verdier skal plukkes fra originalarrayen

    fungerer for både tallverdier og tekstverdier i arrayene

    Eksempel på bruk:
    var minArray = plukktilfeldig(gammelArray,gammelArray.length)
    gir en omstokket kopi med alle verdiene

    Benytter funksjonen verdiFinnesIkke(arrayen,verdi) definert over
*/

function plukkTilfeldig(fraArray,hvorMange) {
    var nyArray = []
    for (var i=0; nyArray.length<hvorMange; i++) {
        var tilfeldig = Math.floor(Math.random()*fraArray.length)
        if (verdiFinnesIkke(nyArray,fraArray[tilfeldig])) {
            nyArray.push(fraArray[tilfeldig])
        }
    }
    return nyArray
}


/*  Lag en selvstendig kopi av en array, 
    slik at endringer på den nye arrayen ikke påvirker den gamle
*/
function kopiArray(originalArray) {
    var nyArray = []
    for (var i=0; i<originalArray.length; i++) {
        nyArray.push(originalArray[i])
    }
    return nyArray
}


/*  Summerer de siste verdiene i en array, fra og med angitt indeks i
    Returnerer summen
    arrayen - en array med tallverdier
    i - en indeks i den arrayen
*/
function sumfraindeks(arrayen,i) {
    var sum = 0
    for (var j = i; j<arrayen.length; j++) {
        sum += arrayen[j]
    }
    return sum
}


/*  Regn ut en potens ved å få oppgitt grunntall og eksponent
    Unødvendig funksjon siden vi kan skrive 3**4 eller bruke Math.pow(a,b), 
    men morsom øvelse. 
    Legg merke til at startverdien for potens er 1
    (Produkter har startverdi 1, summer har startverdi 0)
*/
function potens (grunntall,eksponent) {
    var potens = 1
    for (var i = 0; i<eksponent; i++) {
        potens *= grunntall;
    }
    return potens
}


/*  Finn minste verdi i arrayen
    Verdier sammenlignes direkte med <
    For riktig sammenligning av tall må verdiene i arrayen allerede være av typen number
    Legg merke til at forløkka går fra 1, ikke 0, siden 0 allerede er tatt ut som startverdi
*/
function finnMinst (arrayen) {
    var minst = arrayen[0]
    for (var i=1; i<arrayen.length; i++) {
        if (arrayen[i] < minst) {
            minst = arrayen[i]
        }
    }
    return minst
}


/*  Finn største verdi i arrayen
    Verdier sammenlignes direkte med >
    For riktig sammenligning av tall må verdiene i arrayen allerede være av typen number
    Legg merke til at forløkka går fra 1, ikke 0, siden 0 allerede er tatt ut som startverdi
*/
function finnStorst (arrayen) {
    var storst = arrayen[0]
    for (var i=1; i<arrayen.length; i++) {
        if (arrayen[i] > storst) {
            storst = arrayen[i]
        }
    }
    return storst
}

/*  Tilfeldig tall mellom (og inkudert) fraOgMed og tilOgMed
    fraOgMed er et heltall
    tilOgMed er et heltall
    Gir et tilfeldig heltall tilbake
*/
function tilfeldigMellom(fraOgMed,tilOgMed) {
    var antallVerdier = tilOgMed - fraOgMed + 1
    var tilfeldig = Math.floor(Math.random()*antallVerdier+fraOgMed)
    return tilfeldig
}

/* Funksjon for å tegne en stjerne
    ctx - canvas.getContext("2d")-variabel
    origox, origoy - posisjon av nedre venstre stjernespiss
    farge - stjernefarge
    faktor - relativ størrelse, tall mellom 0 og 1 (eller større...)
*/
function stjerne(ctx,origox,origoy,farge="white",faktor=1) {
    ctx.beginPath();
    ctx.fillStyle = farge;

    ctx.moveTo(origox,origoy);
    ctx.lineTo(origox+50*faktor,origoy-36*faktor);
    ctx.lineTo(origox+100*faktor,origoy);
    ctx.lineTo(origox+81*faktor,origoy-59*faktor);
    ctx.lineTo(origox+131*faktor,origoy-95*faktor);
    ctx.lineTo(origox+69*faktor,origoy-95*faktor);
    ctx.lineTo(origox+50*faktor,origoy-154*faktor);
    ctx.lineTo(origox+31*faktor,origoy-95*faktor);
    ctx.lineTo(origox-31*faktor,origoy-95*faktor);
    ctx.lineTo(origox+19*faktor,origoy-59*faktor);
    ctx.closePath();
    ctx.fill();		
}
