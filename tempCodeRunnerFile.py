bullet = Bullet(bullet_x_pos=random_alien.alien_x_pos, bullet_y_pos=random_alien.alien_y_pos , number_of_bullets=1000, is_alien=True)
        bullet.add_bullet(aliens.total_aliens_bullets)
        bullet_was_shot = True
        if bullet_was_shot:
            time_tracker.threshold += random.uniform(0.2, 3.0)
            bullet_was_shot = False