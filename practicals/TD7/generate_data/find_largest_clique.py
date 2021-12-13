import sys

def find_largest_clique(v, e):
    v = sorted(v, key= lambda x: len(e[x]))
    n = len(v)
    while len(e[v[0]]) != n-1:
        c = v[0]
        for x in e:
            e[x] = [y for y in e[x] if y != c]
        del e[c]
        v = v[1:]
        v = sorted(v, key= lambda x: len(e[x]))
        n = len(v)
        print("DEL", c)
    return v

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    d = {1: [2, 3],
        2: [3, 4],
        3: [4, 2],
        4: [2, 3],
        5: [1]
    }
    cl = find_largest_clique(l, d)
    print("TEST", cl)

    l = []
    d = {}
    with open(sys.argv[1]) as f:
        for line in f:
            fields = line.split()
            pdbi_ch1 = fields[0] + "_" + fields[1]
            pdbi_ch2 = fields[2] + "_" + fields[3]
            if pdbi_ch1 not in l:
                l.append(pdbi_ch1)
            if pdbi_ch2 not in l:
                l.append(pdbi_ch2)
            if pdbi_ch1 not in d:
                d[pdbi_ch1] = []
            if pdbi_ch2 not in d[pdbi_ch1]:
                d[pdbi_ch1].append(pdbi_ch2)
            if pdbi_ch2 not in d:
                d[pdbi_ch2] = []
            if pdbi_ch1 not in d[pdbi_ch2]:
                d[pdbi_ch2].append(pdbi_ch1)
    cl = find_largest_clique(l, d)
    print("SOLUTION", cl)
    with open("clique_rhodopsins_list.txt", 'w') as f:
        for i in cl:
            f.write(i+'\n')
