# coding=gbk

import pygame

# ��Ϸ�ĳ�ʼ��
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

# ����ʱ�Ӷ���
clock = pygame.time.Clock()

# ��Ϸѭ������ζ����Ϸ����ʽ��ʼ
i = 0
while True:

    # ����ָ��ѭ�����ڲ��Ĵ���ִ�е�Ƶ��
    clock.tick(60)

    print(i)

    i += 1
    pass

pygame.quit()