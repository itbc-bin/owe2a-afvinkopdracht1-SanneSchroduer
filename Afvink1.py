#auteur: Sanne Schroduer
#Afvinkopdracht 1 - Exception Handling
#Datum: 22-11-2017


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

    inhoud_check = False
    while inhoud_check == False:
        try:
            headers, seqs = lees_inhoud(bestand)
            inhoud_check = True
        except ValueError:
            print("Dit bestand bevat geen sequenties.")
            break
            
    while inhoud_check == True:

        try:
            is_dna = test_DNA(seqs)

            try:
                knip_enzymen(DNA_check, seqs, headers, enzymen)

            except NameError:
                print("Dit zoekwoord komt niet voor in het bestand.")
        except ValueError:
            print("Geen enkel enzym knipt in deze een sequentie.")
                
        except TypeError:
            print("Dit bestand bevat geen DNA sequenties.\nProbeer opnieuw.")
            print("-" * 70)
            

    
def invoer_bestand():

    bestands_naam = input("Geef de bestandsnaam, in fasta format: " )
    bestand = open(bestands_naam)
    return bestand, bestands_naam


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
    if len(seq) == 0:
        raise ValueError
    
    return headers, seqs

    
def test_DNA(seqs):

    is_dna = False
    for seq in seqs:
        A = seq.count("A")
        T = seq.count("T")
        C = seq.count("C")
        G = seq.count("G")
        N = seq.count("N")
        dna = A + T + C + G + N

        if dna == len(seq):
            is_dna = True
        else:
            raise TypeError
        
    return is_dna


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
    
    
    if woord == 0:
        raise NameError
    if knipenzymen == 0:
        raise ValueError

                    
main()

