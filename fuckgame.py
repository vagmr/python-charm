import sys
import pygame
from time import time
from random import randint
from random import choice


class Entity:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 10
        
    def attack(self, target):
        damage = randint(1, self.damage) # 随机伤害值
        print(f"{self.name} 攻击了 {target.name}，造成了 {damage} 点伤害！")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} 被击败了！")
            return False
        else:
            return True



class Character(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.experience = 0
        self.required_experience = 15
        self.attack_interval = 500 # 攻击间隔，单位为毫秒
        self.last_attack_time = 0 # 上次攻击时间，用于计算攻击间隔

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
            experience_earned = randint(1, 10) # 获得随机经验值
            self.gain_experience(experience_earned)
            print(f"{self.name} 获得了 {experience_earned} 点经验！当前经验值为 {self.experience}")
        
        super().attack(target)

        if isinstance(target, Monster) and target.health <= 0:
            print(f"{target.name} 被击败了！")

#============================================================================#

class Monster(Entity):
    MONSTER_TYPES = ['Goblin', 'Mountain Goblin', 'Slime', 'Werewolf']
    
    def __init__(self, name=None):
        if name is None:
            self.name = self.generate_random_name() # 随机生成名字
        else:
            self.name = name
        
        self.monster_type = choice(Monster.MONSTER_TYPES) # 随机生成类型
        
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
        damage = randint(1, self.damage) # 随机伤害值
        
        if isinstance(target, Character):
            target.take_damage(damage)
        else:
            self.take_damage(damage)
    
    def generate_random_name(self):
        syllables = ['Gob','lin', 'Mo','unt','ain','Goblin', 'Slime', 'Wer','ewolf']
        name = ''
        for i in range(randint(2, 3)):
            name += choice(syllables)
        return name.capitalize()

#=========================================================================#
class StartScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # 加载背景图片
        self.background_image = pygame.image.load('start_screen.png').convert()
        
        # 创建字体对象
        self.font = pygame.font.SysFont(None, 50)
        
        # 创建开始按钮矩形
        self.start_button_rect = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2, 200, 50)
        
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        
        # 设置帧率
        self.fps = 60
        
    def run(self, screen):
        while True:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 如果鼠标点击在开始按钮上，结束循环
                    if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                        return
            
            # 绘制背景
            screen.blit(self.background_image, (0, 0))
            
            # 绘制开始按钮
            pygame.draw.rect(screen, (255, 255, 255), self.start_button_rect)
            start_label = self.font.render("start", True, (0, 0, 0))
            screen.blit(start_label, (self.screen_width // 2 - start_label.get_width() // 2, self.screen_height // 2 + 10))
            
            # 更新显示
            pygame.display.flip()
            
            # 控制帧率
            self.clock.tick(self.fps)
#===========================================================================#

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen_width = 800 # 窗口宽度
        self.screen_height = 600 # 窗口高度
        self.bg_color = (255, 255, 255) # 背景色
        self.title = '怪物猎人（vagmr）' # 窗口标题
        
        self.clock = pygame.time.Clock() # 创建时钟对象
        self.fps = 60 # 帧率
        
        self.player = Character('Player') # 创建玩家对象
        self.monsters = [] # 存储怪物列表
        
        for i in range(5):
            self.monsters.append(Monster())
        
        self.font = pygame.font.SysFont(None, 30) # 创建字体对象
        
    def run(self):
        # 创建窗口
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)
        # 显示开始界面
        start_screen = StartScreen(self.screen_width, self.screen_height)
        start_screen.run(screen)
        while True:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down()
            
            # 绘制背景
            screen.fill(self.bg_color)
    def handle_mouse_button_down(self):
        # 获取当前时间
        current_time = time() * 1000
        
        # 判断是否可以攻击
        if current_time - self.player.last_attack_time >= self.player.attack_interval:
            # 更新上次攻击时间为当前时间
            self.player.last_attack_time = current_time
            
            # 随机选择一个怪物进行攻击
            monster = self.monsters[randint(0, len(self.monsters) - 1)]
            
            # 玩家攻击怪物
            self.player.attack(monster)
    
    def update_and_render_entities(self, screen):
        # 绘制玩家角色
        self.render_entity(screen, self.player, self.screen_width // 4, self.screen_height // 2)
        
        # 更新和绘制怪物
        for i in range(len(self.monsters)):
            # 如果怪物已经死亡，从列表中删除
            if not self.update_and_render_entity(screen, self.monsters[i], self.screen_width // 4 * 3, (i + 1) * self.screen_height // 6):
                del self.monsters[i]
                break
    
    def render_entity(self, screen, entity, x, y):
        # 绘制名称
        name_label = self.font.render(entity.name, True, (0, 0, 0))
        screen.blit(name_label, (x, y))
        
        # 绘制生命值条
        health_bar_width = 100
        health_bar_height = 10
        health_bar_x = x
        health_bar_y = y + 30
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width * entity.health // entity.max_health, health_bar_height))
        
    def update_and_render_entity(self, screen, entity, x, y):
        # 如果实体已经死亡，返回 False
        if not entity.take_damage(0):
            return False
        
        # 绘制实体
        self.render_entity(screen, entity, x, y)
        
        # 随机移动实体位置
        if isinstance(entity, Monster):
            if randint(1, 30) == 1:
                offset = randint(-50, 50)
                entity_rect = pygame.Rect(x, y, 100, 40)
                entity_rect.move_ip(offset, 0)
                
                # 不允许怪物移动到玩家角色的位置
                if entity_rect.collidepoint((self.screen_width // 2, self.screen_height // 2)):
                    return True
                
                # 确保怪物不会移出屏幕
                if entity_rect.left < 0:
                    x -= entity_rect.left
                elif entity_rect.right > self.screen_width:
                    x -= entity_rect.right - self.screen_width
                
        return True
    
    def draw_ui(self, screen):
        # 绘制经验条
        exp_bar_width = 100
        exp_bar_height = 10
        exp_bar_x = self.screen_width - exp_bar_width - 20
        exp_bar_y = 20
        pygame.draw.rect(screen, (255, 0, 0), (exp_bar_x, exp_bar_y, exp_bar_width, exp_bar_height))
        pygame.draw.rect(screen, (0, 0, 255), (exp_bar_x, exp_bar_y, exp_bar_width * self.player.experience // self.player.required_experience, exp_bar_height))
        
        # 绘制等级标签
        level_label = self.font.render(f"Level: {self.player.level}", True, (0, 0, 0))
        screen.blit(level_label, (exp_bar_x - 80, exp_bar_y))
    def run(self):
        # 创建窗口
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)
          # 显示开始界面
        start_screen = StartScreen(self.screen_width, self.screen_height)
        start_screen.run(screen)
        
        while True:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down()
            
            # 绘制背景
            screen.fill(self.bg_color)
            
            # 更新和渲染角色和怪物
            self.update_and_render_entities(screen)
            
            # 绘制 UI
            self.draw_ui(screen)
            
            # 更新显示
            pygame.display.flip()
            
            # 控制帧率
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = Game()
    game.run()
