# coding=gbk

import pygame

pygame.init()

# ������Ϸ�Ĵ��� 480 * 700
# set_mode��ʼ����Ϸ���ڣ����ؽ��Ϊsurface
# resolution�����������б�
# flags����ָ����Ļ�ĸ���ѡ����Ƿ�ȫ������Ĭ�ϲ���Ҫ����
# depth������ʾ��ɫ��λ����Ĭ���Զ�ƥ�䡣
screen = pygame.display.set_mode((480, 700))

# ���Ʊ���ͼ��
# 1.����ͼ������
bg = pygame.image.load("./images/background.png")
# 2.blit����ͼ��
screen.blit(bg, (0, 0))
# 3.update������Ļ����ʾ
pygame.display.update()

# ��Ϸѭ��
while True:
    pass

pygame.quit()