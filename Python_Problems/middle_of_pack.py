
tourist=int(input())
jiangly=int(input())
beng=int(input())
lst=[tourist,jiangly,beng]
lst.sort()
if lst[1]==tourist:
    print("tourist")
elif lst[1]==jiangly:
    print("jiangly")
else:
    print("benq")
