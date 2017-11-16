#auteur: Sanne Schroduer
#Afvinkopdracht 1 
#Datum: 16-11-2017


'''
onderstaande functie roept de andere functies aan(lees_inhoud, is_dna en knip_enzymen)
slaat de input van het zoekwoord op als variabele
'''

def main():

    bestand, bestands_naam = invoer_bestand()
    is_fasta(bestands_naam)
    enzymen = open("enzymen.txt")
    headers, seqs = lees_inhoud(bestand)
    is_DNA = is_dna(seqs)
    input_zoekwoord(seqs, headers, enzymen)
    zoekwoord = knip_enzymen(seqs, headers, enzymen)

def invoer_bestand():

    while True:
        try:
            bestands_naam = input("Geef de bestandsnaam, in fasta format: " )
            bestand = open(bestands_naam)
            return bestand, bestands_naam


        except FileNotFoundError:
            print("Het bestand kan niet gevonden worden")
            print("Voer een geldig bestand in en probeer het opnieuw")
            print("-" * 70)
            


def is_fasta(bestands_naam):

    fasta = False
    if bestands_naam.endswith(".fa") or bestands_naam.endswith(".fasta"):
        fasta = True
    else:
        print("Het bestand is geen fasta format.")
        bestand, bestands_naam = invoer_bestand()
            
            
    

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
    nuc = 'ATGCN'
    isDNA = True

    for x in seqs:
        if x not in nuc:
            isDNA = False
    
    return isDNA



def input_zoekwoord(seqs, headers, enzymen):

    try:
        zoekwoord = knip_enzymen(seqs, headers, enzymen)

            

    except ValueError:
        print("De invoer is geen tekst, probeer opnieuw.")
   

'''       
knip_enzymen krijgt als parameters mee:
de lijst met sequenties, de lijst met headers,
het textbestand waarin de knipenzymen in staan en de variabele zoekwoord.
'''

def knip_enzymen(seqs, headers, enzymen):
    enzymen_2d_lijst = []

    zoekwoord = str(input("Geef een zoekwoord op: "))
             

    for line in enzymen:
        combi = line.strip().split(" ")
        combi[1] = combi[1].replace("^", "")
        enzymen_2d_lijst.append(combi)
        
    # de variabele combi bevat 2 indexen, combi[0] is de naam van het enzym, combi[1] de knipsequentie
    # de 2d_lijst bevat per index 1 combi 

    for x in range(len(headers)):
        if zoekwoord in headers[x]:
            print(headers[x])
            for combi in enzymen_2d_lijst:
                if combi[1] in seqs[x]:
                    print("Enzym", combi[0], "knipt in ", combi[1])

    return zoekwoord             
    # voor elke index in de range van de lengte van de lijst met headers wordt gekeken of het zoekwoord voorkomt.
    # als het zoekwoord voorkomt in een header, wordt deze geprint.
    # voor elke combi in de 2d_lijst wordt gekeken of de knipsequentie voorkomt in een sequentie uit de lijst met sequenties
    # als dat zo is, wordt de naam van het enzym en de knipsequentie geprint
    
                    
main()

