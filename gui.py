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

#player hands: currently an empty list, because they don't have any cards.
playerOne = 1
playerTwo = 2

### TODO: on button click: flip player
current_player = playerOne
playerOneHand = []
playerTwoHand = []
currentPlayerHand = playerOneHand
# or player = playerTwo

#assuming button 0 is pressed:

#space_Exploration.draw(current_player)
#current_player = playerTwo

#assuming button 5 is pressed:
#teleporation.draw(current_player)
#current_player = playerOne

#and so on

def readDescription(i):
    top = Toplevel(root)
    top.lift()
    top.title("Description")
    textString = availableInnovationCards[i].card_desc
    label = Label(top, text=textString)
    label.pack()

def pick(i, current_player, currentPlayerHand):
    #myCanvas.create_line(x1, y1, x2, y2, fill="red")
    if i == 1:
        pickButton1["state"] = "disabled"
        space_Exploration.draw(currentPlayerHand)
        if current_player == 1:
            current_player = 2
            currentPlayerHand = playerTwoHand
        else:
            current_player = 1
            currentPlayerHand = playerOneHand
    elif i == 2:
        pickButton2["state"] = "disabled"
        deep_Sea_Exploration.draw(currentPlayerHand)
        if current_player == 1:
            current_player = 2
            currentPlayerHand = playerTwoHand
        else:
            current_player = 1
            currentPlayerHand = playerOneHand
    elif i == 3:
        pickButton3["state"] = "disabled"
        self_Driving_Cars.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 4:
        pickButton4["state"] = "disabled"
        sustainable_Aviation.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 5:
        pickButton5["state"] = "disabled"
        accesible_Transportation.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 6:
        pickButton6["state"] = "disabled"
        teleporation.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 7:
        pickButton7["state"] = "disabled"
        artifical_Intelligence.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 8:
        pickButton8["state"] = "disabled"
        cryptocurrency.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 9:
        pickButton9["state"] = "disabled"
        virtual_Reality.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 10:
        pickButton10["state"] = "disabled"
        quantum_Computing.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 11:
        pickButton11["state"] = "disabled"
        panacea.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    elif i == 12:
        pickButton12["state"] = "disabled"
        food.draw(current_player)
        if current_player is playerOne:
            current_player = playerTwo
        else:
            current_player = playerOne
    

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

pickButton1 = Button(root, text="Pick Card", command=lambda:pick(1, current_player, currentPlayerHand))
pickButton2 = Button(root, text="Pick Card", command=lambda:pick(2, current_player, currentPlayerHand))
pickButton3 = Button(root, text="Pick Card", command=lambda:pick(3, current_player))
pickButton4 = Button(root, text="Pick Card", command=lambda:pick(4, current_player))
pickButton5 = Button(root, text="Pick Card", command=lambda:pick(5, current_player))
pickButton6 = Button(root, text="Pick Card", command=lambda:pick(6, current_player))
pickButton7 = Button(root, text="Pick Card", command=lambda:pick(7, current_player))
pickButton8 = Button(root, text="Pick Card", command=lambda:pick(8, current_player))
pickButton9 = Button(root, text="Pick Card", command=lambda:pick(9, current_player))
pickButton10 = Button(root, text="Pick Card", command=lambda:pick(10, current_player))
pickButton11 = Button(root, text="Pick Card", command=lambda:pick(11, current_player))
pickButton12 = Button(root, text="Pick Card", command=lambda:pick(12, current_player))

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




'''gwDeck = ImageTk.PhotoImage(Image.open('deck.png'))
gwLabel = Label(image=gwDeck)
gwLabel.pack()'''

'''def refresh():
    root.configure()
    print(current_player)
    pickButton1.configure(command=lambda:pick(1, current_player, currentPlayerHand))
    pickButton2.configure(command=lambda:pick(2, current_player, currentPlayerHand))
    if playerOneHand:
        print(playerOneHand[0].name)
    if playerTwoHand:
        print(playerTwoHand[0].name)

button = Button(root, text="Your Turn", command=refresh).pack()'''
if playerOneHand:
    print(playerOneHand[0].name)
if playerTwoHand:
    print(playerTwoHand[0].name)
root.mainloop()
'''if playerOneHand:
        print(playerOneHand[0].name)
if playerTwoHand:
    print(playerTwoHand[0].name)'''