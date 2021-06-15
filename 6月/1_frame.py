# 프레임 만들기

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

# 게임의 반복실행
running = True
while running:
    clock.tick(30)                      # FPS 속도 고정
    for event in pygame.event.get():    # 이벤트 받아오기
        if event.type == pygame.QUIT:   # 만일 받아온 이벤트가 종료라면
            running = False             # 러닝에 펄스를 줘서 반복문종료
pygmae.quit()                           # 반복문 종료 되면 파이겜 종료




