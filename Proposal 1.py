import random

'''
PLACES:
BDO, WESTERN UNION,ML KWARTA PADALA, GOLDEN BABOY, CARAMEL BAKESHOP, ALISONS TRADING
POSSIBLE ROUTES: 6
'''
RD1=random.randint(10,100);RD2=random.randint(10,100);RD3=random.randint(10,100)
RD4=random.randint(10,100);RD5=random.randint(10,100);RD6=random.randint(10,100)
#POSITIONAL LOCATION
Cur_Pos=random.randint(1,5)
'''
ASSIGNING RANDOM DISTANCES TO POSSIBLE ROUTES
'''
#1D ARRAY STORAGE, 'd stands for distance'
array_1d = ['distance1=0','distance2=0','distance3=0','distance1=4','distance5=0'
    ,'distance6=0','ETA','gen_cur_pos']

array_1d[0]=RD1;array_1d[1]=RD2;array_1d[2]=RD3;array_1d[3]=RD4
array_1d[4]=RD5;array_1d[5]=RD6
#TEST RANDOM DISTANCE
print(RD1,RD2,RD3,RD4,RD5,RD6)

'''#POSITIONING CURRENT LOCATION TO THE MAP
def random_pos(var):
    random.randint(1,5)
    if var == 1:
        print('map data need')
    elif var == 2:
        print('map data need')
    elif var == 3:
        print('map data need')
    elif var == 4:
        print('map data need')
    elif var == 5:
        print('map data need')'''

'''
DESTINATION SELECTION:
[1] BDO
[2] WESTERN UNION
[3] ML KWARTA PADALA
[4] GOLDEN BABOY
[5] CARAMEL BAKESHOP
'''
#SELECTION METHOD
'''def sel_des_loc(loc):
    print('NOTE: Integers only, if the inpute is not please restart the program...')
    if loc.isdigit() == False:
        print('Sorry, please run the program again and select Integer only')
    else:
        if loc == 1:
            print('map data needed')
        elif loc == 2:
            print('map data needed')
        elif loc == 3:
            print('map data needed')
        elif loc == 4:
            print('map data needed')
        elif loc == 5:
            print('map data needed')

d=input('Where do you want to go? e.g [1] for BDO')
sel_des_loc(d)'''

'''TIME OF ARRIVAL'''
MINS=RD1/.1
HRS=MINS/60
APROX = "{:.0f}".format(HRS)
array_1d[6]=APROX
print(f'Aproximately: {APROX} Hours \n1D Array: {array_1d}')

