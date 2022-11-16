'''
DATE=16TH NOV 2022
DAY= WEDNESDAY
TOPIC= STRINGS
AUTHOR= POOJA
'''
k='global'
print(k.capitalize()) #Global 
print(k.casefold()) #global
print(k.center(50))                     #global
p=k.encode()
print(p) #b'global'
print(k.title()) #Global
print(k.istitle()) #false
print(k.endswith('')) #true
print(k.endswith(' ')) #false
print(k.endswith('l')) #true
print(k.startswith('')) #true
print(k.startswith(' ')) #false
print(k.startswith('g')) #true
print(k.isspace()) #false