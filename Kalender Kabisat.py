
# coding: utf-8

# In[3]:


kalender = [('Januari', range(1, 31+1)),
           ('Februari', range(1, 28+1)),
           ('Maret', range(1, 31+1)),
           ('April', range(1, 30+1)),
           ('Mei', range(1, 31+1)),
           ('Juni', range(1, 30+1)),
           ('Juli', range(1, 31+1)),
           ('Agustus', range(1, 31+1)),
           ('September', range(1, 30+1)),
           ('Oktober', range(1, 31+1)),
           ('November', range(1, 30+1)),
           ('Desember', range(1, 31+1))]

minggu = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def klndr(tahun, awal_hari):
    pos_awal = minggu.index(awal_hari)
    
    if kabisat(tahun):
        kalender[1] = ('Februari', range(1, 29+1))
        
    for bulan, days in kalender:
        print('{0} {1}'.format(bulan, tahun).center(20, ' '))
        print(''.join(['{0:<3}'.format(w) for w in minggu]))
        print('{0:<3}'.format('')*pos_awal, end='')
        
        for day in days:
            print('{0:<3}'.format(day), end='')
            pos_awal += 1
            if pos_awal == 7:
                print()
                pos_awal = 0
        print('\n')

tahun_kabisat=input('masukkan tahun = ')
tahun_kabisat=int(tahun_kabisat)
strtday = input('Masukan Hari (Mon, Tue, Wed, Thu, Fri, Sat, Sun) : ')
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
            

