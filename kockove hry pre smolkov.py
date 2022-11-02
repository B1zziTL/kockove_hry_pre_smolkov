#vlozenie modulu
import tkinter 

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=500, height=500, background="white") 
canvas.pack()

#premenne a zoznamy
pocet_klikov = 0
momentalne_suradnice = []
listik_x = [50,100,150,200,250,300,350,400,450,500]
listik_y = [50,100,150,200,250,300,350,400,450,500]

def mreze(): #funkcia na vykreslenie mriezky
    x1 = 50
    y1 = 50
    for i in range(10):
        canvas.create_line(x1,0,x1,500)
        canvas.create_line(0,y1,500,y1)
        x1 += 50
        y1 += 50

def klik_blik(suradnice): #funkcia na zistenie suradnic a vykreslenie
    #zistenie suradnic kliku mysky
    x = suradnice.x
    y = suradnice.y

    #globalna premenna
    global pocet_klikov
    pocet_klikov += 1

    #zistenie na ktoru kocku bolo kliknute
    for i in listik_x:
        if x < i:
            momentalne_suradnice.append(i)
            break
    for ii in listik_y:
        if y < ii:
            momentalne_suradnice.append(ii)
            break

    if pocet_klikov == 2:
        #podmienky na spravne oznacenie
        if momentalne_suradnice[0] == momentalne_suradnice[2] or momentalne_suradnice[1] == momentalne_suradnice[3]:
            #podmienky na spravne vyfarbenie zaznaceneho miesta
            if momentalne_suradnice[0] < momentalne_suradnice[2] or momentalne_suradnice[1] < momentalne_suradnice[3]:
                canvas.create_rectangle(momentalne_suradnice[0]-49,momentalne_suradnice[1]-49,momentalne_suradnice[2],momentalne_suradnice[3],fill='blue',outline='')
            elif momentalne_suradnice[0] > momentalne_suradnice[2]:
                canvas.create_rectangle(momentalne_suradnice[0],momentalne_suradnice[1]-49,momentalne_suradnice[2]-49,momentalne_suradnice[3],fill='blue',outline='')
            elif momentalne_suradnice[1] > momentalne_suradnice[3]:
                canvas.create_rectangle(momentalne_suradnice[0]-49,momentalne_suradnice[1],momentalne_suradnice[2],momentalne_suradnice[3]-49,fill='blue',outline='')

        #vymazanie predoslych pouzitych hodnot
        pocet_klikov = 0
        momentalne_suradnice.clear()

        #privolanie funkcie
        mreze()

#privolanie funkcie
mreze()

#nastavenie tlacidla mysky
canvas.bind('<Button-1>',klik_blik)
