# coding=gbk

import pygame
from plane_sprites import*

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
screen.blit(hero, (150, 300))

# ���������л��ƹ������֮��ͳһ����update����
pygame.display.update()

# ����ʼ�ն���
clock = pygame.time.Clock()

# 1.����rect��¼�ɻ��ĳ�ʼλ��
hero_rect = pygame.Rect(150, 300, 102, 126)

# �����л��ľ���
enemy = GameSprite("./images/enemy1.png")

# ����������
enemy_group = pygame.sprite.Group(enemy)


# ��Ϸѭ������ζ����Ϸ����ʽ��ʼ
i = 0
while True:

    # ����ָ��ѭ�����ڲ��Ĵ���ִ�е�Ƶ��
    clock.tick(60)

    # �����¼�
    for event in pygame.event.get():

        # �ж��¼������Ƿ�Ϊ�˳��¼�
        if event.type == pygame.QUIT:
            print("��Ϸ����������")

            # ж�����е�ģ��
            pygame.quit()

            # exit()
            exit()

    # 2.�޸ķɻ���λ��
    hero_rect.y -= 1

    # �жϷɻ���λ��
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.����blit��������ͼ��
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # �þ����������������
    # update - �����е����о������λ��
    enemy_group.update()
    # draw - ��screen�ϻ������еľ���
    enemy_group.draw(screen)

    # 4.����update����������ʾ
    pygame.display.update()

pygame.quit()