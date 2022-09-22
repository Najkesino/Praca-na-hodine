
spokojny = [0] * 24
nespokojny = [0] * 24

subor = open('spokojny_1.txt', 'r')
for riadok in subor:
        riadok = riadok.strip()
        info = riadok.split()
        spokojnost = info[1]
        cas = info[0].split(':')
        hodina = int(cas[0])
        minuta = int(cas[1])
        if spokojnost == 'áno':
                spokojny[hodina] += 1
        else:
                nespokojny[hodina] += 1
pocet_spokojnych = sum(spokojny)
pocet_nespokojnych = sum(nespokojny)
spolu = pocet_spokojnych+pocet_nespokojnych
print('Vyjadrilo sa { } zákanzíkov.'.format(spolu))
pocet_ok = max(spokojny)
hodina = spokojny.index(pocet_ok)
print('Najviac spokojnych zákazníkov ({ }) je cey hodinu: { }'.format(pocet_ok, hodina))
nespokojny2 = []
for pocet in nespokojny:
        if pocet > 0:
                nespokojny2.append(pocet)
pocet_zle = min(nespokojny2)
hodina = nespokojny.index(pocet_zle)
print('Najmenej nespokojnych zákazníkov ({ }) je cez hodinu:{ }'.format(pocet_zle, hodina))

percenta_spkojnosti = [0] * 24
for i in range(24):
        pocet = spokojny[i]+nespokojny[i]
        if pocet > 0:
                percenta_spokojnosti[i] = spokojny[i]/pocet*100
for i in range(24):
        if percenta_spokojnosti[i] > 0:
                print('V { }. hodine je spokojných {:5.2f}%'.format(i, percenta_spokojnosti[i]))
