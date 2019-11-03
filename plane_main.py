# coding=gbk

import pygame
from plane_sprites import *

class PlaneGame():
    """�ɻ���ս����Ϸ"""

    def __init__(self):

        print("��Ϸ��ʼ��")

        # 1.������Ϸ�Ĵ���
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2.������Ϸ��ʱ��
        self.clock = pygame.time.Clock()

        # 3.����˽�з���������;�����Ĵ���
        self.__create_sprites()

        # 4.���ö�ʱ���¼� - �����л� 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # ������������;�����
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # �����л��ľ�����
        self.enemy_group = pygame.sprite.Group()

        # ����Ӣ�۵ľ���;�����
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        print("��Ϸ��ʼ������")

        while True:
            # 1.����ˢ��֡��
            self.clock.tick(60)

            # 2.�¼�����
            self.__event_handler()

            # 3.��ײ���
            self.__check_collide()

            # 4.���¡����ƾ�����
            self.__update_sprites()

            # 5.������ʾ
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 1.�ж��Ƿ�Գ���Ϸ
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("�л�����������")

                # �����л�����
                enemy = Enemy()

                # ���л�������ӵ��л�������
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("�����ƶ�������")
        # ʹ�ü����ṩ�ķ�����ȡ���̰��� - ����Ԫ��
        key_pressed = pygame.key.get_pressed()
        # �ж�Ԫ���ж�Ӧ�İ�������ֵ 1
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2

        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2

        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1.�ӵ��ݻٵл�
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2.�л�ײ��Ӣ��
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 3.�ж��б��Ƿ�������
        if len(enemies) > 0:
            # ��Ӣ������
            self.hero.kill()

            # ������Ϸ
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("��Ϸ����")

        pygame.quit()

        exit()

if __name__ == '__main__':

    # ������Ϸ����
    game = PlaneGame()
    # ������Ϸ
    game.start_game()