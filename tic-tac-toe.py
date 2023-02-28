import random
import subprocess
import os

# game variables

d = {11: "11", 12: "12", 13: "13",
     21: "21", 22: "22", 23: "23",
     31: "31", 32: "32", 33: "33"}
player_objects = ['x', 'o']
count = 0
winner = False
# game statics
all_spots = [i for i in range(34) if i in d.keys()]


# funcion to check game over
def check(filled_spots):
    filled_spots = set(filled_spots)
    if [11, 12, 13] == sorted(filled_spots.intersection({11, 12, 13})):
        if d[11] == 'x' and d[12] == 'x' and d[13] == 'x':
            return True
        elif d[11] == 'o' and d[12] == 'o' and d[13] == 'o':
            return True
    if [21, 22, 23] == sorted(filled_spots.intersection({21, 22, 23})):
        if d[21] == 'x' and d[22] == 'x' and d[23] == 'x':
            return True
        elif d[21] == 'o' and d[22] == 'o' and d[23] == 'o':
            return True
    if [31, 32, 33] == sorted(filled_spots.intersection({31, 32, 33})):
        if d[31] == 'x' and d[32] == 'x' and d[33] == 'x':
            return True
        elif d[31] == 'o' and d[32] == 'o' and d[33] == 'o':
            return True
    if [11, 21, 31] == sorted(filled_spots.intersection({11, 21, 31})):
        if d[11] == 'x' and d[21] == 'x' and d[31] == 'x':
            return True
        elif d[11] == 'o' and d[21] == 'o' and d[31] == 'o':
            return True
    if [12, 22, 32] == sorted(filled_spots.intersection({12, 22, 32})):
        if d[12] == 'x' and d[22] == 'x' and d[32] == 'x':
            return True
        elif d[12] == 'o' and d[22] == 'o' and d[32] == 'o':
            return True
    if [13, 23, 33] == sorted(filled_spots.intersection({13, 23, 33})):
        if d[13] == 'x' and d[23] == 'x' and d[33] == 'x':
            return True
        elif d[13] == 'o' and d[23] == 'o' and d[33] == 'o':
            return True
    if [13, 22, 31] == sorted(filled_spots.intersection({13, 22, 31})):
        if d[13] == 'x' and d[22] == 'x' and d[31] == 'x':
            return True
        elif d[13] == 'o' and d[22] == 'o' and d[31] == 'o':
            return True
    if [11, 22, 33] == sorted(filled_spots.intersection({11, 22, 33})):
        if d[11] == 'x' and d[22] == 'x' and d[33] == 'x':
            return True
        elif d[11] == 'o' and d[22] == 'o' and d[33] == 'o':
            return True
    return False


# clear screen
clear = open("clear.bat", 'w')
clear.write("cls")
clear.close()
# game loop
game_over = False
while not game_over:
    if count == 2:
        count = 0
    subprocess.run('clear.bat')
    print('\n', d[11], "|", d[12], "|", d[13], '\n',
          '------------', '\n',
          d[21], "|", d[22], "|", d[23], '\n',
          '------------', '\n',
          d[31], "|", d[32], "|", d[33])
    available_spots = [i for i in all_spots if d[i] == str(i)]
    print('available spots are: ', available_spots)
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input(f'choose a spot to place  "{player_objects[count]}": '))
            if user_input in available_spots:
                valid_input = True
            elif user_input in all_spots:
                print('spot occupied, please provide a valid spot from available spots')
            else:
                print('provide a spot which is available in available spots')
        except:
            print('enter a valid input')
    d[user_input] = player_objects[count]
    available_spots = [i for i in all_spots if d[i] == str(i)]
    filled_spots = [i for i in all_spots if i not in available_spots]
    if len(filled_spots) >= 5:
        game_over = check(filled_spots)
    if len(available_spots) == 0:
        if check(filled_spots):
            game_over = True
        else:
            print('its a tie')
            game_over = True
            os.remove("clear.bat")
    if game_over and check(filled_spots):
        print('\n', d[11], "|", d[12], "|", d[13], '\n',
              '------------', '\n',
              d[21], "|", d[22], "|", d[23], '\n',
              '------------', '\n',
              d[31], "|", d[32], "|", d[33])
        print(f'winner of the match is {player_objects[count]}')
        os.remove("clear.bat")
    count += 1
