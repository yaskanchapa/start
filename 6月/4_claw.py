# 집게손 만들기
import os                                 # 파일 위치 반환기능
import pygame

# 보석 클래스 만들기 sprite클래스 사용 이럼으로 써 이 클래스를 사용하면 객체 를 바로바로 만들 수 있음
# Sprite는 게임에서 나타내는 모든 캐릭터, 장애물등을 표현할 때 사용하는 Surface이다.
# 우리가 이전에는 각 캐릭터의 충돌이나 위치등을 모두 직접 계산하는 식을 만들어서 사용하였다. 
# 하지만 Sprite를 사용하면 Sprite 그룹을 만들어서 모두 한꺼번에 움직이게 하거나 Sprite들끼리의 충돌등을 알아낼 수 있다.
# 또한 Sprite를 사용하여 캐릭터가 자연스럽게 움직이는 것을 연출할 수 있다. 물론 이 모든 것들을 Sprite없이도 만들 수 있지만, Sprite를 사용하는 방법을 알아본다.

class Gemstone(pygame.sprite.Sprite):                       # Sprite를 상속받은 클래스를 다룰 것
    def __init__(self, image, position):                    # 일단은 초기화 시켜줌 self는 Sprite를 상속 받아온 것
        super().__init__()                                  # 부모 클래스의 함수도 초기화 하기 위해 super().__init__()사용
        self.image = image                                  # Sprite 함수를 사용하기 위해선 2개의 맴버변수 정의가 필요. 여기선 self.image, self.rect
        self.rect = image.get_rect(center = position)       # 캐릭터의  x,y 정보 (가로,세로 크기) 그래서 __init__(self)에 추가로 image와 position변수를 추가
                                                            # center값은 position값으로 지정

# 보석 만들기 함수
def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0],(200,380))     # gemstone_images의 0 번째 이미지를 (200 , 300) 위치에 생성
    gemstone_group.add(small_gold)                          # 그룹에 추가
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1],(300,500)))# 위의 것을 한 줄로 짜봄
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2],(300,380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3],(900,420)))

# 집게 클래스 만들기
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)                  # 이미지를 집어 넣는 작업임
# 초기화 설정
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Gold Miner")

# FPS값 설정
clock = pygame.time.Clock()

# 배경이미지 불러오기

# 현재 작성중인 코드 파일경로를 current_path에 넣음
current_path = os.path.dirname(__file__) 
# 이제 같은 경로에 배경이미지 불러오기 os.path.join으로 현재 경로엔에 파일 불러오고 pygame.image.load로 이미지 불러오기
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 보석 이미지 불러오기
# 리스트에 이미지 저장
gemstone_images = [
    pygame.image.load(os.path.join(current_path,"small_gold.png")),
    pygame.image.load(os.path.join(current_path,"big_gold.png")),
    pygame.image.load(os.path.join(current_path,"stone.png")),
    pygame.image.load(os.path.join(current_path,"diamond.png"))]

# 보석 그룹 만들기 그룹지정으로인해 한번에 명령이 가능해짐
# 일일히 객체 하나하나 그려달라는 명령 쓰면 너무 코드 길어짐 그래서 그룹에 객채를 모아놓고 한번에 그룹을 그리라고 하면됨
gemstone_group = pygame.sprite.Group()
setup_gemstone()                                  # setup_gmestone 함수 실행

# 집게
claw_image = pygame.image.load(os.path.join(current_path,"claw.png"))
claw = Claw(claw_image, (screen_width//2, 110))   # 가로 화면 절반 그리고 위에서 110정도 위치에 집게 생성

# 이하의 방식은 너무 변수를 많이 설정해야 해서 효율적이지 못함
# character = pygame.image.load(...)
# character_size = character.get_rect().size      # 케릭터 크기는 사각형을 그리는 방식으로
# character_width = character_size[0]             # 케릭터 x값(넓이)는 character_size의 첫번째 값
# character_height = character_size[1]            # 케릭터 x값(넓이)는 character_size의 두번째 값
# character_x_pos = ...character                  # 케릭터의 x 좌표는
# character_y_pos = ...character                  # 케릭터의 x 좌표는



# 게임의 반복실행
running = True
while running:
    clock.tick(30)                      # FPS 속도 고정
    for event in pygame.event.get():    # 이벤트 받아오기
        if event.type == pygame.QUIT:   # 만일 받아온 이벤트가 종료라면
            running = False             # 러닝에 펄스를 줘서 반복문종료

    screen.blit(background, (0,0))      # 화면 맨왼쪽 맨위로 부터 그림
    gemstone_group.draw(screen)         # 그룹 내 모든 sprite를 screen에 그려줘
    claw.draw(screen)
    pygame.display.update()             # 배경 그린걸 업데이트 해줘야됨
pygmae.quit()                           # 반복문 종료 되면 파이겜 종료