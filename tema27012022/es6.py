def foo(c, f):
    words = f.read().split()
    n=0
    m=0
    for word in words:
        if(c.lower()==word[-1]):
            n=n+1
        if(c.upper()==word[0]):
            m=m+1
    print(n,m)

c= input("inserisci un carattere: ")
file = open("text.txt", "r")
foo(c, file)