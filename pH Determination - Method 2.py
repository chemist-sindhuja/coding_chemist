pH_value=int(input())
if pH_value==7:
    msg='neutral'
if pH_value>7 and pH_value<=14:
    msg='basic'
if pH_value>0 and pH_value<7:
    msg='acidic'
def pH(pH_value, msg):
    print(f'The pH of the solution is {pH_value} and it is {msg} in nature')

pH(pH_value, msg)