import pygame
pygame.init()
win = pygame.display.set_mode((1200,820))

pygame.display.set_caption("First Game")
pygame.display.set_caption("MolodoiTalant")

walkRight=[pygame.image.load("0_Fallen_Angels_Running_000.png"),pygame.image.load("0_Fallen_Angels_Running_001.png"),
pygame.image.load("0_Fallen_Angels_Running_002.png"),pygame.image.load("0_Fallen_Angels_Running_003.png"),pygame.image.load("0_Fallen_Angels_Running_004.png"),
pygame.image.load("0_Fallen_Angels_Running_005.png"),pygame.image.load("0_Fallen_Angels_Running_006.png"),pygame.image.load("0_Fallen_Angels_Running_007.png"),
pygame.image.load("0_Fallen_Angels_Running_008.png"),pygame.image.load("0_Fallen_Angels_Running_009.png"),pygame.image.load("0_Fallen_Angels_Running_010.png"),pygame.image.load("0_Fallen_Angels_Running_011.png")]

walkLeft=[pygame.image.load("0_Fallen_Angels_Running_000.png"),pygame.image.load("0_Fallen_Angels_Running_001.png"),
pygame.image.load("0_Fallen_Angels_Running_002.png"),pygame.image.load("0_Fallen_Angels_Running_003.png"),pygame.image.load("0_Fallen_Angels_Running_004.png"),
pygame.image.load("0_Fallen_Angels_Running_005.png"),pygame.image.load("0_Fallen_Angels_Running_006.png"),pygame.image.load("0_Fallen_Angels_Running_007.png")]

PlayerStand=pygame.image.load("0_Fallen_Angels_Idle Blinking_000.png")
bj=pygame.image.load("Background/game_background_1/game_background_1.png")
#scale=pygame.transform.scale(bj,(bj.get_width()//1, bj.get_height()//1))
pygame.display.set_caption("Molodoi Talant")
#bulletSound=pygame.mixer.Sound('Music/ad.wav')
#hitSound=pygame.mixer.Sound("44.wav")
music=pygame.mixer.music.load("Music/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


score=0

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x +100, self.y +100, 52, 70)


    def draw(self, win):
        if self.walkCount + 1 >= 11:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//2], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x +100, self.y + 100, 52, 70)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def hit(self):
        self.IsJump=False
        self.jumpCount=10
        self.x=60
        self.y=610
        self.walkCount=0
        font2=pygame.font.SysFont("comicsans",100)
        text=font2.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))
        pygame.display.update()
        i=0
        while i<120:
            pygame.time.delay(5)
            i+=1
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    i=301
                    win.fill()
                    pygame.quit()

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)






class enemy(object):
    walkRight=[pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_000.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_001.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_002.png"),
    pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_003.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_004.png"),
    pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_005.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_006.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_007.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_008.png")]
    walkLeft=[pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_000.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_001.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_002.png"),
    pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_003.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_004.png"),
     pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_005.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_006.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_007.png"),pygame.image.load("Enemy1/Running/0_Fallen_Angels_Running_008.png")]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health=10
        self.visible=True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 11:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //2], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //2], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255,0,0),(self.hitbox[0],self.hitbox[1]-100,50,10))
            pygame.draw.rect(win, (0,255,0),(self.hitbox[0],self.hitbox[1]-100,50-(5*(10-self.health)),10))
            self.hitbox = (self.x +100, self.y + 100, 52, 70)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health >0:
            self.health-=1
        else:
            self.visible=False
        print('hit')

    def shoot(self):
        if  self.vel > 0:
            facing = -1
        else:
            facing = 1

        if self.visible==True:
            bullets.append(Enemyprojectile(round(goblin.x + goblin.width //2), round(goblin.y +goblin.height//2), 6, (0,255,0),facing))
            bullets.append(Enemyprojectile(round(goblin1.x + goblin1.width //2), round(goblin1.y +goblin1.height//2), 6, (0,255,0),facing))




def redrawGameWindow():
    global goblins
    win.blit(bj, (0,0))
    text=font1.render("Score: "+str(score),1,(255,0,0))
    text1=font1.render("Игра Молодого Таланта",1,(150,0,0))
    win.blit(text,(1000,10))
    win.blit(text1,(500,200))
    man.draw(win)
    for goblin in goblins:
        goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
font1=pygame.font.SysFont("comicsans",50,True)
man = player(300,600, 250,250)
goblin = enemy(800, 600, 300, 300, 1000)
goblin1 = enemy(400, 600, 300, 300, 800)
goblins=[goblin,goblin1]
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(60)

    if goblin.visible==True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5
    if goblin1.visible==True:
        if man.hitbox[1] < goblin1.hitbox[1] + goblin1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin1.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin1.hitbox[0] and man.hitbox[0] < goblin1.hitbox[0] + goblin1.hitbox[2]:
                man.hit()
                score -= 5
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score+=1
                bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin1.hitbox[1] + goblin1.hitbox[3] and bullet.y + bullet.radius > goblin1.hitbox[1]:
            if bullet.x + bullet.radius > goblin1.hitbox[0] and bullet.x - bullet.radius < goblin1.hitbox[0] + goblin1.hitbox[2]:
                goblin1.hit()
                score+=1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 30:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (255,13,5), facing))

        shootLoop = 1

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_d] and man.x < 1100- man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_w]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
