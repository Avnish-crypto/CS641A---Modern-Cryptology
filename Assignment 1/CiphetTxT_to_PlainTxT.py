from collections import defaultdict
d = defaultdict()
d['a'] = 's'
d['b'] = 'v'
d['d'] = 'q'
d['e'] = 'h'
d['f'] = 'p'
d['g'] = 'o'
d['h'] = 'n'
d['i'] = 'c'
d['j'] = 'm'
d['k'] = 'l'
d['m'] = 't'
d['n'] = 'u'
d['o'] = 'b'
d['p'] = 'a'
d['r'] = 'g'
d['s'] = 'r'
d['t'] = 'f'
d['u'] = 'd'
d['v'] = 'w'
d['w'] = 'i'
d['x'] = 'y'
d['y'] = 'e'

St = "Mewa wa mey twsam iepjoys gt mey ipbya . Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa 'mxSrN03uwdd' vwmegnm mey dngmya.".lower()
a = ""
for i in range(len(St)):
    if St[i] in d:
        a += d[St[i]] 
    else:
        a += St[i]