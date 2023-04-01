import pygame
from random import randint

pygame.init()

screen_width = 640
screen_height = 480

font = pygame.font.SysFont(None, 30)

def generate_random_name():
    syllables = ['ba', 'be', 'bo', 'bu', 'da', 'de', 'do', 'du', 'ga', 'ge', 'go', 'gu']
    name = ''
    for i in range(randint(2, 3)):
        name += randint.choice(syllables)
    return name.capitalize()

class Entity:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 10
        
    def attack(self, target):
        damage = randint.randint(1, self.damage) # 随机伤害值
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} 被击败了！")
            return False
        else:
            print(f"{self.name} 受到了 {damage} 点伤害，还剩下 {self.health} 点生命值。")
            return True


class Monster(Entity):
    MONSTER_TYPES = ['Goblin', 'Mountain Goblin', 'Slime', 'Werewolf']
    
    def __init__(self, name=None):
        if name is None:
            self.name = generate_random_name() # 随机生成名字
        else:
            self.name = name
        
        self.monster_type = randint.choice(Monster.MONSTER_TYPES) # 随机生成类型
        
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
            
    def attack(self, target):
        damage = randint.randint(1, self.damage) # 随机伤害值
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        
        if isinstance(target, Character):
            target.take_damage(damage)
        else:
            self.take_damage(damage)


class Character(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.experience = 0
        self.required_experience = 15

    def gain_experience(self, experience_points):
        self.experience += experience_points
        while self.experience >= self.required_experience: # 判断是否升级
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.required_experience
        self.required_experience *= 3
        self.max_health += 10
        self.health = self.max_health
        self.damage += 2

    def attack(self, target):
        if isinstance(target, Monster) and target.health <= 0:
            experience_earned = randint.randint(1, 10) # 获得随机经验值
            self.gain_experience(experience_earned)
            print(f"{self.name} 获得了 {experience_earned} 点经验！当前经验值为 {self.experience}")
        
        super().attack(target)

        if isinstance(target, Monster) and target.health <= 0:
            print(f"{self.monster.name} 被击败了！")


class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 30)
        self.clock = pygame.time.Clock()
        self.width = 800
        self.height = 600
        self.player = None
        self.monster = None
        self.game_state = "menu"
        self.screen = pygame.display.set_mode((self.width, self.height)) # 添加这一行
        pygame.display.set_caption("Monster Hunter") # 添加这一行

    # ...

    
    def generate_monster(self):
        self.monster = Monster()
        print(f"出现了一只 {self.monster.monster_type}，它的名字叫做 {self.monster.name}！")
        
    def show_start_screen(self):
        text = self.font.render("Click to start", True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2))
        
    def show_start_screen(self):
        pygame.display.set_visible(True) # 添加这一行
        text = self.font.render("Click to start", True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2))

    def show_game_screen(self):
        pygame.display.set_visible(True) # 添加这一行
        monster_image = pygame.image.load('monster.png')
        player_image = pygame.image.load('player.png')
    
    # 绘制怪物和角色
        self.screen.blit(monster_image, (self.width // 2 - monster_image.get_width() // 2, self.height // 3 - monster_image.get_height() // 2))
        self.screen.blit(player_image, (self.width // 2 - player_image.get_width() // 2, self.height * 2 // 3 - player_image.get_height() // 2))
    
    # 绘制信息文本
        level_text = self.font.render(f"Level: {self.player.level}", True, (255, 255, 255))
        exp_text = self.font.render(f"Experience: {self.player.experience}/{self.player.required_experience}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.player.health}/{self.player.max_health}", True, (255, 255, 255))
        monster_text = self.font.render(f"{self.monster.monster_type}: {self.monster.health}/{self.monster.max_health}", True, (255, 255, 255))
    
        self.screen.blit(level_text, (10, 10))
        self.screen.blit(exp_text, (10, 50))
        self.screen.blit(health_text, (10, 90))
        self.screen.blit(monster_text, (self.width - monster_text.get_width() - 10, 10))
    
    # 绘制攻击按钮
        attack_text = self.font.render("ATTACK", True, (255, 255, 255))
        attack_rect = attack_text.get_rect(bottomright=(self.width - 10, self.height - 10))
        pygame.draw.rect(self.screen, (255, 0, 0), attack_rect, 2)
        self.screen.blit(attack_text, attack_rect.move(-attack_text.get_width(), -attack_text.get_height()))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = "quit"
            elif event.type == pygame.MOUSEBUTTONUP and self.game_state == "menu":
                self.start_game()
            elif event.type == pygame.MOUSEBUTTONUP and self.game_state == "game":
                self.player.attack(self.monster)
                if self.monster.health <= 0:
                    print(f"{self.monster.name} 被击败了！")
                    self.generate_monster()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_state = "menu"
        
    def start_game(self):
        self.player = Character("Player")
        self.generate_monster()
        self.game_state = "game"
    def run(self):
        print("Game is running") 
        while self.game_state != "quit":
            self.handle_events()
            self.screen.fill((0, 0, 0))
                
            if self.game_state == "menu":
                self.show_start_screen()
            elif self.game_state == "game":
                self.show_game_screen()
                    
        pygame.display.flip() # 更新屏幕
        self.clock.tick(60) # 限制帧率

        pygame.quit()
        game = Game()
        game.start()
        


