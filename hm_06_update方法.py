# coding=gbk

import pygame

pygame.init()

# ������Ϸ�Ĵ��� 480 * 700
screen = pygame.display.set_mode((480, 700))

# ���Ʊ���ͼ��
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# ����Ӣ�۵ķɻ�
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# ���������л��ƹ������֮��ͳһ����update����
pygame.display.update()

# ��Ϸѭ��
while True:
    pass

pygame.quit()