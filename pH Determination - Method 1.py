#pH Determination
#Method-1: if condition
pH_value=int(input('Enter the pH value: '))
if pH_value>0 and pH_value<7:
    print('Acid')
if pH_value>7 and pH_value<14:
    print('Base')
if pH_value==7:
    print('Neutral')
