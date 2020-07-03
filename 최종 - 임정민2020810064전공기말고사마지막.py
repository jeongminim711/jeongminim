import pygame
import sys
import random
from time import sleep

BLACK = (0,0,0)

padWidth = 984
padHeight = 554
rockImage = ['rock01.png', 'rock07.png', 'rock13.png', 'rock02.png', 'rock08.png', 'rock14.png', 'rock03.png', 'rock09.png', 'rock15.png', 'rock04.png', 'rock10.png', 'rock16.png',
              'rock05.png', 'rock11.png', 'rock17.png', 'rock06.png', 'rock12.png', 'rock18.png', 'rock19.png', 'rock23.png', 'rock27.png', 'rock20.png', 'rock24.png', 'rock28.png',
              'rock21.png', 'rock25.png', 'rock29.png', 'rock22.png', 'rock26.png', 'rock30.png' ]
diaImage = ['dia.png']

goldImage = ['gold.png']

ufoImage = ['u1-removebg.png', 'u2-removebg.png', 'u3-removebg.png', 'u4-removebg.png', 'u5-removebg.png', 'u6-removebg.png', 'u7-removebg.png']


font_1 = 'NanumGothic.ttf'

explosionSound = ['explosion01.wav', 'explosion02.wav', 'explosion03.wav', 'explosion04.wav']

def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 22)
    text = font.render('놓힌 운석 수:' + str(count), True, (255,0,0))
    gamePad.blit(text, (10, 80))

def writePassed1(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 22)
    text = font.render('놓힌 ufo 수:' + str(count), True, (255,0,0))
    gamePad.blit(text, (10, 110))

def writeScore2(count):
    global gamePad
    font = pygame.font.Font(font_1, 22)
    text = font.render('파괴한 ufo와 운석의 수:' + str(count), True, (255,255,255))
    gamePad.blit(text, (10, 20))

def writePassed2(count):
    global gamePad
    font = pygame.font.Font(font_1, 22)
    text = font.render('놓힌 ufo와 운석의 수:' + str(count), True, (255,0,0))
    gamePad.blit(text, (10, 50))    

def writeMessage(text):
    global gamePad
    gamePad.fill(BLACK)
    textfont = pygame.font.Font(font_1, 20)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(0.01)
    textfont = pygame.font.Font('font.ttf', 56)
    text = textfont.render('You failed to protect Earth', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 - 50)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    sleep(4)
    pygame.mixer.music.play()
    runGame()

def crash():
    global gamePad
    gamePad.fill(BLACK)
    writeMessage('우주선이 파괴되었습니다. 5초 후 재시작합니다')


def gameOver():
    global gamePad
    gamePad.fill(BLACK)
    writeMessage2('총 10개의 외계인과 운석을 놓쳤으며 침공을 막지 못했습니다.')

def writeMessage1(text):
    global gamePad
    pygame.mixer.music.stop()
    gamePad.fill(BLACK)
    textfont = pygame.font.Font(font_1, 20)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(0.01)
    textfont = pygame.font.Font('font.ttf', 50)
    text = textfont.render('You protected Earth', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 - 50)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(0.01)
    textfont = pygame.font.Font(font_1, 20)
    text = textfont.render('축하합니다. 5초 후 게임을 종료합니다', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 + 40)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(5)
    gamePad.fill(BLACK)
    textfont = pygame.font.Font('font.ttf', 40)
    text = textfont.render('Save the Earth', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 - 50)
    gamePad.blit(text, textpos)
    pygame.display.update()
    textfont = pygame.font.Font('font.ttf', 30)
    text = textfont.render('Thank you for playing my game', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    textfont = pygame.font.Font('font.ttf', 30)
    text = textfont.render('-Im Jeong Min-', True, (255,255,255))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 +45)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(3)
    pygame.quit()

def writeMessage2(text):
    global gamePad
    gamePad.fill(BLACK)
    textfont = pygame.font.Font(font_1, 20)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(0.01)
    textfont = pygame.font.Font('font.ttf', 50)
    text = textfont.render('You failed to protect Earth', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 - 50)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(0.01)
    textfont = pygame.font.Font(font_1, 20)
    text = textfont.render('5초 후 재시작합니다', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 + 40)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    sleep(4)
    pygame.mixer.music.play()
    runGame()



def missionClear():
    global gamePad
    gamePad.fill(BLACK)
    writeMessage1('당신은 30개의 U.F.O와 운석을 파괴했으며 지구를 구했습니다.')



def gameOver1():
    global gamePad
    gamePad.fill(BLACK)
    textfont = pygame.font.Font(font_1, 40)
    text = textfont.render('당신은 WARNING을 무시했습니다. 5초 후 재시작합니다', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 + 40)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    sleep(4)
    pygame.mixer.music.play()
    runGame()
    
#------------------------------------------------------------------------------------

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Save the Earth')
    background = pygame.image.load('space102.jpg')
    fighter = pygame.image.load('spaceship.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    pygame.mixer.music.load('space.mp3')
    missileSound = pygame.mixer.Sound('missile.wav')
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound    
    gamePad.fill(BLACK)
    textfont = pygame.font.Font('font.ttf', 50)
    text = textfont.render('Save the Earth', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2 - 50)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(1)
    textfont = pygame.font.Font('font.ttf', 30)
    text = textfont.render('Roading the game', True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    sleep(1)
    for i in range(1,280):
        sleep(0.005)
        i = i + 20
        text = textfont.render('O', True, (255,0,0))
        textpos.center = (padWidth/2 - 50 + i, padHeight/2 + 40)
        gamePad.blit(text, textpos)
        pygame.display.update()

        continue
    
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[1]
    fighterHeight = fighterSize[1]
 

    x = padWidth * 0.50
    y = padHeight * 0.82    #우주선의 위치
    fighterX = 0
    fighterY = 0

    missileXY = []
#-----------------------------------------------------------------------------
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 7                         #운석의 속도


    isShot = False
    shotCount = 0
    rockPassed = 0
#-----------------------------------------------------
    dia = pygame.image.load(random.choice(diaImage))
    diaSize = dia.get_rect().size
    diaWidth = diaSize[0]
    diaHeight = diaSize[1]

    diaX = random.randrange(0, padWidth - diaWidth)
    diaY = -1000
    diaSpeed = 5 
#-----------------------------------------------------
    gold = pygame.image.load(random.choice(goldImage))
    goldSize = gold.get_rect().size
    goldWidth = goldSize[0]
    goldHeight = goldSize[1]

    goldX = random.randrange(0, padWidth - goldWidth)
    goldY = -1200
    goldSpeed = 5
    
#-----------------------------------------------------------------------------
    ufo = pygame.image.load(random.choice(ufoImage))
    ufoSize = ufo.get_rect().size
    ufoWidth = ufoSize[0]
    ufoHeight = ufoSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    ufoX = random.randrange(0, padWidth - ufoWidth)
    ufoY = 0
    ufoSpeed = 7           #외계인의 속도



    isShot1 = False
    shotCount1 = 0
    ufoPassed = 0
#-----------------------------------------------------------------------------
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 15             #우주선 속도

                if event.key == pygame.K_RIGHT:
                    fighterX += 15

                if event.key == pygame.K_UP:
                    fighterY -= 15             #우주선 속도

                if event.key == pygame.K_DOWN:
                    fighterY += 15

                if event.key == pygame.K_SPACE:
                    missileSound.play()
                    missileX = x + fighterWidth/2 -6   #로켓 발사 위치
                    missileY = y - fighterHeight + 30
                    missileXY.append([missileX,missileY])

                if event.key == pygame.K_a:
                    gamePad.fill(BLACK)
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("방향키로 우주선을 움직이며 스페이스 바는 미사일 발사입니다.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2-80)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("40개의 운석과 U,F.O를 맞추면 당신은 승리합니다.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2-40)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("놓친 운석과 U.F.O의 개수가 10개가 되거나, 우주선과 부딫히면 임무 실패입니다.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("다이아몬드는 놓친 운석의 개수를, 골드는 놓친 U.F.O의 개수를 각 2개씩 빼줍니다.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+40)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("s키를 누르면 U.F.O와 운석의 시간이 멈추고 격추시키면 새로운 운석과 U.F.O의 속력이 초기화됩니다..", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+80)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('font.ttf', 50)
                    text = textfont.render("How to play the game.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2-130)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("운석과 U.F.O는 맞추면 점차 빨라집니다. 행운을 빕니다..", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+160)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("게임방법은 15초간 보여주며 A키를 한번 더 누르면 15초동안 또 봐야하니 한번만 누르세요.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+200)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 20)
                    text = textfont.render("그러나 놓친 운석과 U.F.O의 수에서 4를 추가하니 조심해서 사용하세요.", True, (0,255,255))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+120)
                    gamePad.blit(text, textpos)
                    pygame.display.update()


                    sleep(15)
                if event.key == pygame.K_s:
                    textfont = pygame.font.Font('font.ttf', 50)
                    text = textfont.render("WARNING", True, (255,0,0))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 28)
                    text = textfont.render("멈춘 운석과 U.F.O 둘다 격추시키지 않고 게임을 진행하면", True, (255,0,0))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+50)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    textfont = pygame.font.Font('NanumGothic.ttf', 28)
                    text = textfont.render("미션을 클리어해도 실패한 것으로 간주되니 꼭 멈춘 운석과 U.F.O를 파괴하세요.", True, (255,0,0))
                    textpos = text.get_rect()
                    textpos.center = (padWidth/2, padHeight/2+90)
                    gamePad.blit(text, textpos)
                    pygame.display.update()
                    sleep(5)


                    rockPassed = rockPassed + 2
                    ufoPassed = ufoPassed + 2
                    ufoSpeed = 0
                    rockSpeed = 0
                    
                            
                    
                    



            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    fighterX = 0

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    fighterY = 0

                    
                    

        drawObject(background, 0, 0)

        x += fighterX
        if x < 0:
            x = 0

        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth        #우주선의 좌, 우 마지노선 위치 지정

        y += fighterY
        if y < 0:
            y = 0

        elif y > padHeight - fighterHeight:
            y = padHeight - fighterHeight      #우주선의 위, 아래 마지노선 위치 지정

#------------------------------------------------------------------------------------------------

        if rockY + rockHeight - 80< y < rockY + rockHeight - 40:
            if(rockX + 30  > x and rockX + 30< x + fighterWidth) or (rockX + rockWidth - 110 > x and rockX + rockWidth < x +fighterWidth):
                crash()

        if ufoY + ufoHeight - 90 < y < ufoY + ufoHeight - 50:
            if(ufoX - 30 > x and ufoX < x - 30  + fighterWidth) or (ufoX + ufoWidth - 10  > x and ufoX + ufoWidth < x +fighterWidth + 100 ):
                crash()

                                                #운석이나 외계인에 충돌하면?

        drawObject(fighter, x, y)
#------------------------------------------------------------------------------------------------

        if diaY + diaHeight - 80 < y < diaY + diaHeight - 40:
            if(diaX - 30 > x and diaX< x  - 30 + fighterWidth) or (diaX + diaWidth - 10> x and diaX+ diaWidth < x +100 +fighterWidth):
                rockPassed -= 2
                
                dia = pygame.image.load(random.choice(diaImage))
                diaSize = dia.get_rect().size
                diaWidth = diaSize[0]
                diaHeight = diaSize[1]

                diaX = random.randrange(0, padWidth - diaWidth)
                diaY = -1000

        if goldY + goldHeight - 80 < y < goldY + goldHeight - 40:
            if(goldX - 30 > x and goldX < x - 30 + fighterWidth) or (goldX + goldWidth - 10> x and goldX + goldWidth < x + 100 + fighterWidth):
                ufoPassed -= 2
                
                gold = pygame.image.load(random.choice(goldImage))
                goldSize = gold.get_rect().size
                goldWidth = goldSize[0]
                goldHeight = goldSize[1]

                goldX = random.randrange(0, padWidth - goldWidth)
                goldY = -1000

        drawObject(fighter, x, y)


#------------------------------------------------------------------------------------------------
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY + 70:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:       #미사일이 운석을 맞출 때
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1


                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY)  != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

                                          
        writeScore2(shotCount + shotCount1)

        rockY += rockSpeed
  
        if rockY > padHeight:                                    #만일 운석과 외계인이 지구에 닿으면 새로운 운석 생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]

            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = -100
            rockPassed += 1
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))

            

        if shotCount1 + shotCount == 30:
            if rockSpeed == 0:
                gameOver1()
            if ufoSpeed == 0:
                gameOver1()
                
            else:
                missionClear()                                        #게임 승리 조건
            
        
        if rockPassed + ufoPassed > 10:                          #게임 오버 조건
            gameOver()

        writePassed(rockPassed)    
       
        
        writePassed2(ufoPassed + rockPassed)
             
        if isShot:
            drawObject(explosion, rockX, rockY)          #isShot
            destroySound.play()

            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]

            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = -100
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot = False

            rockSpeed += 0.4
            if rockSpeed >= 13:
                rockspeed = 13
            if rockSpeed == 0.4:
                rockSpeed = 7
            
           
#------------------------------------------------------------------------------------------------
        if len(missileXY) != 0:
            for i, axy in enumerate(missileXY):
                axy[1] -= 10
                missileXY[i][1] = axy[1]

                if axy[1] < ufoY + 70:
                    if axy[0] > ufoX and axy[0] < ufoX + ufoWidth:       #미사일이 운석을 맞출 때
                        missileXY.remove(axy)
                        isShot1 = True
                        shotCount1 += 1


                if axy[1] <= 0:
                    try:
                        missileXY.remove(axy)
                    except:
                        pass

        if len(missileXY)  != 0:
            for ax, ay in missileXY:
                drawObject(missile, ax, ay)

        writeScore2(shotCount + shotCount1)                                

        ufoY += ufoSpeed
  
        if ufoY > padHeight:                                      #만일 운석과 외계인이 지구에 닿으면 새로운 운석 생성
            ufo = pygame.image.load(random.choice(ufoImage))
            ufoSize = ufo.get_rect().size
            ufoWidth = ufoSize[0]
            ufoHeight = ufoSize[1]
            ufoX = random.randrange(0, padWidth - ufoWidth)
            ufoY = -100
            ufoPassed += 1
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))

     

        if shotCount1 + shotCount == 30:
            if rockSpeed == 0:
                gameOver1()
            if ufoSpeed == 0:
                gameOver1()
                
            else:
                missionClear()                                        #게임 승리 조건
            

        if ufoPassed + rockPassed > 10:                           #게임 오버 조건
            gameOver()

        writePassed1(ufoPassed)    
        

        writePassed2(ufoPassed + rockPassed)
            
        if isShot1:                                               #isShot
            drawObject(explosion, ufoX + 40, ufoY + 40)
            destroySound.play()

            ufo = pygame.image.load(random.choice(ufoImage))
            ufoSize = ufo.get_rect().size
            ufoWidth = ufoSize[0]
            ufoHeight = ufoSize[1]
            ufoX = random.randrange(0, padWidth - ufoWidth)
            ufoY = -100
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot1 = False

            ufoSpeed += 0.4
            if ufoSpeed >= 13:
                ufospeed = 13

            if ufoSpeed == 0.4:
                ufoSpeed = 7
#------------------------------------------------------------------------------------------------
        diaY += diaSpeed
        if diaY > padHeight: 
            dia = pygame.image.load(random.choice(diaImage))
            diaSize = dia.get_rect().size
            diaWidth = diaSize[0]
            diaHeight = diaSize[1]

            diaX = random.randrange(0, padWidth - diaWidth)
            diaY = -1000
           
#-----------------------------------------------------
        goldY += goldSpeed
        if goldY > padHeight:    
            gold = pygame.image.load(random.choice(goldImage))
            goldSize = gold.get_rect().size
            goldWidth = goldSize[0]
            goldHeight = goldSize[1]

            goldX = random.randrange(0, padWidth - goldWidth)
            goldY = -1000
            

#------------------------------------------------------------------------------------------------

        drawObject(rock, rockX, rockY)

        drawObject(ufo, ufoX, ufoY)

        drawObject(dia, diaX, diaY)

        drawObject(gold, goldX, goldY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()

runGame()
            


