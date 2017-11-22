#auteur: Sanne Schroduer
#Afvinkopdracht 1 - Exception Handling
#Datum: 21-11-2017


def main():

    bestand_check = False
    while bestand_check == False: 
        try:
            bestand, bestandsnaam = invoer_bestand()
            bestand_check = True 
            
        except FileNotFoundError:
            print("Het bestand kan niet gevonden worden")
            print("Voer een geldig bestand in en probeer het opnieuw")
            print("-" * 70)
         
     
    enzymen = open("enzymen.txt")
    headers, seqs = lees_inhoud(bestand)

    try:
        DNA_check = is_dna(seqs)
    except TypeError:
        print("Dit bestand bevat geen DNA sequenties.\nProbeer opnieuw.")
        print("-" * 70)
        
    
    try:
        knip_enzymen(DNA_check, seqs, headers, enzymen)
    
    except NameError:
        print("Dit zoekwoord komt niet voor in het bestand.")
    except ValueError:
        print("Geen enkel enzym knipt in deze een sequentie.")
        

    
def invoer_bestand():

    bestands_naam = input("Geef de bestandsnaam, in fasta format: " )
    bestand = open(bestands_naam)
    return bestand, bestands_naam

   
'''
lees_inhoud krijgt als parameter het bestand met sequenties mee
returnt een lijst genaamd headers met daarin alle headers uit het bestand (elke index bevat 1 header)
return een lijst genaamd seqs met daarin alle sequenties (elke index bevat 1 gehele sequentie)
'''

def lees_inhoud(bestand):
    headers = []
    seqs = []
    seq = "" 

    for line in bestand:
        line = line.strip()
        if ">" in line:
            headers.append(line)
            if len(seq) > 0:
                seqs.append(seq)
                seq = ""
        else:
            seq += line
        

    return headers, seqs

'''
is_dna krijgt als parameter het lijstje met sequenties mee
per sequentie wordt gekeken of de totale lengte gelijk is aan het aantal A+T+G+C
returnt True of False
'''

    
def is_dna(seqs):

    DNA_check = False
    for seq in seqs:
        A = seq.count("A")
        T = seq.count("T")
        C = seq.count("C")
        G = seq.count("G")
        N = seq.count("N")
        dna = A + T + C + G + N

        if dna == len(seq):
            DNA_check = True
        else:
            raise TypeError
        
    return DNA_check

'''
knip_enzymen krijgt als parameters mee:
de lijst met sequenties, de lijst met headers,
het textbestand waarin de knipenzymen in staan en de variabele zoekwoord.
'''

def knip_enzymen(DNA_check, seqs, headers, enzymen):
    woord = 0
    knipenzymen = 0
    
    enzymen_2d_lijst = []
    for line in enzymen:
        combi = line.strip().split(" ")
        combi[1] = combi[1].replace("^", "")
        enzymen_2d_lijst.append(combi)

   
    
    zoekwoord = input("Geef een zoekwoord op: ")

    for x in range(len(headers)):
        if zoekwoord in headers[x]:
            print(headers[x])
            woord += 1
            for combi in enzymen_2d_lijst:
                if combi[1] in seqs[x]:
                    knipenzymen += 1
                    print("Enzym", combi[0], "knipt in ", combi[1])

    
        
    # de variabele combi bevat 2 indexen, combi[0] is de naam van het enzym, combi[1] de knipsequentie
    # de 2d_lijst bevat per index 1 combi 
    
    if woord == 0:
        raise NameError
    if knipenzymen == 0:
        raise ValueError

    # voor elke index in de range van de lengte van de lijst met headers wordt gekeken of het zoekwoord voorkomt.
    # als het zoekwoord voorkomt in een header, wordt deze geprint.
    # voor elke combi in de 2d_lijst wordt gekeken of de knipsequentie voorkomt in een sequentie uit de lijst met sequenties
    # als dat zo is, wordt de naam van het enzym en de knipsequentie geprint
    
                    
main()

