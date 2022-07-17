n=int(input("inserisci un numero (0 per fermarti): "))
max=None

while n!=0:
    if not None or n>max:
        max=n 
    n=int(input("inserisci un numero (0 per fermarti): "))

print(max)