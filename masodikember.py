sutik = ['csokis brownie', 'almás pite', 'mogyorós keksz', 'mézeskalács', 'kókuszos szelet', 'tejszínes pite', 'citromos muffin', 'vaníliás fánk', 'eperkrém torta', 'almás-fahéjas palacsinta', 'karamellás popcorn', 'mandulás torta', 'datolyás sütemény', 'túrófánk', 'meggyes pite', 'almás süti', 'puncsos torta', 'citromhabos sütemény', 'diós tekercs', 'narancsos piskóta']


hossz = 0
for item in sutik:
    if len(item) > hossz:
        hossz = len(item) 
        nev = item
print(nev)

sutik.sort()
print(*sutik, sep=" , ")


