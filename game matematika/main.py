# Game System
import game

# Data Mode Awal Game
modeGame = 0

while modeGame != 9:

    # Data Nama Pemain
    print('Siapa Nama Anda?')
    playerName = input()

    print('Selamat Bermain !!'.center(80, '-'))
    print('-'.center(80, '-'))
    print('Silahkan Pilih Tingkat Kesulitan Permaninan ??')

    # Membuat List Mode Game
    print('1. Mudah')
    print('2. Sedang')
    print('3. Sulit \n')

    print('9. Keluar')
    print('\n')

    try:
        # User Memilih
        modeGame = int(input())

    except ValueError:
        print('Masukkan Angka Saja!!')
        print('Pilih Hanya Kategori Diatas Saja\n')

    if modeGame == 1:
        # User Meminta Mode Mudah
        game.modeMudah(playerName)

    elif modeGame == 2:
        # User Meminta Mode Sedang
        game.modeSedang(playerName)

    elif modeGame == 3:
        # USer Meminta Mode Sulit
        game.modeSulit(playerName)

print('Good Bye!!!')
print('Thanks For Playing, See you!!')
