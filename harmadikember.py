sutik = ['csokis brownie', 'almás pite', 'mogyorós keksz', 'mézeskalács', 'kókuszos szelet', 'tejszínes pite', 'citromos muffin', 'vaníliás fánk', 'eperkrém torta', 'almás-fahéjas palacsinta', 'karamellás popcorn', 'mandulás torta', 'datolyás sütemény', 'túrófánk', 'meggyes pite', 'almás süti', 'puncsos torta', 'citromhabos sütemény', 'diós tekercs', 'narancsos piskóta']



muffin = []
keres = "muffin"
for item in sutik:
    if keres in item:
        muffin.append(item)
print(*muffin)



keres = "mogyorókrémes linzer"
benne = True
for item in sutik:
    if item == keres:
        benne = True
if benne == True:
    print("Benne van")
else:
    print("Nincs benne")



