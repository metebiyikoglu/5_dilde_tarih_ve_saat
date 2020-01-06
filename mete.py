from datetime import date
from datetime import datetime

print('Metenin bilgili makinesine hosgeldiniz!!!')
print('Oralet ister misiniz?')
print('Hangi dil? turkce icin 1\'e, ingilizce icin 2\'ye, havai icin 3\'e, almanca icin 4\'e, ispanyolca icin 5\'e basin.')
dil = input()

gun = ''
saat = ''

if(dil == '1'):
    print('Merhaba')
    gun = 'Bugunun tarihi '    
    saat = ', saat '
if(dil == '2'):
    print('Hello')
    gun = 'Today is '
    saat = ', time is '
if(dil == '3'):
    print('Aloha')
    gun = 'O keia la '
    saat = ', manawa '
if(dil == '4'):
    print('Hallo')
    gun = 'Heute ist '
    saat = ', die Zeit ist '
if(dil == '5'):
    print('Hola')
    gun = 'Hoy es '
    saat = ', el tiempo es '
    
today = date.today()
now = datetime.now().strftime("%H:%M:%S")

print(gun + str(today) + saat + str(now))
