import hashlib

door_id = "fkylfhsq"

counter = 0
i = 10700000
pswd = ["9","b","e","0","b","5","f","7",]
while (counter != 0):
    i += 1
    print(i, end=":")
    print(counter)
    hash = hashlib.md5((door_id + str(i)).encode('UTF-8')).hexdigest()
    if (hash[0:5] == "00000"):
        digit = -1
        if (hash[5] == 'a'):
            digit = 10
        elif (hash[5] == 'b'):
            digit = 11
        elif (hash[5] == 'c'):
            digit = 12
        elif (hash[5] == 'd'):
            digit = 13
        elif (hash[5] == 'e'):
            digit = 14
        elif (hash[5] == 'f'):
            digit = 15
        else:
            digit = int(hash[5])
        
        if (digit <= 7) and (pswd[digit] == "_"):
            pswd[digit] = hash[6]
            counter += 1
            print("pswd = " + " ".join(pswd) + "\nindex = " + str(i))
            input()

print("".join(pswd))