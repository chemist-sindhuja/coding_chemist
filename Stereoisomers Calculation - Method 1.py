#Stereoisomers Calculations
#Method-2:Functions
Chirality=int(input('Enter no. of Chiral Carbons: '))
def Stereoisomers():
    return(2**Chirality)
    print(f'Possible no.of Stereoisomers = {Stereoisomers}')
Stereoisomers(Chirality)