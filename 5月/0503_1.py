import pygame # 로딩
import sys    # 종료
import time   # 시간
import random # 랜덤

from pygame.locals import * # 파이게임의 로컬스에 접근해 전부 임폴트

WINDOW_WIDTH = 800 # 창 넓이 값
WINDOW_HEIGHT = 600 # 창 높이 값
GRID_SIZE = 20 # 한칸을 20으로 잡음
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE

WHITE = (255,255,255) # R G B최대값은 하얀색
GREEN = (0 ,50 , 0)
ORANGE = (250, 150, 0)
GRAY = (100,100,100)

# 움직임 x,y 좌표로 준다
UP = (0,-1) # y는 그럼 +1 아닌가 ? pygame 라이브러리에서 이렇게 지정해놓은건가 ?
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

FPS = 10 # 뱀속도

#객체 2개 만들기 뱀 = Python  먹이 = Feed

class Python(object):       # 뱀이 먹이 먹으면서 길어지는 구문
    def __init__(self):     # 파이썬(뱀)을 이닛으로 받고
        self.create()       # 뱀 생성
        self.color = GREEN  # 뱀 색깔
    def create(self):       # 뱀 생성에대해
        self.length = 2     # 뱀 길이 2칸
        self.positions = [((WINDOW_WIDTH/2),(WINDOW_HEIGHT/2))] # 뱀 위치 가운데 생성되게
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT]) # 뱀이 초기에 어디로 움직일찌
    def control(self,xy):   # 뱀 컨트롤
        if(xy[0] * -1, xy[1] * -1) == self.direction: # 뱀이 반대 방향으로 조작되선 안됨
            return # -1 이 self.direction과 값이 같다면 따로 결과를 주지 않는다.
        else:
            self.direction = xy # 아니라면 self.direction에 xy 값을 준다. 반대로 못가게 한거 아니면 좌표값 그냥주면됨
        # 만일 control 함수에 self.direction = xy란거만 넣으면 안되나 ? -> 그럼 뱀이 반대로도 움직이는게 가능해짐
    def move(self):
        cur = self.positions[0] # 뱀의머리
        x,y = self.direction
        new = (((cur[0] + (x*GRID_SIZE)) % WINDOW_WIDTH), ((cur[1]+(y*GRID_SIZE)) % WINDOW_HEIGHT))
        # %즉 나머지를 주게 한이유 : 뱀이 창넘어가면 사라지기 때문에 창넘어가면 반대에서 나오도록 즉 1부터 다시 시작하도록
        if new in self.positions[2:]: # 뱀의 위치 좌표에 몸통이 포함 그럼 죽는다.
            self.create()# 다시 생성시켜서 게임 리셋
        else: # 몸통 안먹었다면
            self.positions.insert(0,new) # 몸통에 추가
            if len(self.positions) > self.length: # 만일 포지션 갯수가 실제 길이보다 클경우
                self.positions.pop() # 포지션에서 가장 뒤에껄 꺼낸다. (머릴만들고 꼬리 지우고 머리 만들고 꼬리지우고  하며 움직이게)
    def eat(self):
        self.length += 1
    def draw(self,surface): # 사각형 모양 그리기
        for p in self.positions:
            draw_object(surface, self.color,p) #draw_object함수 호출

class Feed(object): # 먹이
    def __init__(self):
        self.position = (0,0)
        self.color = ORANGE
        self.create()
    def create(self):
        self.position = (random.randint(0,GRID_WIDTH -1)*GRID_SIZE, random.randint(0,GRID_HEIGHT -1)*GRID_SIZE)#먹이 랜덤생성
    def draw(self,surface): # 먹이를 그려주는 부분 하부에 draw_object만들어뒀으니까
        draw_object(surface, self.color, self.position) # draw-object 호출

def draw_object(surface, color, pos): # 사각형 모양을 그리도록
    r = pygame.Rect((pos[0], pos[1]),(GRID_SIZE, GRID_SIZE)) # 사각형은 포지션 0과1에서 그리드를 그려야된다.
    pygame.draw.rect(surface, color, r)

def check_eat(python,feed):# 먹이를 먹었을 경우를 체크필요
    #뱀이 먹이를 먹었다 -> 파이썬의 머리(포지션첫번째 위치) == 먹이의 위치
    if python.positions[0] == feed.position:
        python.eat() # 먹이 먹었으니 먹이가 없어짐
        feed.create() # 먹이 다시 생성해줘

def show_info(length,speed,surface): # 정보창
    font = pygame.font.Font(None,34)
    text = font.render("Length:"+str(length) + "    Speed:" + str(round(speed,2)),1,GRAY) # render->랜더링 speed->나누기2 했었으니까 ,2 round는 반올림 한다는 소리
    pos = text.get_rect()
    pos.centerx = 150
    surface.blit(text,pos)

if __name__ == '__main__': # 내가 현재 작업하는게 메인페이지 일 경우란 뜻
    python = Python() # Python이란 객체 만들기
    feed = Feed() # Feed란 객체 만들기

    pygame.init() # pygame을 초기화
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32) # 창 사이즈
    pygame.display.set_caption('Python Game') # 창 바에 제목
    surface=pygame.Surface(window.get_size()) # 창 위에 게임화면(Surface)을 겹치게 윈도우 800 600 싸이즈와 같이해서 놓을거임
    surface=surface.convert() # 컨버트해줘야됨
    surface.fill(WHITE) # 게임 화면 채우기는 하얀색으로
    clock = pygame.time.Clock() # 게임이니까 시간이용해야함
    pygame.key.set_repeat(1, 40) # 키의 repeat값을 정의
    window.blit(surface,(0,0)) # 윈도우의 blit으로 비트연산통한 화면구성

while True:

    for event in pygame.event.get(): # 이벤트가져와라
        if event.type == QUIT: # 만일 이벤트 타입이 QUIT라면 종료해
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN: # 그게 아니고 KEYDOWN 즉 키보드가 눌렸다면
            if event.key == K_UP:
                python.control(UP)
            elif event.key == K_DOWN:
                python.control(DOWN)
            elif event.key == K_LEFT:
                python.control(LEFT)
            elif event.key == K_RIGHT:
                python.control(RIGHT)
    
    surface.fill(WHITE)
    python.move() # 파이썬이 움직일때 
    check_eat(python,feed) # 먹이를 먹었을 경우
    speed = (FPS + python.length) / 2  #먹이 먹었다면 길이 늘어나면서 스피드 UP (스피드임의조절위해서 /2)
    python.draw(surface)
    feed.draw(surface)
    show_info(python.length,speed,surface) #먹이를 먹고나서 정보창이 수정되야되기 때문에 이자리에 둠
    window.blit(surface,(0,0))
    pygame.display.flip() # 플립 해줘야됨
    pygame.display.update() # 업데이트 해줘야됨
    clock.tick(speed) # 스피드를 틱에 반영시킴
    

#------------------준비 끝-----------------------------------------------------------------#
