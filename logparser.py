import re


def get(data, r, mode):
    regex = re.compile(r)
    datalist = regex.findall(data)
    slist = []
    cdict = {}
    sorteddict = {}
    for i in datalist:
        if mode == 'p':
            slist.append(i.split(',')[1].split(':')[1].strip())
        if mode == 'a':
            slist.append(i.split('entered')[1].strip('.').strip())
        if mode == 'l':
            slist.append(i.split('now')[0].strip().strip(':').strip('is').strip())
        if mode == 'd':
            slist.append(i.split('has')[0].strip().strip(':').strip())
    for i in slist:
        try:
            cdict[i] += 1
        except KeyError:
            cdict[i] = 1
    it = sorted(cdict, key=cdict.__getitem__, reverse=True)
    for i in it:
        sorteddict[i] = cdict[i]
    return sorteddict


with open('Client.txt', encoding='utf8') as f:
    contents = f.read()
    passives = get(contents, r'Successfully allocated passive skill id: .+, name: .+', 'p')
    areas = get(contents, r' : You have entered .+.', 'a')
    levelups = get(contents, r' : .+ is now level .+', 'l')
    deaths = get(contents, r' : .+ has been slain.', 'd')
    print(passives)
    print(areas)
    print(levelups)
    print(deaths)

with open('clientstats.txt', 'w') as f:
    print('Passives:\n', file=f)
    for i in passives:
        print(i, passives[i], file=f)
    print(file=f)
    print('Areas:\n', file=f)
    for i in areas:
        print(i, areas[i], file=f)
    print(file=f)
    print('Level ups:\n', file=f)
    for i in levelups:
        print(i, levelups[i], file=f)
    print(file=f)
    print('Deaths:\n', file=f)
    for i in deaths:
        print(i, deaths[i], file=f)