// SORTERING

// Sammenligningsfunksjon for sort()-metoden til arrays
// Virker for både tekst og tall
// Sorterer stigende (ascending)
function sammenlign(a,b) {
  if (a > b) {
    return 1;
  }
  else if (a < b) {
    return -1;
  }
  else {
    return 0;
  }
}

// Sammenligningsfunksjon for sort()-metoden til arrays
// Virker for både tekst og tall
// Sorterer synkende (descending)
function sammenlignD(a,b) {
  if (a > b) {
    return -1;
  }
  else if (a < b) {
    return 1;
  }
  else {
    return 0;
  }
}

// Sammenligningsfunksjon for sort()-metoden til 2D-arrays
// Virker for både tekst og tall
// Sorterer på kolonne med index 1
// Sorterer stigende (ascending)
function sammenlign1(a,b) {
  if (a[1] > b[1]) {
    return 1;
  }
  else if (a[1] < b[1]) {
    return -1;
  }
  else {
    return 0;
  }
}

// Sammenligningsfunksjon for sort()-metoden til 2D-arrays
// Virker for både tekst og tall
// Sorterer på kolonne med index 1
// Sorterer synkende (descending)
function sammenlign1D(a,b) {
  if (a[1] > b[1]) {
    return -1;
  }
  else if (a[1] < b[1]) {
    return 1;
  }
  else {
    return 0;
  }
}

// ARRAY-FUNKSJONER

/* 
ANTALL ELEMENTER
Går gjennom en array og teller opp hvor mange elementer vi har av en verdi 

Inn:
arrayInn - array i 1 dimensjon 
verdi - verdien du søker etter i arrayen

Ut:
return - antall av verdien du søker etter (tall)
*/
function antallElementer(arrayInn,verdi) {
  let antall = 0;
  for (let i=0; i< arrayInn.length; i++) {
    if (arrayInn[i] === verdi) {
      antall ++;
    }
  }
  return antall;
}