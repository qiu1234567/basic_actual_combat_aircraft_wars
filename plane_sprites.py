# coding=gbk

import random
import pygame

# ��Ļ��С�ĳ���
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# ˢ�µ�֡��
FRAME_PER_SEC = 60
# �����л��Ķ�ʱ������
CREATE_ENEMY_EVENT = pygame.USEREVENT
# Ӣ�۷����ӵ��¼�
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """�ɻ���ս����"""

    def __init__(self, image_name, speed=1):

        # ���ø���ĳ�ʼ������
        super().__init__()

        # ������������
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # ����Ļ�Ĵ�ֱ�����ƶ�
        self.rect.y += self.speed


class Background(GameSprite):
    """��Ϸ��������"""

    def __init__(self, is_alt = False):

        # 1.���ø��෽��ʵ�־���Ĵ�����iamge/rect/speed��
        super().__init__("./images/background.png")

        # 2.�ж��Ƿ�ʽ����ͼ������ǣ���Ҫ���ó�ʼλ��
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.���ø���ķ���ʵ��
        super().update()

        # 2.�ж��Ƿ��Ƴ���Ļ
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """�л�����"""

    def __init__(self):
        pass
        # 1.���ø��෽���������л����飬ͬʱָ���л�ͼƬ
        super().__init__("./images/enemy1.png")

        # 2.ָ���л��ĳ�ʼ����ٶ�
        self.speed = random.randint(1, 3)

        # 3.ָ���л��ĳ�ʼ���λ��
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1.���ø��෽�������ִ�ֱ�����ķ���
        super().update()
        # �ж��Ƿ�ɳ���Ļ������ǣ���Ҫ�Ӿ�����ɾ���л�
        if self.rect.y >= SCREEN_RECT.height:
            # print("�ɳ���Ļ����Ҫ�Ӿ�����ɾ��������")

            # kill�������Խ�����Ӿ��������Ƴ�������ͻᱻ�Զ�����
            self.kill()

    def __del__(self):
        # print("�л����� %s" % self.rect)
        pass


class Hero(GameSprite):
    """Ӣ�۾���"""

    def __init__(self):

        # 1.���ø��෽��������image&speed
        super().__init__("./images/me1.png", 0)

        # 2.����Ӣ�۵ĳ�ʼλ��
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.�����ӵ��ľ�����
        self.bullets = pygame.sprite.Group()

    def update(self):

        # Ӣ����ˮƽ�����ƶ�
        self.rect.x += self.speed

        # ����Ӣ�۲����뿪��Ļ
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("�����ӵ�")

        for i in (0, 1, 2):
            # 1.�����ӵ�����
            bullet = Bullet()

            # 2.���þ����λ��
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3.��������ӵ�������
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """�ӵ�����"""

    def __init__(self):

        # ���ø��෽���������ӵ�ͼƬ�����ó�ʼ�ٶ�
        super().__init__("./images/bullet1.png", -2)



    def update(self):

        # ���ø��෽�������ӵ��ش�ֱ�������
        super().update()

        # �ж��ӵ��Ƿ�ɳ���Ļ
        if self.rect.bottom < 0:
            self.kill()
