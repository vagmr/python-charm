import random

ATTACK = 1

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.hand = []
        self.field = []

    def draw(self):
        card = deck.pop()
        self.hand.append(card)
        print(f"{self.name} 抽取了牌：{card.name}")
        if isinstance(card, HealCard):
            self.health += card.heal
            print(f"{self.name} 对自己使用了 {card.name}，恢复了 {card.heal} 点生命值")
        elif isinstance(card, DrawCard):
            for i in range(card.draw):
                self.draw()
            print(f"{self.name} 使用了 {card.name}，摸了 {card.draw} 张牌")

    def play_card(self, card_index, target=None):
        card = self.hand.pop(card_index)
        if isinstance(card, DamageCard):
            if target is None or not isinstance(target, Player):
                print("需要选择目标玩家")
            else:
                damage = card.damage - target.defense
                if damage < 0:
                    damage = 0
                target.health -= damage
                print(f"{self.name} 对 {target.name} 使用了 {card.name}，造成了 {damage} 点伤害")
        elif isinstance(card, DefenseCard):
            self.field.append(card)
            print(f"{self.name} 使用了 {card.name}，获得了 {card.defense} 点防御力")
        elif isinstance(card, DiscardCard):
            if target is None or not isinstance(target, Player):
                print("需要选择目标玩家")
            else:
                target.discard()
                print(f"{self.name} 对 {target.name} 使用了 {card.name}，让其弃掉了一张手牌")
        self.field.append(card)
    
    def discard(self):
        card_index = random.randint(0, len(self.hand) - 1)
        card = self.hand.pop(card_index)
        print(f"{self.name} 弃掉了一张牌：{card.name}")
        
    @property
    def defense(self):
        return sum([card.defense for card in self.field if isinstance(card, DefenseCard)])

class Card:
    def __init__(self, name):
        self.name = name
        
class DamageCard(Card):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

class DefenseCard(Card):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense

class HealCard(Card):
    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal

class DrawCard(Card):
    def __init__(self, name, draw):
        super().__init__(name)
        self.draw = draw

class DiscardCard(Card):
    def __init__(self, name):
        super().__init__(name)
class AnotherPlayerAI:
    def __init__(self):
        self.current_state = 'idle'
        self.target = None

    def choose_action(self, player, enemies):
        if self.current_state == 'idle':
            # 如果当前处于空闲状态，随机选择一个敌人作为目标并进入攻击模式
            self.target = random.choice(enemies)
            print('Another player chooses to attack', self.target)
            self.current_state = 'attack'

        elif self.current_state == 'attack':
            # 如果当前处于攻击状态，继续攻击目标敌人
            if self.target in enemies:
                print('Another player continues to attack', self.target)
            else:
                # 如果目标敌人已经死亡，重新进入空闲状态
                print('Target enemy has been defeated. Another player goes back to idle state.')
                self.current_state = 'idle'


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def start(self):
        global deck
        deck = []
        for i in range(5):
            deck.append(DamageCard("普通攻击", 2))
            deck.append(DefenseCard("防御", 2))
            deck.append(HealCard("恢复", 2))
            deck.append(DrawCard("抽牌", 1))
            deck.append(DiscardCard("弃牌"))
        for i in range(5):
            deck.append(DamageCard("火球术", 5))
            deck.append(DefenseCard("铁布衫", 4))
            deck.append(HealCard("治疗术", 8))
            deck.append(DrawCard("探险家", 2))
            deck.append(DiscardCard("诱敌深入"))
        random.shuffle(deck)

        print("游戏开始！")
        while True:
            print(f"当前玩家：{self.current_player.name}")
            self.current_player.draw()
            self.play_turn(self.current_player)
            if self.current_player.health <= 0:
                print(f"游戏结束，{self.current_player.name} 输了！")
                break
            elif all(len(player.field) == 0 and len(player.hand) == 0 for player in [self.player1, self.player2]):
                print("游戏结束，平局！")
                break
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play_turn(self, player):
        while True:
            for i, card in enumerate(player.hand):
                print(f"{i + 1}. {card.name}")
            print(f"{ATTACK}. 攻击")
            print("0. 结束回合")

            try:
                choice = int(input("请选择要出的牌："))
            except ValueError:
                print("无效的输入，请重新选择")
                continue
            
            if choice == 0:
                break
            
            if choice == ATTACK:
                target_choice = int(input("请选择目标玩家（1：对方玩家，2：自己）："))
                if target_choice == 1:
                    target = self.player2 if player == self.player1 else self.player1
                    player.play_card(choice - 1, target)
                else:
                    player.play_card(choice - 1, player)
                    
            elif choice > 0 and choice <= len(player.hand):
                target_choice = int(input("请选择目标玩家（1：对方玩家，2：自己）："))
                if target_choice == 1:
                    target = self.player2 if player == self.player1 else self.player1
                    player.play_card(choice - 1, target)
                else:
                    player.play_card(choice - 1, player)
            else:
                print("无效的输入，请重新选择")
                continue

if __name__ == '__main__':
    player1 = Player("小明")
    player2 = Player("小红")
    game = Game(player1, player2)
    game.start()
