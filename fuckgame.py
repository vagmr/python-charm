import pygame
import random

pygame.init()

# 设置窗口大小和标题
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("回合制游戏")

# 设置字体
pygame.font.init()
font = pygame.font.SysFont('SimHei', 24)

# 定义玩家和怪物的类
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, target):
        damage = random.randint(1, self.damage)
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} 已经被打败了！")

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        damage = random.randint(1, self.damage)
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} 已经被打败了！")

# 定义主类和 GUI 函数
class Game:
    def __init__(self, player_name):
        self.player = Character(player_name)
        self.monster = Monster("哥布林", 50, 5)
        self.running = False
        self.attack_button_rect = None

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    # 检测攻击按钮的点击事件
                    if self.attack_button_rect.collidepoint(pos):
                        self.player.attack(self.monster) # 玩家对怪物造成伤害
                        if self.monster.health <= 0:
                            print("玩家胜利！")
                            self.running = False
                            break
                        self.monster.attack(self.player) # 怪物对玩家造成伤害
                        if self.player.health <= 0:
                            print("怪物胜利！")
                            self.running = False
                            break

            # 更新屏幕内容
            screen.fill((255, 255, 255))
            player_health_text = font.render(f"玩家: {self.player.health}", True, (0, 0, 0))
            monster_health_text = font.render(f"{self.monster.name}: {self.monster.health}", True, (0, 0, 0))
            screen.blit(player_health_text, (10, 10))
            screen.blit(monster_health_text, (10, 40))

            # 绘制攻击按钮和文本
            attack_button_text = font.render("攻击", True, (255, 255, 255))
            attack_button_width = attack_button_text.get_width() + 20
            attack_button_height = attack_button_text.get_height() + 10
            attack_button_x = (screen_width - attack_button_width) // 2
            attack_button_y = (screen_height - attack_button_height) // 2 + 50
            self.attack_button_rect = pygame.Rect(attack_button_x, attack_button_y, attack_button_width, attack_button_height)
            pygame.draw.rect(screen, (0, 0, 255), self.attack_button_rect)
            screen.blit(attack_button_text, (attack_button_x + 10, attack_button_y + 5))

            pygame.display.flip()

    def play(self):
        # 在这里添加游戏逻辑
        pass

def GUI():
    game_instance = Game("玩家")
    game_instance.start()

# 启动游戏
GUI()
