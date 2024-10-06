import random
from ttkbootstrap import *
import pygame
import time

MainWords = []
j = 61
points = 0
pygame.init()
Music = pygame.mixer.music.load("sleepy-bear-cub-222385.mp3")
pygame.mixer.music.play(-1)
Sound = pygame.mixer.Sound("mixkit-video-game-win-2016.wav")
Sound.set_volume(0.8)
def Less_than_or_equal_to_4():
    global MainWords
    MainWords = ["This is my cat.", "My cat likes milk.", "My cat can jump.",
                "The den is dim.", "I see the den.", "That is a den.", "The den is big.",
                "She sets the bed.", "The bed is flat.", "This is my bed.",
                "The man is fat.", "The man can hop.",
                "This mug is big.", "That mug is hot.",
                "I see a pot.", "The pot is hot.",
                "I had a bun.", "The bun is cold", "She likes buns", "That bun is soft.",
                "This pig is pink.", "The pig has a cap.",
                "This is my bag.", "The bag is wet.",
                "She has a kid.", "He fed the kid.", "The kid can run.",
                "This is a tin.",
                "This is a lid.", "He hid the lid.",
                "The hen is red.", "The hen can run.",
                "She has six eggs.",
                "My dog can run.", "My dog can jump.",
                "My mom can mop.", "This mop is long.", "The mop is wet.",
                "She has a nut.", "The nut is big.", "I like nuts.",
                "I am a boy.", "I am a girl.", "He is a boy.", "She is a girl.",
                "This is my hat.", "She has a top.", "I like my top.",
                "You are my mom.", "Play with me.", "He was fit.", "My bag is here.", "There is a hat."]
    root.destroy()
def More_than_4():
    global MainWords
    MainWords = ["My cat has soft fur.", "The cat bit the rat.",
               "The fox is in the den.",
               "This box has a lid.", "A pen is in the box.", "I can hold the box.", "The girl has a red box.", "The box is in the bag.",
               "The boy sleeps on the bed.", "I can jump on the bed.",
               "The man is in the van.", "The man has a pet dog.", "The man ran to the bus.",
               "The mug has a rim.", "The mug is on the jug.",
               "The girl has a mud pot.", "The pot is on the mat.", "This mud pot is red.",
               "The dog ran with the bun.",
               "The pig is in the mud.", "The pig has a cap.", "The wig fits the pig.", "That pig sat on the rug.",
               "The girl has a bag.", "The pin is in the bag.", "The bag has a zip.",
               "The kid is in the pen.", "That kid was near the den.",
               "The tin has a lid.", "This tin is in the bin.", "Milk is in the tin.", "The cat sat on the tin.",
               "The jug has a lid.", "This lid fits the pan.", "She can lift the lid.",
               "The hen is in the pen.", "The hen is in the nest.", "This hen sat on the eggs.",
               "The egg has a shell.", "That egg was in the pan.", "The eggs were in the nest.", "The girl has a big egg.",
               "The dog is my pet.", "My dog can dig mud.",
               "The mop is in the tub", "He hit me with the mop.",
               "The nut fell from the tree.", "The nut has a shell.", "The nut is in the box.",
               "Those are big fat hens.", "Did he see the milk?", "I like milk and sweets.", "Do you drink water?"]
    root.destroy()

root = Window(themename="journal")
root.geometry("900x600")
root.title("Reading game")

mysty = Style()
mysty.configure("default.TButton", font=("Comic Sans MS", 18, "bold italic"))
L1 = Label(root, text = "How many words would you like\n      in your sentences?", font=("Comic Sans MS", 18, "bold italic"))
F1 = Frame(root)
B1 = Button(F1, text="3 or 4 words", style="default.TButton", command=Less_than_or_equal_to_4)
B2 = Button(F1, text="5 or 6 words", style="default.TButton", command=More_than_4)
L1.place(relx = 0.5, rely = 0.35, anchor='center')
B1.pack(padx = 20, side = 'left')
B2.pack(padx = 20, side = 'right')
F1.place(relx = 0.5, rely = 0.55, anchor='center')
root.mainloop()

class LackOfInformationError(Exception):
    def __init__(self,
                 message="Please select an option"
                 ):
            super().__init__(message)

if MainWords == []:
    raise LackOfInformationError

################################################################

screen = pygame.display.set_mode((800, 500))
running = True
Clock = pygame.time.Clock()

Font1 = pygame.font.Font("VarelaRound-Regular.otf", 40)
Font2 = pygame.font.Font("VarelaRound-Regular.otf", 30)

Diamond = pygame.transform.scale(pygame.image.load("Diamond.png"), (225, 225))
Barbie = pygame.transform.scale(pygame.image.load("Barbie.png"), (225, 225))
DiamondRect = Diamond.get_rect(center = (400, 250))

Option = random.choice(MainWords)
i = 0
while running:
    T1 = Font1.render(f'{Option}', True, 'black')
    T1Rect = T1.get_rect(center = ((400 - (len(Option) / 2)), 250))
    T2 = Font2.render(f'Points: {points}', True, 'black')
    T2Rect = T2.get_rect(center = ((400 - ((9 + len(str(points))) / 2)), 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        i += 1
        if i == 8:
            Option = random.choice(MainWords)
            points += 1
            Sound.play()
            i = 0

    screen.fill("white")
    if points % 4 == 0 and points != 0:
        active = True
        p = 0
        Option2 = random.choice([Diamond, Barbie])
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False
                    points += 1

            if p == 2000:
                active = False
                points += 1

            p += 1
            screen.fill('white')
            screen.blit(Option2, DiamondRect)
            pygame.display.update()

    screen.blit(T1, T1Rect)
    screen.blit(T2, T2Rect)
    pygame.display.update()
    Clock.tick(100)