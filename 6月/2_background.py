# 배경 이미지 넣기
import os                                 # 파일 위치 반환기능
import pygame

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

# 현재 2_backgorund.py의 위치를 반환시켜서 위치값을 current_path에 넣어둠
current_path = os.path.dirname(__file__) 
# 이제 2_background.py와 같은 경로에 배경이미지 불러오기
background = pygame.image.load(os.path.join(current_path, "background.png"))


# 게임의 반복실행
running = True
while running:
    clock.tick(30)                      # FPS 속도 고정
    for event in pygame.event.get():    # 이벤트 받아오기
        if event.type == pygame.QUIT:   # 만일 받아온 이벤트가 종료라면
            running = False             # 러닝에 펄스를 줘서 반복문종료

    screen.blit(background, (0,0))      # 화면 맨왼쪽 맨위로 부터 그림
    pygame.display.update()             # 배경 그린걸 업데이트 해줘야됨
pygmae.quit()                           # 반복문 종료 되면 파이겜 종료
