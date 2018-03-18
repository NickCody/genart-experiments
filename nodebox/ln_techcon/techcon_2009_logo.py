d = 45
r = 9
c = 11
size(c*d, r*d)

techcon = "TECHCON"
yyyy = "2009"
    
def drawdots():
    font('Visitor TT1 (BRK)', d)

    push()
    
    #global frame
    #frame += 1
    
    fill(0,0,0,1) # black dots

    for x, y in grid(c,r,d,d):
        push()
        if y == 3*d and x in range(2*d, 9*d):
            scale(random(1.0,1.4))
        elif y == 5*d and x in range(5*d, 9*d):
            scale(random(1.0,1.4))
        else:
            scale(random(0.2,1.0))
        #fill(random(0.5),random(0.5),random(.5)+.5,1) # color dots
        oval(x,y,d,d)
        pop()


    fill(1,1,1,1)

    drawtext(techcon, 2, 4)
    drawtext(yyyy, 5, 6)

def drawtext(t, r1, c1):
    push()

    ox = (d-textwidth(t[0]))/2
    oy = (d-textheight(t[0])/2)/2
    
    translate((r1-1)*d+ox, c1*d-oy)
    
    # techcon
    for i in range (0,len(t)):
        translate(d, 0)
        #fill(random(.75)+.25,random(.75)+.25,random(.25)+.75,1) # color letters
        text(t[i], 0, 0)
        i = i + 1

    pop()

drawdots()    
