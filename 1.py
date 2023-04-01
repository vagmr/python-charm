import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480

font = pygame.font.SysFont(None, 30)

def generate_random_name():
    syllables = ['ba', 'be', 'bo', 'bu', 'da', 'de', 'do', 'du', 'ga', 'ge', 'go', 'gu']
    name = ''
    for i in range(random.randint(2, 3)):
        name += random.choice(syllables)
    return name.capitalize()

class Monster:
    MONSTER_TYPES = ['Goblin', 'Mountain Goblin', 'Slime', 'Werewolf']
    def __init__(self, name=None):
        if name is None:
            self.name = generate_random_name()  # 随机生成一个名称
        else:
            self.name = name
        self.monster_type = random.choice(Monster.MONSTER_TYPES)  # 从四种类型中随机选择一种
        if self.monster_type == 'Goblin':
            self.health = 50
            self.max_health = 50
            self.damage = 5
        elif self.monster_type == 'Mountain Goblin':
            self.health = 60
            self.max_health = 60
            self.damage = 7
        elif self.monster_type == 'Slime':
            self.health = 20
            self.max_health = 20
            self.damage = 3
        elif self.monster_type == 'Werewolf':
            self.health = 100
            self.max_health = 100
            self.damage = 15

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.level = 1
        self.experience = 0
        self.required_experience = 15

    def gain_experience(self, experience_points):
        self.experience += experience_points
        while self.experience >= self.required_experience:
            self.level_up()
        
    def level_up(self):
        self.level += 1
        self.experience -= self.required_experience
        self.required_experience *= 3
        self.max_health += 10
        self.health = self.max_health
        self.damage += 2

    def attack(self, target):
        damage = random.randint(1, self.damage)
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        target.take_damage(damage)
        if isinstance(target, Monster) and target.health <= 0:
            experience_earned = random.randint(1, 10)
            self.gain_experience(experience_earned)
            print(f"{self.name} 获得了 {experience_earned} 点经验！当前经验值为 {self.experience}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} 被击败了！")
            return False
        else:
            print(f"{self.name} 受到了 {damage} 点伤害，还剩下 {self.health} 点生命值。")
            return True

class Game:
    def __init__(self, screen):
        self.player_name = input("请输入你的名字：")
        self.player = Character(self.player_name)
        self.monster = Monster()
        self.attack_button_rect = None
        self.quit_button_rect = None
        self.running = True
        self.screen = screen

    def start(self):
        pygame.display.set_caption('冒险游戏')
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.attack_button_rect.collidepoint(pos):
                        self.player.attack(self.monster)
                        if self.monster.health <= 0:
                            print("玩家胜利！")
                            self.running = False
                            break
                        self.monster.attack(self.player)
                        if self.player.health <= 0:
                            print("玩家失败！")
                            self.running = False
                            break
                    elif self.quit_button_rect.collidepoint(pos):
                        print("游戏结束。")
                        self.running = False
                        break

            self.screen.fill((255, 255, 255))

            # 绘制
            player_text = font.render(f"{self.player.name} (Level {self.player.level})", True, (0, 0, 0))
            self.screen.blit(player_text, (20, 20))

            monster_text = font.render(f"{self.monster.name} ({self.monster.monster_type})", True, (0, 0, 0))
            self.screen.blit(monster_text, (screen_width - monster_text.get_width() - 20, 20))

            player_health_bar_width = int(100 * self.player.health / self.player.max_health)
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(20, 50, player_health_bar_width, 10))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(20, 50, 100, 10), 1)

            monster_health_bar_width = int(100 * self.monster.health / self.monster.max_health)
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(screen_width - monster_health_bar_width - 20, 50, monster_health_bar_width, 10))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(screen_width - 120, 50, 100, 10), 1)

            if not self.attack_button_rect:
                attack_button_text = font.render("攻击", True, (0, 0, 0))
                self.attack_button_rect = pygame.Rect(20, screen_height - attack_button_text.get_height() - 20, attack_button_text.get_width(), attack_button_text.get_height())
                pygame.draw.rect(self.screen, (200, 200, 200), self.attack_button_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), self.attack_button_rect, 1)
                self.screen.blit(attack_button_text, (self.attack_button_rect.x, self.attack_button_rect.y))
            if not self.quit_button_rect:
                quit_button_text = font.render("退出", True, (0, 0, 0))
                self.quit_button_rect = pygame.Rect(screen_width - quit_button_text.get_width() - 20, screen_height - quit_button_text.get_height() - 20, quit_button_text.get_width(), quit_button_text.get_height())
                pygame.draw.rect(self.screen, (200, 200, 200), self.quit_button_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), self.quit_button_rect, 1)
                self.screen.blit(quit_button_text, (self.quit_button_rect.x, self.quit_button_rect.y))

            pygame.display.flip()

        pygame.quit()
