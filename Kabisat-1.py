tahun_kabisat=input('masukkan tahun = ')
tahun_kabisat=int(tahun_kabisat)
if tahun_kabisat%400==0:
    print (tahun_kabisat,"tahun kabisat")
else:
    if tahun_kabisat%100==0:
        print (tahun_kabisat,"bukan tahun kabisat")
    else:
        if tahun_kabisat%4==0:
            print (tahun_kabisat,"tahun kabisat")
        else:
            print (tahun_kabisat,"bukan tahun kabisat")
