import pygame # 파이게임 라이브러리
import sys # 종료시키기 위해서
from time import sleep # 게임시간 관련
import time # 이거도 시간 관련 아닌가?
import random # 운석 떨어지는거 랜덤으로 고르도록

BLACK = (0,0,0)
padWidth = 480 # 패드 넒이 x축
padHeight = 640 # 패드 높이 y축
#운석 이미지
rockImage = ['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
             'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
             'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
             'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
             'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
             'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png']
explosionSound = ['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav']

#게임 메세지 출력 함수
def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('NanumGothic.ttf',80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2,padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()   # 배경 음악 정지
    gameOverSound.play()        # 게임 오버 사운드 재생
    sleep(2)
    pygame.mixer.music.play(-1) # 배경 음악 재생
    runGame()

# 전투기가 운석과 충돌시 메세지 출력 함수
def crash():
    global gamePad
    writeMessage('전투기 파괴!')

# 게임 오버 메세지 보이기 함수
def gameOver():
    global gamePad
    writeMessage('게임 오버!')

# 운석을 맞춘 갯수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20) # 글꼴, 크기
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))
    gamePad.blit(text,(10,0)) # 왼쪽 모서리에 띄우고
# 운석이 화면 아래로 통과한 갯수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20) # 글꼴, 크기
    text = font.render('놓친 운석 수: '+str(count), True, (255, 255, 255))
    gamePad.blit(text,(340,0)) # 오른쪽 위쪽에 띄우고

def drawObject(obj,x,y): # 게임 화면을 그려주는것
    global gamePad # gamePad 글로벌로 가져옴
    gamePad.blit(obj,(x,y)) # 오브젝트를 x,y좌표 위치로부터 그려라, obj,(x,y)가아니라 obj,x,y로하면 안되나?


def initGame(): # 게임 초기화 함수
    global gamePad, clock, background , fighter, missile, explosion, missileSound, gameOverSound # 글로벌 함수로 gamePad와 clock, background 등을 가져옴
    pygame.init() # 파이게임이란 라이브러리 초기화
    gamePad = pygame.display.set_mode((padWidth,padHeight)) # 게임 화면구성
    pygame.display.set_caption("PyShooting") # 창 이름
    background = pygame.image.load('background.png') # 배경그림
    fighter = pygame.image.load('fighter.png') # 전투기 이미지
    missile = pygame.image.load('missile.png') # 미사일 이미지
    explosion = pygame.image.load('explosion.png') # 폭파 이미지
    pygame.mixer.music.load('music.wav')            # 배경음악
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('missile.wav') # 미사일 사운드
    gameOverSound = pygame.mixer.Sound('gameover.wav') # 겜오버 사운드
    clock = pygame.time.Clock() # 시간 걸어줌

def runGame(): # 게임 실제 실행
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound # 글로벌 함수로 gamePad와 clock, background등을 가져옴

    isShot = False # 운석이 미사일 맞았을 때 
    shotCount = 0 # 맞은 갯수 카운트용
    rockPassed = 0 # 놓친 갯수 카운트용

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0] # 비행기 그림 사이즈 넒이
    fighterHeight = fighterSize[1] # 비행기 그림 사이즈 높이 숫자의미는?

    x = padWidth * 0.45 # 넓이에서 0.45 위치
    y = padHeight  * 0.9 #높이에서 0.9 위치
    fighterX = 0 # 비행기 움직임 0

    missileXY = [] # 미사일은 여러개 발사 될거니까 리스트로

    rock = pygame.image.load(random.choice(rockImage)) # 운석 랜덤 선택
    rockSize = rock.get_rect().size # 운석 실제 크기
    rockWidth = rockSize[0]
    rockHeight =  rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound)) # explosionSound 에서 랜덤 으로 폭파소리재생
    
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2 # 이거 나중에 운석 스피드값으로 줄거임 y축 2씩 증가 = 2씩 떨어진단말

    onGame = False # onGame 이란걸 False 값으로 둠
    while not onGame: # 각종 이벤트 처리를 위해서,그럼 onGame = False를 두지 말고 그냥 while True:로하면 안되나?
        for event in pygame.event.get(): # 게임 처음할 때는 종료시키는 이벤트밖에 존재 안함
            if event.type in [pygame.QUIT]: # event타입으로 파이게임 창을 닫거나 하면
                pygame.quit() # 파이게임 종료
                sys.exit()  # 시스템 종료 시켜라!

            if event.type in [pygame.KEYDOWN]: # 키가 눌렸다면
                if event.key == pygame.K_LEFT:
                    fighterX -= 5
                elif event.key == pygame.K_RIGHT:
                    fighterX += 5
                elif event.key == pygame.K_SPACE: # 미사일 발사 키 지정
                    missileSound.play()            # 미사일 사운드
                    missileX = x + fighterWidth/2 # 미사일 x좌표(넓이) , 비행기 중간에서 나가게끔하게 하기위해 /2
                    missileY = y - fighterHeight # 미사일 y좌표(높이) 전체y좌표에서 비행기 크기만큼 뺴줌(그래야 비행기에서 나감)
                    missileXY.append([missileX,missileY]) # 아까 미사일 리스트 만들어 논거에 x,y좌표 각각 저장시킴

            if event.type in [pygame.KEYUP]: # 키를 뗀다면 정지시키는 조건문
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0    
            

        gamePad.fill(BLACK) # 게임 화면 블랙

        drawObject(background, 0, 0) # x=0 y=0에 백그라운드를 그려라!
        
        # 전투기 움직임 표현
        x += fighterX # x값에 fighterX의 위치이동값을 더해라
        if x < 0: # 게임 왼쪽으로 끝까지 갔을 경우
            x = 0 # 더이상 못가게 0값줌 x=0은 왼쪽 제일 끝값
        elif x > padWidth - fighterWidth: # 오른쪽 끝가지 갔을 경우
            x = padWidth - fighterWidth # 더이상 오른쪽 못가게

        # 전투기 운석 충돌 체크
        if y < rockY + rockHeight:
            if(rockX > x and rockX < x + fighterWidth) or \
                (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                crash() # 충돌 함수 실행

        drawObject(fighter, x, y) # 비행기 출현 x, y값 위에 지정해뒀으니까

       
        #비행기 그린 후 미사일 그려야 되니까 이위치
        if len(missileXY) != 0: # 미사일의 길이가 0이 아니면
            for i, bxy in enumerate(missileXY): # 미사일요소에 대한 반복
                bxy[1] -= 10 # 미사일의 y좌표 -10(위로이동한다는말)
                missileXY[i][1] = bxy[1] # missileXY의값이 -10만큼 이동된 값이 되야됨

                if bxy[1] < rockY: # 미사일이 운석에 맞은경우 처리
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0: # 미사일이 화면 밖을 벗어나면 
                    try:
                        missileXY.remove(bxy) # 미사일 제거
                    except: # 그외의 사항은 전부 pass
                        pass
        if len(missileXY) != 0: # 미사일이 실제 0이 아니면
            for bx, by in missileXY: # 미사일을 그려주도록 draw함수 호출
                drawObject(missile, bx, by)
        
        writeScore(shotCount) # 운석 맞춘 점수 표시

        rockY += rockSpeed # 운석이 떨어지는 것

        if rockY > padHeight:#바닥으로 운석이 떨어졌다면 생성해야되니까
            rock = pygame.image.load(random.choice(rockImage)) # 운석 랜덤 선택
            rockSize = rock.get_rect().size # 운석 실제 크기
            rockWidth = rockSize[0]
            rockHeight =  rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed += 1 # 운석이 놓치면 +1
        
        if rockPassed == 3: #운석 3개 놓치면 게임오버
            gameOver()
            
        writePassed(rockPassed) # 놓친 운석 수 표시

        if isShot: # 만일 운석이 맞았다면 폭파 그리고 운석생성해라
            drawObject(explosion, rockX, rockY)  # 폭파 이미지
            destroySound.play() # 폭파소리
            #새로운 운석(랜덤)
            rock = pygame.image.load(random.choice(rockImage)) # 운석 랜덤 선택
            rockSize = rock.get_rect().size # 운석 실제 크기
            rockWidth = rockSize[0]
            rockHeight =  rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound)) # 랜덤 폭파소리재생
            isShot = False

            #운석 맞춘경우 속도 증가
            rockSpeed += 0.05
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY) # 운석그림

        pygame.display.update() # 디스플레이 업데이트 해줘야됨

        clock.tick(60) # 초당 프레임수 60

    pygame.quit() # 종료

# 함수실행
initGame()
runGame()
    



