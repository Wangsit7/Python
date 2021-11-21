# Eksekusi Program
# Mengimport module/library random

import random

# Mode Game Mudah
def modeMudah(data):

    # Jumlah Soal
    jumlahSoal = 0

    # Skor Sekarang
    currentSkor = 0

    # No Soal
    intSoal = 0

    for jumlahSoal in range(1,11):

        # Mencetak nomor soal
        currentSoal = 1
        intSoal = intSoal + currentSoal

        # Angka Random
        angka1 = random.randint(1,25)
        angka2 = random.randint(1,25)

        # Soal Mudah
        soal = angka1 + angka2
        # print(soal)
        print(intSoal,'Hasil Dari : ',angka1,'+',angka2)

        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban yang Benar
                jawabanBenar = 10

                currentSkor = currentSkor + jawabanBenar
                print('\nSkor Saya : ',currentSkor)
                print('---- Jawaban Anda Benar ----\n')
            
            elif int(answer) != soal:
                print('---- Jawaban Anda Salah ----\n')

            else:
                print('Jawaban Tidak Dikenali!')
        except Exception as err:
            print(err)
    
    # Total Jumlah Skor yang diperoleh ,
    # Kategori Tingkat Kemampuan dalam Mengerjakan Soal
    if currentSkor <= 45:
        print('Skor Anda :',currentSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu',data)
        print('Terima Kasih Sudah Bermain',data,'\n')
    elif currentSkor >= 50 and currentSkor <= 75:
        print('Skor Anda :',currentSkor)
        print('Kategori : B ==>  Tingkatkan Lagi Supaya Sempurna',data)
        print('Terima Kasih Telah Bermain',data,'\n')
    elif currentSkor >= 80:
        print('Skor Anda :',currentSkor)
        print('Kategori : A ==> ',data,'Pertahankan!')
        print('Terima Kasih Telah Bermain',data,'\n')


# Mode Game Sedang
def modeSedang(data):
    jumlahSoal = 0
    currentSkor = 0
    intSoal = 0

    for jumlahSoal in range (1,21):
        # Mencetak no soal
        currentSoal = 1
        intSoal = intSoal + currentSoal

        # Angka Random
        angka1 = random.randint(1,50)
        angka2 = random.randint(1,50)

        # operasi Matematika
        listMatematika = random.randint(1,2)

        if listMatematika == 1:
            soal = angka1 + angka2
            print(intSoal,'Hasil Dari : ', angka1,'+',angka2)
        
        elif listMatematika == 2:
            soal = angka1 - angka2
            print(intSoal,'Hasil Dari : ',angka1,'-',angka2)

        # Jawaban User
        answer = input('Answer : ')

        try:
            if int(answer) == soal:
                # Skor Jawaban Yang Benar
                jawabanBenar = 5

                currentSkor = currentSkor + jawabanBenar
                print('\nSkor Saya : ',currentSkor)
                print('---- Jawaban Anda Benar ----\n')

            elif int(answer) != soal:
                # Skor Jawaban Yang salah
                # Dikurangi
                jawabanSalah = 3

                currentSkor = currentSkor - jawabanSalah
                print('\nSkor Saya :',currentSkor)
                print('---- Jawaban Anda Salah ----\n')

            else:
                print('Jawaban Tidak Diketahui!')
        except Exception as err:
            print(err)

    # Total Jumlah Skor yang Diperoleh,
    # Kategori Tingkat Kemampuan dalam Mengerjakan Soal
    if currentSkor <= 45:
        print('Skor Anda :',currentSkor)
        print('Kategori : C ==> Tingkatkan Lagi Kemampuan Kamu!',data)
        print('Terima Kasih Telah Bermain',data,'\n')
    elif currentSkor >= 50 and currentSkor <= 75:
        print('Skor Anda :',currentSkor)
        print('Kategori : B ==> Bagus, Tingkatkan Lagi Supaya Sempurna',data)
        print('Terima Kasih Telah Bermain',data,'\n')
    elif currentSkor >= 80:
        print('Skor Anda :',currentSkor)
        print('Kategori : A ==>',data,'Pertahankan!')
        print('Terima Kasih Telah Bermain',data,'\n')


# Mode Game Sulit
def modeSulit(data):
        jumlahSoal = 0
        currentSkor = 0
        intSoal = 0

        for jumlahSoal in range(1,26):
            # Mencetak no soal
            currentSoal = 1
            intSoal = intSoal + currentSoal

            # Angka Random Utama untuk Penjumlahan, Pengurangan, Perkalian
            angka1 = random.randint(1,100)
            angka2 = random.randint(1,100)

            # Angka Random Tambahan untuk Operasi Campuran
            angka3 = random.randint(1,50)
            angka4 = random.randint(1,25)

            # Operasi Matematika
            listMatematika = random.randint(1,4)

            if listMatematika == 1:
                soal = (angka1 - angka3) * (angka4 + angka2)
                print(intSoal,'. Hasil Dari: ', '(', angka1 ,'-', angka3, ') *', angka4, '+',angka2)

            elif listMatematika == 2:
                soal = angka1 - angka2
                print(intSoal,'. Hasil Dari:', angka1 ,'-', angka2)

            elif listMatematika == 3:
                soal = angka1 * angka2
                print(intSoal,'. Hasil Dari: ', angka1 ,'*', angka2)

            elif listMatematika == 4:
                # Soal Operasi Matematika Campuran
                soal = angka4 * angka1 - ( angka2 + angka3 )
                print(intSoal,'. Hasil Dari: ', angka4, '*', angka1, '- (', angka2, '-', angka3, ')')

            # Jawaban User
            answer = input('Answer: ')

            try:
                if answer == soal:
                    # Skor Jawaban yang Benar
                    jawabanBenar = 4

                    currentSkor = currentSkor + jawabanBenar
                    print('\nSkor Saya: ', currentSkor)
                    print('---- Jawaban Anda Benar ----\n')

                elif answer != soal:
                    # Skor Jawaban yang Salah
                    # Dikurangi
                    jawabanSalah = 3

                    currentSkor = currentSkor - jawabanSalah
                    print('\nSkor Saya: ', currentSkor)
                    print('---- Jawaban Anda Salah ----\n')

                else:
                    print('Jawaban Tidak Dikenlai! \n')
            except Exception as err:
                print(err)

        # Total Jumlah Skor yang Diperoleh
        # Kategori Tingkat Kemampuan dalam Mengerjakan Soal
        if currentSkor <= 45:
            print('Skor Anda :', currentSkor)
            print('Katergori : C ==> Tingkatkan Lagi Kemampuan Kamu!', data)
            print('Terima Kasih Telah Bermain', data, '\n')
        elif currentSkor >= 50 and currentSkor <= 75:
            print('Skor Anda :', currentSkor)
            print('Katergori : B ==> Bagus, Tingkatkan Lagi Kemampuan Kamu!', data)
            print('Terima Kasih Telah Bermain', data, '\n')
        elif currentSkor >= 80:
            print('Skor Anda :', currentSkor)
            print('Katergori : A ==>',data, 'Pertahankan!')
            print('Terima Kasih Telah Bermain', data, '\n')