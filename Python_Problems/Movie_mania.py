year1, year2, year3, year4 = map(int,input().split())
if year1<year2 and year1<year3 and year1<year4:
    print("Spiderman")
elif year2<year1 and year2<year3 and year2<year4:
    print("Superman")
elif year3<year1 and year3<year2 and year3<year4:
    print("Batman")
elif year4<year1 and year4<year2 and year4<year3:
    print("Aquaman")
