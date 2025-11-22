class Player:

    team_name = "FC Barc"
    num_players = 0

    def __init__(self, name):
        self.name = name

        # code will always be executed when we instantiate an object
        Player.num_players += 1


player1 = Player("farah")
player2 = Player("rusu")

print(f"{player1.name} belongs to {Player.team_name}")
# farah belongs to FC Barc

print(Player.num_players)  # 2
