import random

class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.cards = []
        self.is_ai = is_ai

    def draw_card(self, deck):
        card = deck.pop()
        self.cards.append(card)
        print(f"{self.name} draws a card: {card}")

    def play_a_card(self, game):
        if self.is_ai:
            # AI 选牌逻辑
            valid_cards = game.get_valid_cards(self)
            if valid_cards:
                card = random.choice(valid_cards)
                self.cards.remove(card)
                print(f"{self.name} plays a card: {card}")
                return card
            else:
                print(f"{self.name} has no valid cards to play.")
                return None
        else:
            # 玩家手动选牌
            while True:
                card = input(f"Please choose a card to play, {self.name}: ")
                if card in self.cards and game.is_valid_card(card, self):
                    self.cards.remove(card)
                    return card
                else:
                    print(f"Invalid card choice, {self.name}. Please try again.")

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = self.create_deck()
        self.current_card = None
        self.current_player = 0
        self.direction = 1
        self.game_over = False

    def create_deck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
        deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def start_game(self):
        print("Starting a new game.")
        # 每个玩家抽 7 张牌
        for _ in range(7):
            for player in self.players:
                player.draw_card(self.deck)

        # 第一张牌必须是数字或者 A，不能是 J、Q、K 或者其他特殊牌
        while True:
            self.current_card = self.deck.pop()
            if self.current_card[0] in "23456789A":
                break

        print(f"The starting card is: {self.current_card}")
        print(f"{self.players[self.current_player].name} goes first.")

    def play_game(self):
        self.start_game()

        while not self.game_over:
            current_player = self.players[self.current_player]
            card = current_player.play_a_card(self)

            if card:
                if card == "J":
                    # 如果打出的是 J，改变游戏方向
                    print(f"{current_player.name} plays a reverse card.")
                    self.direction *= -1
                elif card[0] == "2":
                    # 如果打出的是 2，让下一位玩家摸两张牌并跳过一轮
                    print(f"{current_player.name} plays a draw-two card.")
                    next_player = self.get_next_player()
                    next_player.draw_card(self.deck)
                    next_player.draw_card(self.deck)
                    self.current_player = self.get_next_player()
                else:
                    # 普通牌，更新当前牌面
                    self.current_card = card
                    print(f"The current card is now: {self.current_card}")
                    self.current_player = self.get_next_player()
            else:
                # 没有合法牌可出，摸一张牌
                print(f"{current_player.name} draws a card.")
                current_player.draw_card(self.deck)
                self.current_player = self.get_next_player()

            if len(current_player.cards) == 0:
                # 如果当前玩家手牌出完了，游戏结束
                print(f"{current_player.name} wins!")
                self.game_over = True

    def get_next_player(self):
        # 根据游戏方向获取下一位玩家的索引
        next_player = (self.current_player + self.direction) % len(self.players)
        return self.players[next_player]

    def is_valid_card(self, card, player):
        if card[0] == "J":
            # J 可以随意出
            return True
        elif card[0] == self.current_card[0] or card[-1] == self.current_card[-1]:
            # 和当前牌面数字或花色相同的牌可以出
            return True
        elif card[0] == "8":
            # 8 是万能牌，可以随意指定花色
            suit = input(f"Please choose a suit, {player.name}: ")
            if suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
                print(f"{player.name} chooses {suit}.")
                return True
        else:
            return False

    def get_valid_cards(self, player):
        # 获取当前手牌中可以出的所有合法牌
        valid_cards = []
        for card in player.cards:
            if self.is_valid_card(card, player):
                valid_cards.append(card)
        return valid_cards
