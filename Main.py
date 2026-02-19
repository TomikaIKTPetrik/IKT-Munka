sutik = ['csokis brownie', 'almás pite', 'mogyorós keksz', 'mézeskalács', 'kókuszos szelet', 'tejszínes pite', 'citromos muffin', 'vaníliás fánk', 'eperkrém torta', 'almás-fahéjas palacsinta', 'karamellás popcorn', 'mandulás torta', 'datolyás sütemény', 'túrófánk', 'meggyes pite', 'almás süti', 'puncsos torta', 'citromhabos sütemény', 'diós tekercs', 'narancsos piskóta']
def elso():
    print(len(sutik))
def masodik():
    keres = "csoki"
    darab = 0
    for item in sutik:
        if keres in item:
            darab += 1
    print(darab)
def harmadik():
    hossz = 0
    for item in sutik:
        if len(item) > hossz:
            hossz = len(item) 
            nev = item
    print(nev)
def negyedik():
    sutik.sort()
    print(*sutik, sep=" , ")
def otodik():
    muffin = []
    keres = "muffin"
    for item in sutik:
        if keres in item:
            muffin.append(item)
    print(*muffin)
def hatodik():
    keres = "mogyorókrémes linzer"
    benne = True
    for item in sutik:
        if item == keres:
            benne = True
    if benne == True:
        print("Benne van")
    else:
        print("Nincs benne")

def main():
    elso()
    masodik()
    harmadik()
    negyedik()
    otodik()
    hatodik()
main()