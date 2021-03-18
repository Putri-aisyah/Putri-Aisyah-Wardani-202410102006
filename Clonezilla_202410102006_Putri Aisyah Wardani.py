print('Welcome to my ATM')
print('Pilih Option')
print('1. Check Uang')
print('2. Ambil Uang')
print('3. Menabung')
option = int(input('Silahkan pilih option: '))
if option == 1:
    print('Uang anda berjumlah Rp 200.000')
elif option == 2:
    print('Uang anda berjumlah RP 200.000. Berapa yang akan anda ambil? ')
    print('1. Rp 100.000')
    print('2. Rp 200.000')
    uang_anda = 200000
    opsi = int(input('Option: '))
    if opsi == 1:
        hasil = uang_anda-100000
        print('Uang anda tersisa: Rp ', hasil)
    elif opsi == 2:
        hasil2 = uang_anda-200000
        print('Uang anda tersisa: RP ', hasil2)
    else:
        print('Nominal yang anda masukkan salah!!!')
elif option == 3:
    uang_anda = 200000
    print('Uang anda berjumlah RP 200.000, Berapakah yang akan anda tabungkan?')
    opsi2 = int(input('Ketikkan nominal uang yang akan ditabung: Rp '))
    hasil3 = uang_anda + opsi2
    print('Jumlah uang anda sekarang adalah Rp ', hasil3)
else:
    print('Keyword yang anda masukkan salah, Mohon coba lagi!!!')