from tkinter import *
#from environmentalCards import *
#from innovationCards import *
from PIL import ImageTk, Image
from ccg import *

root = Tk()
root.title("Wasteful Innovation")
root.geometry('800x600')
root.state("zoomed")

availableInnovationCards = [space_Exploration, deep_Sea_Exploration, self_Driving_Cars, sustainable_Aviation, accesible_Transportation, teleporation, artifical_Intelligence, cryptocurrency, virtual_Reality, quantum_Computing, panacea, food]

one = []
two = []
counter = [0]

def readDescription(i):
    top = Toplevel(root)
    top.lift()
    top.title("Description")
    textString = availableInnovationCards[i].card_desc
    label = Label(top, text=textString)
    label.pack()

def pick(i):
    #myCanvas.create_line(x1, y1, x2, y2, fill="red")
    if i == 1:
        pickButton1["state"] = "disabled"
        if len(counter) % 2 == 0:
            space_Exploration.draw(one)
        else:
            space_Exploration.draw(two)
        counter.append(0)
    elif i == 2:
        pickButton2["state"] = "disabled"
        if len(counter) % 2 == 0:
            deep_Sea_Exploration.draw(one)
        else:
            deep_Sea_Exploration.draw(two)
        counter.append(0)
    elif i == 3:
        pickButton3["state"] = "disabled"
        if len(counter) % 2 == 0:
            self_Driving_Cars.draw(one)
        else:
            self_Driving_Cars.draw(two)
        counter.append(0)
    elif i == 4:
        pickButton4["state"] = "disabled"
        if len(counter) % 2 == 0:
            sustainable_Aviation.draw(one)
        else:
            sustainable_Aviation.draw(two)
        counter.append(0)
    elif i == 5:
        pickButton5["state"] = "disabled"
        if len(counter) % 2 == 0:
            accesible_Transportation.draw(one)
        else:
            accesible_Transportation.draw(two)
        counter.append(0).draw(current_player)
    elif i == 6:
        pickButton6["state"] = "disabled"
        if len(counter) % 2 == 0:
            teleporation.draw(one)
        else:
            teleporation.draw(two)
        counter.append(0)
    elif i == 7:
        pickButton7["state"] = "disabled"
        if len(counter) % 2 == 0:
            artifical_Intelligence.draw(one)
        else:
            artifical_Intelligence.draw(two)
        counter.append(0)
    elif i == 8:
        pickButton8["state"] = "disabled"
        if len(counter) % 2 == 0:
            cryptocurrency.draw(one)
        else:
            cryptocurrency.draw(two)
        counter.append(0)
    elif i == 9:
        pickButton9["state"] = "disabled"
        if len(counter) % 2 == 0:
            virtual_Reality.draw(one)
        else:
            virtual_Reality.draw(two)
        counter.append(0)
    elif i == 10:
        pickButton10["state"] = "disabled"
        if len(counter) % 2 == 0:
            quantum_Computing.draw(one)
        else:
            quantum_Computing.draw(two)
        counter.append(0)
    elif i == 11:
        pickButton11["state"] = "disabled"
        if len(counter) % 2 == 0:
            panacea.draw(one)
        else:
            panacea.draw(two)
        counter.append(0)
    elif i == 12:
        pickButton12["state"] = "disabled"
        if len(counter) % 2 == 0:
            food.draw(one)
        else:
            food.draw(two)
        counter.append(0)

myCanvas = Canvas(root, bg="white")
#myCanvas.grid(row=0, column=0, columnspan=3, sticky='ew')
myCanvas.pack(side='top', fill='x', expand=False)

xValues = [10, 170, 330, 490, 650, 810, 970, 1130, 1290, 1450, 1610, 1770]
yValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
coords = zip(xValues, yValues)
for x1, y1 in zip(xValues, yValues):
    x1 = int(x1)
    y1 = int(y1)
    x2 = x1 + 140
    y2 = y1 + 250
    myCanvas.create_rectangle(x1, y1, x2, y2, fill="cyan")
    w, h = 80, 20
    w2 = 50
    h2 = 70
    h3 = 110
    h4 = 150
for card in availableInnovationCards:
    myCanvas.create_text(w, h, text=card.name, fill="black")
    myCanvas.create_text(w, h2, text=f'Category: {card.category}', fill="black")
    myCanvas.create_text(w, h3, text=card.current_point_value, fill="black")
    #myCanvas.create_text(w, h4, text="Description", fill="black")
    w += 160
    w2 += 160

myButton = Button(root, text="Description", command=lambda:readDescription(0))
myButton2 = Button(root, text="Description", command=lambda:readDescription(1))
myButton3 = Button(root, text="Description", command= lambda: readDescription(2))
myButton4 = Button(root, text="Description", command= lambda: readDescription(3))
myButton5 = Button(root, text="Description", command= lambda: readDescription(4))
myButton6 = Button(root, text="Description", command= lambda: readDescription(5))
myButton7 = Button(root, text="Description", command= lambda: readDescription(6))
myButton8 = Button(root, text="Description", command= lambda: readDescription(7))
myButton9 = Button(root, text="Description", command= lambda: readDescription(8))
myButton10 = Button(root, text="Description", command= lambda: readDescription(9))
myButton11 = Button(root, text="Description", command= lambda: readDescription(10))
myButton12 = Button(root, text="Description", command= lambda: readDescription(11))
myButton13 = Button(root, text="Description", command= lambda: readDescription(12))

myButton.place(x=50, y=150)
myButton2.place(x=210, y= 150)
myButton3.place(x=370, y=150)
myButton4.place(x=530, y= 150)
myButton5.place(x=690, y=150)
myButton6.place(x=850, y= 150)
myButton7.place(x=1010, y=150)
myButton8.place(x=1170, y= 150)
myButton9.place(x=1330, y=150)
myButton10.place(x=1490, y= 150)
myButton11.place(x=1650, y=150)
myButton12.place(x=1810, y= 150)

pickButton1 = Button(root, text="Pick Card", command=lambda:pick(1))
pickButton2 = Button(root, text="Pick Card", command=lambda:pick(2))
pickButton3 = Button(root, text="Pick Card", command=lambda:pick(3))
pickButton4 = Button(root, text="Pick Card", command=lambda:pick(4))
pickButton5 = Button(root, text="Pick Card", command=lambda:pick(5))
pickButton6 = Button(root, text="Pick Card", command=lambda:pick(6))
pickButton7 = Button(root, text="Pick Card", command=lambda:pick(7))
pickButton8 = Button(root, text="Pick Card", command=lambda:pick(8))
pickButton9 = Button(root, text="Pick Card", command=lambda:pick(9))
pickButton10 = Button(root, text="Pick Card", command=lambda:pick(10))
pickButton11 = Button(root, text="Pick Card", command=lambda:pick(11))
pickButton12 = Button(root, text="Pick Card", command=lambda:pick(12))

pickButton1.place(x=55, y=200)
pickButton2.place(x=215, y=200)
pickButton3.place(x=375, y=200)
pickButton4.place(x=535, y=200)
pickButton5.place(x=695, y=200)
pickButton6.place(x=855, y=200)
pickButton7.place(x=1015, y=200)
pickButton8.place(x=1175, y=200)
pickButton9.place(x=1335, y=200)
pickButton10.place(x=1495, y=200)
pickButton11.place(x=1655, y=200)
pickButton12.place(x=1815, y=200)


'''def refresh(current_player):
    root.configure()
    if current_player:
        print(current_player[0].name, current_player[1].name, current_player[2].name)

button = Button(root, text="Your Turn", command=lambda:refresh(current_player)).pack()'''



hand1 = []
hand2 = []
for i in one:
    hand1.append(i.name)
for j in two:
    hand2.append(j.name)

root.mainloop()
'''hand = []
for i in one:
    hand.append(i)
print(hand)
halfway = len(hand)//2
two = hand[halfway:]

hand2 = []
for i in two:
    hand2.append(i.name)
print(hand2)'''
