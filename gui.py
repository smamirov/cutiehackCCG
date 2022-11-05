from tkinter import *
from environmentalCards import *
from innovationCards import *
from PIL import ImageTk, Image

root = Tk()
root.title("Wasteful Innovation")
root.geometry('800x600')
root.state("zoomed")

availableInnovationCards = [space_Exploration, Deep_Sea_Exploration, self_Driving_Cars, sustainable_Aviation, accesible_Transportation, teleporation, artifical_Intelligence, cryptocurrency, virtual_Reality, quantum_Computing, panacea, food]

def readDescription(i):
    top = Toplevel(root)
    top.lift()
    top.title("Description")
    textString = availableInnovationCards[i].card_desc
    label = Label(top, text=textString)
    label.pack()


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




'''gwDeck = ImageTk.PhotoImage(Image.open('deck.png'))
gwLabel = Label(image=gwDeck)
gwLabel.pack()'''


root.mainloop()