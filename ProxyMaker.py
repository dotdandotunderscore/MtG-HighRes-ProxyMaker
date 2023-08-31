import scrython
import time
from fpdf import FPDF
import numpy as np
start = time.time()

proxy_list = np.genfromtxt('proxy_list.txt', dtype=str, delimiter='\n')

num_cards = 0
image_paths=[]
iterator = 1
for i in proxy_list:
    iterator+=1
    if iterator%10 == 0:
        print('Current card being processed:',iterator)
    ammount = int(i.split("x", 1)[0])
    num_cards+=ammount
    card_name = i.split("x",1)[1].split("(")[0][1:-1]
    set_code = i.split("x",1)[1].split("(")[1].split(")")[0]
    time.sleep(0.05) #Use inbetween lookups to keep scryfall happy
    card = scrython.cards.Named(fuzzy=card_name, set=set_code)
    for i in range(ammount):
        try:
            faces = card.card_faces()
            for j in faces:
                image = j['image_uris']['png']
                image_paths.append(image)
        except KeyError:
            image = card.image_uris()['png']
            image_paths.append(image)

print('Time to get: ' + str(time.time()-start))

cards_added=0

pdf = FPDF()
pdf.add_page()
# x=4.5
# xjump=67
# y=8
# yjump=93.5
x=10
xjump=63
y=15
yjump=88
xcards=0
ycards=1
iterator = 1
for image in image_paths:
    iterator+=1
    if iterator%10 == 0:
        print(iterator)
    cards_added+=1
    xcards+=1
    if xcards==4:
        if ycards==3:
            pdf.add_page()
            xcards=1
            ycards=1
        else:
            xcards=1
            ycards=ycards+1
    xpos=x+(xcards-1)*xjump
    ypos=y+(ycards-1)*yjump
    pdf.image(image[:-11], x=xpos, y=ypos, w=63, h=88)
    if cards_added%10 == 0:
        print('Cards added: ' + str(cards_added) + '. Time elapsed: ' + str(time.time()-start))
print('Saving')
pdf.output('cards.pdf', 'F')


print('Time to complete: ' + str(time.time()-start))
print('Time per card: ' + str((time.time()-start)/num_cards))
