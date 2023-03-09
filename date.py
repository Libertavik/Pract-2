import calendar

year = int(input('Введите год: ')) 
calend = calendar.Calendar() #bibloteka
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #mesiaca
for i in range(1,12+1):#dchitaem god
    rezultat = calend.itermonthdays(year,i)#dni v mesiace
    rezultat=list(rezultat)
    try:
        while True:#Cicle
            rezultat.remove(0)#funkia vishe delaet minogo nulei ia ix ubrat ot greha
    except ValueError:#ashubka dabi nuli zaconchilis nasialnika
        pass#livaem iz cicla

    massive=[]#oppa masive "games" MEM

    for x in rezultat:#chitaem daty
        y=str(x)#priravnivaem v ctring znachenie
        if len(y)==2:
            z=list(str(x))
            massive.append(int(z[0]))#mnenie kajdogo chicla vajno dlia nas, KAJDOE CHISLO TEPER CIFRA
            massive.append(int(z[1]))
        else:#esli ne tak
            massive.append(x)#vstavliaem chislo prosto

    if i == 1:
        Jan = sum(massive)
    elif i == 2:
        Feb = sum(massive)
    elif i == 3:
        Mar = sum(massive)
    elif i == 4:
        Apr = sum(massive)
    elif i == 5:
        May = sum(massive)
    elif i == 6:
        Jun = sum(massive)
    elif i == 7:
        Jul = sum(massive)
    elif i == 8:
        Aug = sum(massive)
    elif i == 9:
        Sep = sum(massive)
    elif i == 10:
        Oct = sum(massive)
    elif i == 11:
        Nov = sum(massive)
    elif i == 12:
        Dec = sum(massive)
        #tyt chisto mesiaci raspisanai v dniax
print(Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec) #ny i otvet po zadaniy! ALE OP