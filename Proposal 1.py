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
distances = ['d1','d2','d3','d4','d5','d6','ETA','gen_pos']

distances[0]=RD1;distances[1]=RD2;distances[2]=RD3;distances[3]=RD4
distances[4]=RD5;distances[4]=RD6
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
print(f'Aproximately: {APROX} Hours')
