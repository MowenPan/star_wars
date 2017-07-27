import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    # print(event.key)
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # print(event.key)
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # print(event.key)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
        # print(event.key)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        # print(event.key)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # print(event.key)
    """响应松开按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # print(event.key)
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        # print(event.key)
    elif event.key == pygame.K_UP:
        ship.moving_up = False
        # print(event.key)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        # print(event.key)


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像并求换到新屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在外星人和飞船后面绘制所有子弹
    for bullet in  bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到限制就发射子弹"""
    # 创建新子弹并加入到bullets编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """# 创建一个外星人，并计算一行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    alailable_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(alailable_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整个外星人下移并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_directions *= -1


def update_aliens(ai_settings, aliens):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
