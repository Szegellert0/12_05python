#Készitsen python kódot ami bekér egy egész hömérsékleti értéket
#és kiirja hogy az adott értéken milyen halmazállapotú a viz.

def homerseklet():
    homersekletC = int(input("Adja meg a hömérsékletet: "))
    
    if homersekletC <= 0:
        print("Szilárd Hállapot") #igaz ág
    elif homersekletC < 100:
        print("folyékony Hállapot")
    else:
        print("gáz Hállapot") #hamis ág

homerseklet()