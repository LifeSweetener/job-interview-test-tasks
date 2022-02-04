file = open(r"C:\Users\User_ll\Downloads\07.txt")
data = file.readlines()
file.close()

valve = ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]  # список всех возможных операций
vars = {'c': 0, 'b': 14146, 'd': 3536, 't': 0, 'e': 1768, 'v': 7073, 'f': 442, 'h': 168, 'g': 2042, 'i': -169, 'j': 1874, 'l': 1360, 'k': 4050, 'm': -1361, 'n': 2690,'p': 514, 'o': 16322, 'q': -515, 'r': 15808, 's': 0, 'u': 0, 'w': 0, 'x': 7073,'ao': 0, 'y': 1768, 'aq': 3536, 'z': 884, 'aa': 221, 'ab': 1021, 'ac': 84, 'ad': -85, 'ae': 937, 'ag': 680, 'af': 2025, 'ah': -681, 'ai': 1345, 'ak': 257, 'aj': 8161, 'al': -258, 'am': 7904, 'an': 0, 'ap': 0, 'ar': 0, 'as': 3536, 'av': 110, 'bj': 0, 'bl': 1768, 'au': 442, 'at': 884, 'aw': 510, 'ax': 42, 'ay': -43, 'az': 468, 'bb': 340, 'ba': 1012, 'bc': -341, 'bd': 672, 'bf': 128, 'bg': -129, 'be': 4080, 'bh': 3952, 'bi': 0, 'bm': 0, 'bn': 1768, 'bq': 55, 'bk': 0, 'bp': 221, 'cg': 884, 'bo': 442, 'ce': 0, 'bs': 21, 'bt': -22, 'br': 255, 'bu': 234, 'bw':170, 'bv': 506, 'bx': -171, 'by': 336, 'bz': 2040, 'ca': 64, 'cb': -65, 'cc': 1976, 'cd': 0, 'cf': 0, 'ch': 0, 'cz': 0, 'ci': 884, 'cj': 221, 'cl': 27, 'ck': 110, 'db': 442, 'cm': 127, 'cn': 10, 'co': -11, 'cp': 117, 'cr': 85, 'cq': 253, 'cs': -86, 'ct': 168, 'cu': 1020, 'cv': 32, 'cw': -33, 'cx': 988, 'cy': 0, 'dc': 0, 'da': 0, 'du': 0, 'dd': 442, 'de': 110, 'dw': 221, 'dg': 13, 'df': 55, 'dh': 63, 'di': 5, 'dj': -6, 'dk': 58, 'dm': 42, 'dn': -43, 'dl': 126, 'do': 84, 'dq':16, 'dp': 510, 'dr': -17, 'ds': 494, 'dt': 0, 'dv': 0, 'dx': 0, 'ep': 0, 'dy': 221, 'dz': 55, 'ea': 27, 'er': 110, 'eb': 6, 'ed': 2, 'ee': -3, 'ec': 31, 'ef': 29, 'eg': 63, 'eh': 21, 'ei': -22, 'ej': 42, 'ek': 255, 'el': 8, 'em': -9, 'en':247, 'eo': 1, 'es': 32768, 'et': 32878, 'fm': 16439, 'eq': 1, 'eu': 8219, 'ew':1027, 'ev': 4109, 'ex': 5135, 'fk': 2, 'ey': 1, 'ez': -2, 'fa': 5134, 'fc': 10,'fb': 13343, 'fd': -11, 'fe': 13333, 'fg': 4, 'ff': 46207, 'fh': -5, 'fi': 46203, 'fj': 1, 'fn': 32768, 'fl': 3, 'fo': 49207, 'fp': 12301, 'gf': 6, 'gh': 24603, 'fq': 6150, 'fr': 1537, 'fs': 7687, 'ft': 0, 'fu': -1, 'fv': 7687, 'fx': 4101,'fy': -4102, 'fw': 15887, 'fz': 11786, 'gb': 2, 'ga': 60991, 'gc': -3, 'gd': 60989, 'ge': 1, 'gi': 32768, 'gg': 7, 'gj': 57371, 'gk': 14342, 'ha': 14, 'gm': 1792, 'hc': 28685, 'gl': 7171, 'go': 1024, 'gn': 7939, 'gp': -1025, 'gq': 6915, 'gr': 15111, 'gs': 6146, 'gt': -6147, 'gu': 8965, 'gv': 58143, 'gw': 8193, 'gx': -8194, 'gy': 49950, 'gz': 0, 'hb': 14, 'hv': 28, 'hd': 0, 'he': 28685, 'hh': 3585, 'hf': 7171, 'hg': 3585, 'hj': 3585, 'hx': 14342, 'hi': 3585, 'hk': -3586, 'hl': 0, 'hn': 0, 'hm': 7171, 'ho': -1, 'hp': 7171, 'hq': 31759, 'hr': 4097, 'hs': -4098, 'ht': 27662, 'hu': 0, 'hy': 0, 'hz': 14342, 'ic': 448, 'ib': 1792, 'hw': 28, 'ie': 256, 'id': 1984, 'is': 7171, 'ia': 3585, 'iq': 56, 'if': -257, 'ig': 1728, 'ii': 1536, 'ih': 3777, 'ij': -1537, 'ik': 2241, 'im': 2048, 'il': 14535, 'in': -2049, 'io': 12487, 'ip': 1, 'it': 32768, 'ir': 57, 'jl': 114, 'iu': 39939, 'iv': 9984, 'jn': 19969, 'ix': 1248, 'iw': 4992, 'iy': 6112, 'iz': 128, 'ja': -129, 'jb': 5984, 'jd': 1792, 'jc': 14176, 'je': -1793, 'jf': 12384, 'jg': 48227, 'jh': 4096, 'ji': -4097, 'jj': 44131, 'jk': 1, 'jm': 115, 'kg': 230, 'jo': 32768, 'jp': 52737, 'jr': 6592, 'ki': 26368, 'js': 1648, 'jq': 13184, 'jt': 8176, 'ju': 64, 'jv': -65, 'jw': 8112, 'jy': 4992, 'jx': 16304, 'jz': -4993, 'ka': 11312, 'kb': 60977, 'kc': 3072, 'kd': -3073, 'ke': 57905, 'kf': 1, 'kj': 32768, 'kh': 231, 'lb': 462, 'kk': 59136, 'kn': 1848, 'ld': 29568, 'km': 7392, 'kl': 14784, 'ko': 8184, 'kp': 1056, 'kq': -1057, 'kr': 7128, 'kt': 6592, 'ks': 15320, 'ku': -6593, 'kv': 8728, 'kw': 59160, 'kx': 8704, 'ky': -8705, 'kz': 50456, 'la': 0, 'lc': 462, 'lw': 924, 'le': 0, 'lf': 29568, 'ly': 14784, 'lh': 3696, 'li': 924, 'lk': 528, 'll': -529, 'lg': 7392, 'lj': 4092, 'lm': 3564, 'ln': 7660, 'lo': 3296, 'lp': -3297, 'lq': 4364, 'lr': 29580, 'ls': 4352, 'lt': -4353, 'lu': 25228, 'lv': 0, 'lz': 0, 'ma': 14784, 'lx': 924, 'a': 924}  # словарь со всеми переменными и их текущими значениями
counter = 0
sos = True
while (sos):
    counter = 0
    sos = False
    for line in data:
        var1 = ""  # левый операнд
        var2 = ""  # правый операнд
        result = ""  # результат
        action = ""  # операция
        
        # Определение переменных выше: var1, var2, result и action:
        for operation in valve:
            op_index = line.find(operation)
            if (op_index != -1):
                if (operation != "NOT"):  #  в случае операций, кроме NOT...
                    var1 = line[:op_index-1]
                    var2 = line[ (op_index+len(operation)+1) : (line.find("->")-1) ]
                else:  #  в случае операции NOT...
                    var2 = line[ (op_index+len(operation)+1) : (line.find("->")-1) ]
                action = operation
        
        if (action == ""):  # присваивание CONST...
            var1 = line[:line.find("->")-1]
        
        result = line[line.find("->")+3:line.find('\n')]
        
        # Работа с хранилищем vars:
        if (action == "AND"):
            if (var1 in vars) and (var2 in vars):
                print("AND")
                vars[result] =  vars[var1] & vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("AND")
                vars[result] =  int(var1) & vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("AND")
                vars[result] =  vars[var1] & int(var2)
            else:
                sos = True
        elif (action == "OR"):
            if (var1 in vars) and (var2 in vars):
                print("OR")
                vars[result] =  vars[var1] | vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("OR")
                vars[result] =  int(var1) | vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("OR")
                vars[result] = vars[var1] | int(var2)
            else:
                sos = True
        elif (action == "NOT"):
            if (var2 in vars):
                print("NOT")
                vars[result] = ~vars[var2]
            elif (var2.isdigit()):
                print("NOT")
                vars[result] = ~int(var2)
            else:
                sos = True
        elif (action == "LSHIFT"):
            if (var1 in vars) and (var2 in vars):
                print("LSHIFT")
                vars[result] = vars[var1] << vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("LSHIFT")
                vars[result] = int(var1) << vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("LSHIFT")
                vars[result] = vars[var1] << int(var2)
            else:
                sos = True
        elif (action == "RSHIFT"):
            if (var1 in vars) and (var2 in vars):
                print("RSHIFT")
                vars[result] = vars[var1] >> vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("RSHIFT")
                vars[result] =int(var1) >> vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("RSHIFT")
                vars[result] = vars[var1] >> int(var2)
            else:
                sos = True
        elif (action == ""):  # присваивание CONST...
            if (var1.isdigit()):
                print("CONST")
                vars[result] = int(var1)
            elif (var1 in vars):
                print("CONST")
                vars[result] = vars[var1]
            else:
                sos = True

print(vars)
print("1) a = " + str(vars["a"]))
input()

value_a = vars["a"]  # сохранение значения "a"
vars.clear()

counter = 0
sos = True
while (sos):
    counter = 0
    sos = False
    for line in data:
        var1 = ""  # левый операнд
        var2 = ""  # правый операнд
        result = ""  # результат
        action = ""  # операция
        
        # Определение переменных выше: var1, var2, result и action:
        for operation in valve:
            op_index = line.find(operation)
            if (op_index != -1):
                if (operation != "NOT"):  #  в случае операций, кроме NOT...
                    var1 = line[:op_index-1]
                    var2 = line[ (op_index+len(operation)+1) : (line.find("->")-1) ]
                else:  #  в случае операции NOT...
                    var2 = line[ (op_index+len(operation)+1) : (line.find("->")-1) ]
                action = operation
        
        if (action == ""):  # присваивание CONST...
            var1 = line[:line.find("->")-1]
        
        result = line[line.find("->")+3:line.find('\n')]
        if result == 'b':
            vars[result] = value_a
            continue
        
        # Работа с хранилищем vars:
        if (action == "AND"):
            if (var1 in vars) and (var2 in vars):
                print("AND")
                vars[result] =  vars[var1] & vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("AND")
                vars[result] =  int(var1) & vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("AND")
                vars[result] =  vars[var1] & int(var2)
            else:
                sos = True
        elif (action == "OR"):
            if (var1 in vars) and (var2 in vars):
                print("OR")
                vars[result] =  vars[var1] | vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("OR")
                vars[result] =  int(var1) | vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("OR")
                vars[result] = vars[var1] | int(var2)
            else:
                sos = True
        elif (action == "NOT"):
            if (var2 in vars):
                print("NOT")
                vars[result] = ~vars[var2]
            elif (var2.isdigit()):
                print("NOT")
                vars[result] = ~int(var2)
            else:
                sos = True
        elif (action == "LSHIFT"):
            if (var1 in vars) and (var2 in vars):
                print("LSHIFT")
                vars[result] = vars[var1] << vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("LSHIFT")
                vars[result] = int(var1) << vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("LSHIFT")
                vars[result] = vars[var1] << int(var2)
            else:
                sos = True
        elif (action == "RSHIFT"):
            if (var1 in vars) and (var2 in vars):
                print("RSHIFT")
                vars[result] = vars[var1] >> vars[var2]
            elif (var1.isdigit()) and (var2 in vars):
                print("RSHIFT")
                vars[result] =int(var1) >> vars[var2]
            elif (var2.isdigit()) and (var1 in vars):
                print("RSHIFT")
                vars[result] = vars[var1] >> int(var2)
            else:
                sos = True
        elif (action == ""):  # присваивание CONST...
            if (var1.isdigit()):
                print("CONST")
                vars[result] = int(var1)
            elif (var1 in vars):
                print("CONST")
                vars[result] = vars[var1]
            else:
                sos = True
        print(str(vars))
        print(counter)
        print()

print("2) a = " + str(vars['a']))