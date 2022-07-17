
c = input("enter a character: ")
c = c.upper()

while ord(c)<65 and ord(c)>69:
    c = input("enter a character: ")
    c = c.upper()

for c1 in range(ord("A"),ord(c)+1):
    for c2 in range(ord("A"),ord(c)+1):
        print(chr(c1)+chr(c2),end=" ")
