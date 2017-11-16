#auteur: Sanne Schroduer
#Afvinkopdracht 1 - Versie 1


bestand = open("Alpaca.fa")
enzymen = open("enzymen.txt")

'''
onderstaande functie roept de andere functies aan(lees_inhoud, is_dna en knip_enzymen)
slaat de input van het zoekwoord op als variabele
'''

def main():
    headers, seqs = lees_inhoud(bestand)
    is_dna(seqs)
    zoekwoord = input("Geef een zoekwoord op: ")
    knip_enzymen(seqs, headers, enzymen, zoekwoord)


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

    for x in seqs:
        A = seqs.count("A")
        T = seqs.count("T")
        C = seqs.count("C")
        G = seqs.count("G")
        dna = A + T + C + G
        if dna == len(seqs):
            return True
        else:
            return False

'''       
knip_enzymen krijgt als parameters mee:
de lijst met sequenties, de lijst met headers,
het textbestand waarin de knipenzymen in staan en de variabele zoekwoord.
'''

def knip_enzymen(seqs, headers, enzymen, zoekwoord):
    enzymen_2d_lijst = []
    

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
                    
    # voor elke index in de range van de lengte van de lijst met headers wordt gekeken of het zoekwoord voorkomt.
    # als het zoekwoord voorkomt in een header, wordt deze geprint.
    # voor elke combi in de 2d_lijst wordt gekeken of de knipsequentie voorkomt in een sequentie uit de lijst met sequenties
    # als dat zo is, wordt de naam van het enzym en de knipsequentie geprint
    
                    
main()

