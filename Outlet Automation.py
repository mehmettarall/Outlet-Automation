import random                 #Mehmet Aral Işık 19010011053

def girisKısmı():
    print("-------------------- SUBAYEVLERİ CREW --------------------")
    print("-------- PERAKENDE SATIŞ MAĞAZASI OTOMASYONU --------")
    print("1) Ürün Ekleme")
    print("2) Ürün Silme")
    print("3) Ürün Güncelleme")
    print("4) Ürün Arama")
    print("5) Ürün Listeleme")
    print("6) Ürün Monteleme İçin Ücret Hesaplama ve Randevu Alma")
    print("7) İl Dışı Gönderim Fiyatı ve  Randevu Alma")
    print("8) Hazır Monteli Getirim İçin Ücret Hesaplama ve Randevu Alma")
    print("9) Çıkış")
    secim = int(input("Seçiminiz:"))
    return secim

def altEkran():
    print("1) Beyaz Eşya Kategorisi")
    print("2) Mobilya Kategorisi")
    print("3) Ana Menü")
    print("4) Çıkış")
    secim = int(input("Seçiminiz:"))
    return secim


def whiteEsya():        #Dosyaya beyaz eşya kısmını ekleme
    beyaz = {}
    ürünNo = random.randint(100, 999)
    beyaz["Ürün Numarası"] = ürünNo
    ürünName = input("Ürünün İsmi:")
    beyaz["Ürünün İsmi"]= ürünName
    kütle = int(input("Ürünün Ortalama Ağırlığı(Gram):"))
    beyaz["Ürünün Ortalama Ağrılığı"]=kütle
    renk = input("Ürünün Rengi:")
    beyaz["Ürünün Rengi"] = renk
    üretimYılı = input("Ürünün Üretim Yılı:")
    beyaz["Ürünün Üretim Yılı"] = üretimYılı
    papel = input("Ürünün Ücreti:")
    beyaz["Ürünün Ücreti"] = papel
    byz=open("beyazEşya.txt","a")
    byz.write(str(beyaz)+"\n")
    byz.close()
    print("Ürün Kaydı Başarılı!!")


def Mibolyu():          #Dosyaya mobilya kısmını ekleme
    mobilya = {}
    ürünNo = random.randint(1000, 9999)
    mobilya["Ürün Numarası"] = ürünNo
    ürünName = input("Ürünün İsmi:")
    mobilya["Ürünün İsmi"]= ürünName
    kütle = int(input("Ürünün Ortalama Ağırlığı(Gram):"))
    mobilya["Ürünün Ortalama Ağrılığı"]=kütle
    renk = input("Ürünün Rengi:")
    mobilya["Ürünün Rengi"] = renk
    üretimYılı = input("Ürünün Üretim Yılı:")
    mobilya["Ürünün Üretim Yılı"] = üretimYılı
    papel = input("Ürünün Ücreti:")
    mobilya["Ürünün Ücreti"] = papel
    mbly=open("mobilya.txt","a")
    mbly.write(str(mobilya)+"\n")
    mbly.close()
    print("Ürün Kaydı Başarılı!!")


def beyazSilme():           #Beyaz eşya kaydı silme
    ürünNo = input("Silinecek Ürünün Numarası:")
    sucuk = []
    dosya = open("beyazEşya.txt","r")
    for s in dosya:
        sucuk.append(s)
    dosya.close()
    tutucu = 0
    for i in sucuk:         #Ürün numarasından silme
        tutucu +=1
        if ürünNo == i[18:21]:
            break
    saklı = ""
    d = open("beyazEşya.txt","r")
    saglam = d.read().splitlines()
    for n,s in enumerate(saglam,1):
        if n == tutucu:
            continue
        saklı = saklı + s + "\n"
    d.close()
    with open("beyazEşya.txt","w") as d:
        d.write(saklı)
    print("Ürün Başarıyla Silindi..")

def mobilyaSilme():         #Mobilya kaydı silme
    ürünNo = input("Silinecek Ürünün Numarası:")
    sucuk = []
    dosya = open("mobilya.txt","r")
    for s in dosya:
        sucuk.append(s)
    dosya.close()
    tutucu = 0
    for i in sucuk:         #Ürün numarasından silme
        tutucu +=1
        if ürünNo == i[18:22]:
            break
    saklı = ""
    d = open("mobilya.txt","r")
    saglam = d.read().splitlines()
    for n,s in enumerate(saglam,1):
        if n == tutucu:
            continue
        saklı = saklı + s + "\n"
    d.close()
    with open("mobilya.txt","w") as d:
        d.write(saklı)
    print("Ürün Başarıyla Silindi..")


def beyazGuncelle():            #Beyaz eşya güncelleme
    ürünNo = input("Güncellenecek Ürünün Numarası:")
    dosya = open("beyazEşya.txt", "r")
    sucuk = []
    for i in dosya:
        sucuk.append(i)
    dosya.close()
    tutucu = 0
    for i in sucuk:
        tutucu = tutucu + 1  # girilen numaranın hangi satırda olduğunu bulma
        if ürünNo == i[18:21]:
            break

    helö = ""
    k = open("beyazEşya.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == tutucu:
            continue
        helö = helö + s + "\n"
    k.close()
    with open("beyazEşya.txt", "w") as k:
        k.write(helö)
    k.close()

    beyaz = {}
    ürünNo = random.randint(100, 999)
    beyaz["Ürün Numarası"] = ürünNo
    ürünName = input("Ürünün İsmi:")
    beyaz["Ürünün İsmi"] = ürünName
    kütle = int(input("Ürünün Ortalama Ağırlığı(Gram):"))
    beyaz["Ürünün Ortalama Ağrılığı"] = kütle
    renk = input("Ürünün Rengi:")
    beyaz["Ürünün Rengi"] = renk
    üretimYılı = input("Ürünün Üretim Yılı:")
    beyaz["Ürünün Üretim Yılı"] = üretimYılı
    papel = input("Ürünün Ücreti:")
    beyaz["Ürünün Ücreti"] = papel
    byz = open("beyazEşya.txt", "a")
    byz.write(str(beyaz) + "\n")
    byz.close()
    print("Ürün Güncellemesi Başarılı!!")


def mobilyaGuncelle():          #Mobilya Güncelleme
    ürünNo = input("Güncellenecek Çizelgenin Numarası:")
    dosya = open("mobilya.txt", "r")
    sucuk = []
    for i in dosya:
        sucuk.append(i)
    dosya.close()
    tutucu = 0
    for i in sucuk:
        tutucu = tutucu + 1  # girilen numaranın hangi satırda olduğunu bulma
        if ürünNo == i[18:22]:
            break

    helö = ""
    k = open("mobilya.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == tutucu:
            continue
        helö = helö + s + "\n"
    k.close()
    with open("mobilya.txt", "w") as k:
        k.write(helö)
    k.close()

    mobilya = {}
    ürünNo = random.randint(1000, 9999)
    mobilya["Ürün Numarası"] = ürünNo
    ürünName = input("Ürünün İsmi:")
    mobilya["Ürünün İsmi"] = ürünName
    kütle = int(input("Ürünün Ortalama Ağırlığı(Gram):"))
    mobilya["Ürünün Ortalama Ağrılığı"] = kütle
    renk = input("Ürünün Rengi:")
    mobilya["Ürünün Rengi"] = renk
    üretimYılı = input("Ürünün Üretim Yılı:")
    mobilya["Ürünün Üretim Yılı"] = üretimYılı
    papel = input("Ürünün Ücreti:")
    mobilya["Ürünün Ücreti"] = papel
    mbly = open("mobilya.txt", "a")
    mbly.write(str(mobilya) + "\n")
    mbly.close()
    print("Ürün Güncellemesi Başarılı!!")

def beyazArama():           #Beyaz eşya bulma
    ürünNo =input("Ürün Numarası:")
    sosis=[]
    dosya=open("beyazEşya.txt","r")
    for s in dosya:
        sosis.append(s)
    dosya.close()
    tutamac = 0
    for i in sosis:         # Numara ile cismi bulma
        tutamac += 1
        if ürünNo == i[18:21]:
            break
    print(sosis[tutamac-1])



def mobilyaArama():         #Mobilya bulma
    ürünNo =input("Ürün Numarası:")
    sosis=[]
    dosya=open("mobilya.txt","r")
    for s in dosya:
        sosis.append(s)
    dosya.close()
    tutamac = 0
    for i in sosis:         # Numara ile cismi bulma
        tutamac += 1
        if ürünNo == i[18:22]:
            break
    print(sosis[tutamac-1])



def beyazListele():         #Beyaz eşya listeleme
    dosya = open("beyazEşya.txt","r")
    for tlm in dosya:
        print(tlm)



def mobilyaListele():           #Mobilya listeleme
    dosya = open("mobilya.txt","r")
    for ıks in dosya:
        print(ıks)


def beyazMonte():           #Beyaz eşya monte parası ve randevu
    byzMnt = {}
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    byzMnt["Montelenecek Ürünün Ortalama Ağrılığı"] = ortAgr
    evKat = int(input("Ev Kaçıncı Katta:"))
    byzMnt["Ev Kaçıncı Katta"] = evKat
    yol = int(input("Mağaza-Ev Arası Mesafe:"))
    byzMnt["Mağaza-Ev Arası Mesafe"] = yol
    if ortAgr <500:
        a = ortAgr*0.1
        r = random.randint(1, 5)
        print("Kaç gün sonra Geleceğiz",r)
    elif ortAgr>=500 & ortAgr<2000:
        a = ortAgr*0.25
        r = random.randint(5, 7)
        print("Kaç gün sonra Geleceğiz", r)
    elif ortAgr>=2000:
        a = ortAgr*0.4
        r = random.randint(7, 10)
        print("Kaç gün sonra Geleceğiz", r)

    if evKat <0 & evKat >=-3:
        b = 10
    elif evKat <-3 & evKat >=-6:
        b = 30
    elif evKat <-6:
        b = 40


    if evKat >0 & evKat<=2:
        b = 10
    elif evKat >2 & evKat <=5:
        b = 30
    elif evKat >5:
        b = 40


    if yol >0 & yol<=8:
        c = 5
    elif yol >8 & yol<=20:
        c = 15
    elif yol >20:
        c= 25

    para = a+b+c
    print("Montaj Ücreti",para)



def mobilMonte():           #Mobilya monte parası ve randevu
    mblMnt = {}
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    mblMnt["Montelenecek Ürünün Ortalama Ağrılığı"] = ortAgr
    evKat = int(input("Ev Kaçıncı Katta:"))
    mblMnt["Ev Kaçıncı Katta"] = evKat
    yol = int(input("Mağaza-Ev Arası Mesafe:"))
    mblMnt["Mağaza-Ev Arası Mesafe"] = yol
    if ortAgr <500:
        a = ortAgr*0.2
        r = random.randint(1, 5)
        print("Kaç gün sonra Geleceğiz",r)
    elif ortAgr>=500 & ortAgr<2000:
        a = ortAgr*0.35
        r = random.randint(5, 7)
        print("Kaç gün sonra Geleceğiz", r)
    elif ortAgr>=2000:
        a = ortAgr*0.45
        r = random.randint(7, 10)
        print("Kaç gün sonra Geleceğiz", r)

    if evKat <0 & evKat >=-3:
        b = 10
    elif evKat <-3 & evKat >=-6:
        b = 30
    elif evKat <-6:
        b=40


    if evKat >0 & evKat<=2:
        b = 15
    elif evKat >2 & evKat <=5:
        b = 35
    elif evKat >5:
        b = 45


    if yol >0 & yol<=8:
        c = 8
    elif yol >8 & yol<=20:
        c = 19
    elif yol >20:
        c= 27

    para = a+b+c
    print("Montaj Ücreti",para)



def beyazTicari():          #Şehir dışı için Beyaz eşya monte parası ve randevu
    byzTic = {}
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    byzTic["Montelenecek Ürünün Ortalama Ağrılığı"] = ortAgr
    yol = int(input("Mağaza-İl Arası Mesafe:"))
    byzTic["Mağaza-İl Arası Mesafe"] = yol
    if ortAgr <500:
        a = ortAgr*0.3
        r = random.randint(4, 9)
    elif ortAgr>=500 & ortAgr<2000:
        a = ortAgr*0.4
        r = random.randint(9, 12)
    elif ortAgr>=2000:
        a = ortAgr*0.5
        r = random.randint(12, 15)

    if yol >0 & yol<=100:
        c = 30
        ar = random.randint(1, 3)
    elif yol >100 & yol<=200:
        c = 40
        ar = random.randint(3, 5)
    elif yol >200:
        c = 55
        ar = random.randint(5, 9)



    para = a+c
    gidis = r+ar
    print("Kaç gün sonra Geleceğiz", gidis)
    print("Ücret",para)


def mobilTicari():          #Şehir dışı için Mobilya monte parası ve randevu
    mobilTic = {}
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    mobilTic["Montelenecek Ürünün Ortalama Ağrılığı"] = ortAgr
    yol = int(input("Mağaza-İl Arası Mesafe:"))
    mobilTic["Mağaza-İl Arası Mesafe"] = yol
    if ortAgr < 500:
        a = ortAgr * 0.25
        r = random.randint(3, 6)
    elif ortAgr >= 500 & ortAgr < 2000:
        a = ortAgr * 0.38
        r = random.randint(6, 10)
    elif ortAgr >= 2000:
        a = ortAgr * 0.52
        r = random.randint(10, 17)

    if yol > 0 & yol <= 100:
        c = 30
        ar = random.randint(1, 4)
    elif yol > 100 & yol <= 200:
        c = 40
        ar = random.randint(4, 7)
    elif yol > 200:
        c = 55
        ar = random.randint(7, 10)

    para = a + c
    gidis = r + ar
    print("Kaç gün sonra Geleceğiz", gidis)
    print("Ücret", para)


def beyazHazır():           #Beyaz eşya hazır monteli yollama için para ve randevu
    byzHzr = []
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    byzHzr.append(ortAgr)
    yol = int(input("Mağaza-İl Arası Mesafe:"))
    byzHzr.append(yol)

    if ortAgr < 250:
        a = ortAgr * 0.30
        r = random.randint(5, 11)
    elif ortAgr >= 250 & ortAgr < 1750:
        a = ortAgr * 0.56
        r = random.randint(11, 15)
    elif ortAgr >= 1750:
        a = ortAgr * 0.79
        r = random.randint(15, 19)

    if yol > 0 & yol <= 70:
        c = 40
        ar = random.randint(2, 5)
    elif yol > 70 & yol <= 180:
        c = 55
        ar = random.randint(5, 9)
    elif yol > 180:
        c = 72
        ar = random.randint(9, 13)

    para = a + c
    gidis = r + ar
    print("Kaç gün sonra Geleceğiz", gidis)
    print("Ücret", para)


def mobilHazır():           #Mobilya hazır monteli yollama için para ve randevu
    mblHzr = []
    ortAgr = int(input("Montelenecek Ürünün Ortalama Ağrılığı:"))
    mblHzr.append(ortAgr)
    yol = int(input("Mağaza-İl Arası Mesafe:"))
    mblHzr.append(yol)


    if ortAgr < 200:
        a = ortAgr * 0.35
        r = random.randint(4, 110)
    elif ortAgr >= 200 & ortAgr < 1930:
        a = ortAgr * 0.60
        r = random.randint(11, 15)
    elif ortAgr >= 1930:
        a = ortAgr * 0.83
        r = random.randint(15, 19)

    if yol > 0 & yol <= 75:
        c = 48
        ar = random.randint(1, 5)
    elif yol > 75 & yol <= 205:
        c = 62
        ar = random.randint(5, 12)
    elif yol > 205:
        c = 79
        ar = random.randint(12, 14)

    para = a + c
    gidis = r + ar
    print("Kaç gün sonra Geleceğiz", gidis)
    print("Ücret", para)



while 1:            #Sürekli Döngü
    s = girisKısmı()
    if s == 1:


        b = altEkran()
        if b == 1:
            whiteEsya()
        elif b == 2:
            Mibolyu()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")



    elif s == 2:


        b = altEkran()
        if b == 1:
            beyazSilme()
        elif b == 2:
            mobilyaSilme()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 3:


        b = altEkran()
        if b == 1:
            beyazGuncelle()
        elif b == 2:
            mobilyaGuncelle()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 4:


        b = altEkran()
        if b == 1:
            beyazArama()
        elif b == 2:
            mobilyaArama()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 5:


        b = altEkran()
        if b == 1:
            beyazListele()
        elif b == 2:
            mobilyaListele()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 6:


        b = altEkran()
        if b == 1:
            beyazMonte()
        elif b == 2:
            mobilMonte()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 7:


        b = altEkran()
        if b == 1:
            beyazTicari()
        elif b == 2:
            mobilTicari()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")


    elif s == 8:


        b = altEkran()
        if b == 1:
            beyazHazır()
        elif b == 2:
            mobilHazır()
        elif b == 3:
            girisKısmı()
        elif b == 4:
            break
        else:
            print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")



    elif s == 9:
        break
    else:
        print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")
        girisKısmı()
