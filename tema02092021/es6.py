def foo(c,f):
    list = []
    file = open(f,"r")
    words = file.read().split()
    file.close()

    for word in words:
        if word.count(c) >= 2:
            list.append(word)
    list.sort()
    return list

c = input("enter a charchter: ")
print(foo(c,'text.txt'))

