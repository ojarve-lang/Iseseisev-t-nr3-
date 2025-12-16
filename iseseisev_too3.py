#Olavi Järve
#16.12.2025
#Kilpkonnaga kujundite joonistamine

import turtle
#alustame kilpkonna toomisega

import random
# Võimaldab teha juhusliku valiku

t = turtle.Turtle()
# Loob kilpkonna nimega t

t.speed(5)
# Määrab kilpkonna liikumise kiiruse

def ruut():
    # Funktsioon ruudu joonistamiseks
    for i in range(4):
        # Kordab tegevust 4 korda
        t.forward(50)
        # Kilpkonn liigub 50 sammu edasi
        t.right(90)
        # Kilpkonn pöörab 90 kraadi paremale

def ring():
    # Funktsioon ringi joonistamiseks
    t.circle(30)
    # Kilpkonn joonistab ringi raadiusega 30

def viisnurk():
    # Funktsioon viisnurga joonistamiseks
    for i in range(5):
        # Kordab tegevust 5 korda
        t.forward(50)
        # Kilpkonn liigub 50 sammu edasi
        t.right(72)
        # Kilpkonn pöörab 72 kraadi paremale

while True:
    # Programm töötab seni, kuni kasutaja lõpetab

    kujund = input("Kirjuta ruut, ring, viisnurk või suvaline (Enter = lõpeta): ")
    # Küsib kasutajalt kujundi tüübi

    if kujund == "":
        # Kontrollib, kas kasutaja vajutas ainult Enterit
        break
        # Lõpetab programmi töö

    kogus = int(input("Mitu kujundit?: "))
    # Küsib, mitu kujundit joonistada ja muudab selle arvuks

    for i in range(kogus):
        # Kordab joonistamist nii mitu korda, kui kasutaja sisestas

        if kujund == "ruut":
            # Kui kasutaja valis ruudu
            ruut()
            # Joonistab ruudu

        elif kujund == "ring":
            # Kui kasutaja valis ringi
            ring()
            # Joonistab ringi

        elif kujund == "viisnurk":
            # Kui kasutaja valis viisnurga
            viisnurk()
            # Joonistab viisnurga

        else:
            # Kui kasutaja valis suvalise
            valik = random.choice(["ruut", "ring", "viisnurk"])
            # Valib juhuslikult ühe kujundi

            if valik == "ruut":
                ruut()
                # Joonistab ruudu

            elif valik == "ring":
                ring()
                # Joonistab ringi

            else:
                viisnurk()
                # Joonistab viisnurga

        t.penup()
        # Tõstab pliiatsi üles (ei joonista)

        t.forward(70)
        # Liigutab kilpkonna edasi, et kujundid ei kattuks

        t.pendown()
        # Paneb pliiatsi tagasi alla (joonistab edasi)

turtle.done()
# Hoiab akna avatuna, kuni kasutaja selle sulgeb
