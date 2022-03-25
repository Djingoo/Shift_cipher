####  V1  ####

# final =''
# with open('ch7.bin','rb') as f:
#     while True:
#         c = f.read(1)
#         if not c:
#             break
#         place = ord(c)
#         place += i (see below)
#         if place > 127:
#             place -= 128
#         c = chr(place)
#         final = final + c
# print("{}".format(final))

# i = 59 for e
# i = 27 for E 
    
####  V2  ####

i = 0

while i < 128:
    final =''
    with open('ch7.bin','rb') as f:
        while True:
            c = f.read(1)
            if not c:
                break
            place = ord(c)
            place += i 
            if place > 127:
                place -= 128
            c = chr(place)
            final = final + c
    print("[{}] : {}".format(i,final))
    i += 1
    