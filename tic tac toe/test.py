import os
from time import sleep

baner='''
TABEL PENGISIAN
┏━━━━┳━━━━┳━━━━┓
┃ １ ┃ ２ ┃ ３ ┃
┣━━━━╋━━━━╋━━━━┃
┃ ４ ┃ ５ ┃ ６ ┃
┣━━━━╋━━━━╋━━━━┃
┃ ７ ┃ ８ ┃ ９ ┃
┗━━━━┻━━━━┻━━━━┛
'''
board = {
    '1': '  ', '2': '  ', '3': '  ',
    '4': '  ', '5': '  ', '6': '  ',
    '7': '  ', '8': '  ', '9': '  '
}

player = 1
total_moves = 0
end_check = 0

def check():
    if board['1'] == 'Ｘ' and board['2'] == 'Ｘ' and board['3'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['4'] == 'Ｘ' and board['5'] == 'Ｘ' and board['6'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['7'] == 'Ｘ' and board['8'] == 'Ｘ' and board['9'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['1'] == 'Ｘ' and board['4'] == 'Ｘ' and board['7'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['2'] == 'Ｘ' and board['5'] == 'Ｘ' and board['8'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['3'] == 'Ｘ' and board['6'] == 'Ｘ' and board['9'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['1'] == 'Ｘ' and board['5'] == 'Ｘ' and board['9'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1
    if board['3'] == 'Ｘ' and board['5'] == 'Ｘ' and board['7'] == 'Ｘ':
        print('PLAYER Ｘ WON !')
        return 1


    if board['1'] == 'Ｏ' and board['2'] == 'Ｏ' and board['3'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['4'] == 'Ｏ' and board['5'] == 'Ｏ' and board['6'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['7'] == 'Ｏ' and board['8'] == 'Ｏ' and board['9'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['1'] == 'Ｏ' and board['4'] == 'Ｏ' and board['7'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['2'] == 'Ｏ' and board['5'] == 'Ｏ' and board['8'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['1'] == 'Ｏ' and board['5'] == 'Ｏ' and board['9'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['3'] == 'Ｏ' and board['5'] == 'Ｏ' and board['7'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    if board['3'] == 'Ｏ' and board['6'] == 'Ｏ' and board['9'] == 'Ｏ':
        print('PLAYER Ｏ WON !')
        return 1
    return 0



os.system('clear')
print()
print(baner)
print()

while True:
    print()
    print('┏━━━━┳━━━━┳━━━━┓')
    print('┃ '+board['1']+' ┃ '+board['2']+' ┃ '+board['3']+' ┃')
    print('┣━━━━╋━━━━╋━━━━┃')
    print('┃ '+board['4']+' ┃ '+board['5']+' ┃ '+board['6']+' ┃')
    print('┣━━━━╋━━━━╋━━━━┃')
    print('┃ '+board['7']+' ┃ '+board['8']+' ┃ '+board['9']+' ┃')
    print('┗━━━━┻━━━━┻━━━━┛')
    print()
    end_check = check()
    if total_moves == 9 and end_check == 0:
        print('GAME OVER !')
    elif total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('PLAYER Ｘ: ')
            if p1_input.upper() in board and board[p1_input.upper()] == '  ':
                board[p1_input.upper()] = 'Ｘ'
                player = 2
                break
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('PLAYER Ｏ: ')
            if p2_input.upper() in board and board[p2_input.upper()] == '  ':
                board[p2_input.upper()] = 'Ｏ'
                player = 1
                break
            else:
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print()