#game1 为竞技模式的模块,包含用竞技模式的主函数 game1()
import sys
import pygame
from pygame import *
from draw.initWindow import iniTdraw

'''
游戏界面:
进入游戏:传入一个颜色列表
'''
def game_1(init):
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 760))
    screen.fill(init[0])

    grade = 0
    speed = 0

    button_c = [1, 1, 1, init[1]]
    loop=True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 玩家强制结束游戏
                # todo:保存游戏数据然后再退出:用户名称+当前游戏数据矩阵
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if 40 <= event.pos[0] <= 95 and 5 <= event.pos[1] <= 30:
                    button_c[0] = 0
                else:
                    button_c[0] = 1
                if 105 <= event.pos[0] <= 160 and 5 <= event.pos[1] <= 30:
                    button_c[1] = 0
                else:
                    button_c[1] = 1
                if 170 <= event.pos[0] <= 225 and 5 <= event.pos[1] <= 30:
                    button_c[2] = 0
                else:
                    button_c[2] = 1
                print(event.pos)

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    # todo:完成方块右移动
                    print("2,→/D:右移动")

                if event.key == K_LEFT or event.key == K_a:
                    # todo:完成方块左移动
                    print("1,←/A:左移动")

                if event.key == K_UP or event.key == K_w:
                    # todo:完成方块顺时针旋转
                    print("3,↑/W:顺时针旋转")

                if event.key == K_DOWN or event.key == K_s:
                    # todo:方块向下加速
                    print("4,↓/S:向下加速移动")

                if event.key == K_ESCAPE:
                    # 玩家按下了esc键,退出游戏
                    # todo:保存游戏数据然后再退出:用户名称+当前游戏数据矩阵
                    print("玩家按下了esc键,保存游戏")
                    # pygame.event.post(pygame.event.Event(QUIT))
                    loop=False
        iniTdraw(screen, button_c, grade)

        # 测试:方块下落----------------------------------------------------------------
        pygame.draw.rect(screen, (255, 255, 255), (120, 80 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 120 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 160 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 200 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 240 + speed * 40, 40, 40))
        pygame.draw.line(screen, (0, 0, 0), (120, 80 + 40 + speed * 40), (160, 80 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 120 + 40 + speed * 40), (160, 120 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 160 + 40 + speed * 40), (160, 160 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 200 + 40 + speed * 40), (160, 200 + 40 + speed * 40), 1)

        speed += 0.05
        pygame.display.update()
        fpsClock.tick(100)
