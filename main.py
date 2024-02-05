import random
from wall import Wall
from bullet import Bullet

def main():
    battlefield = Wall(20, 10)
    tank1_x = random.randint(0, battlefield.width // 2)
    tank1_y = random.randint(0, battlefield.height)
    tank2_x = random.randint(battlefield.width // 2, battlefield.width - 1)
    tank2_y = random.randint(0, battlefield.height)
    bullets = []

    while True:
        battlefield.draw_field(tank1_x, tank1_y, tank2_x, tank2_y, bullets)

        action1 = input("Player 1 - Choose an action (w, a, s, d to move, t to shoot): ")
        if action1 == "w" and tank1_y > 0:
            tank1_y -= 1
        elif action1 == "s" and tank1_y < battlefield.height - 1:
            tank1_y += 1
        elif action1 == "a" and tank1_x > 0:
            tank1_x -= 1
        elif action1 == "d" and tank1_x < battlefield.width // 2 - 1:
            tank1_x += 1
        elif action1 == "t":
            new_bullet = Bullet(tank1_x, tank1_y, "d")
            bullets.append(new_bullet)

        # Bullet movement and removal logic
        bullets = [b for b in bullets if 0 <= b.x < battlefield.width and 0 <= b.y < battlefield.height]
        for bullet in bullets:
            bullet.move()

        action2 = input("Player 2 - Choose an action (w, a, s, d to move, t to shoot): ")
        if action2 == "w" and tank2_y > 0:
            tank2_y -= 1
        elif action2 == "s" and tank2_y < battlefield.height - 1:
            tank2_y += 1
        elif action2 == "a" and tank2_x > battlefield.width // 2:
            tank2_x -= 1
        elif action2 == "d" and tank2_x < battlefield.width - 1:
            tank2_x += 1
        elif action2 == "t":
            new_bullet = Bullet(tank2_x, tank2_y, "a")
            bullets.append(new_bullet)

if __name__ == "__main__":
    main()
