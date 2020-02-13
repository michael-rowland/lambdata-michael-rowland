# PLAYER CLASS
# read about scope
class Player():
    def __init__(self, name, number, position, handedness):
        self.name = name
        self.number = number
        self.position = position
        self.handedness = handedness

    # @property
    def position_map(self):
        pmap = {
            1: 'P', 2: 'C', 3: '1B',
            4: '2B', 5: '3B', 6: 'SS',
            7: 'LF', 8: 'CF', 9: 'RF'
            }
        return pmap[self.position]

    def box_score(self):
        return f'{self.name} ({self.handedness}) - #{self.number} - {self.position_map()}'


class Batter(Player):
    def __init__(self, name, number, position, handedness, hits, at_bats):
        super().__init__(name, number, position, handedness)
        self.hits = hits
        self.at_bats = at_bats

    def batting_average(self):
        return self.hits / self.at_bats

    def player_statistics(self):
        print(f'Batting Average: {self.batting_average():.3f}')

    # @staticmethod
    # def advertise_generic():
    #     print(f"Our team has the best players!")

class Pitcher(Player):
    def __init__(self, name, number, position, handedness, wins, starts):
        super().__init__(name, number, position, handedness)
        self.wins = wins
        self.starts = starts

    def win_pct(self):
        return self.wins / self.starts

    def advertise(self):
        print(f'Win Percentage: {self.win_pct()*100:.0f}%')

if __name__ == "__main__":

    players = [
        {'name': 'Byron Buxton', 'number': 25, 'position': 8, 
        'handedness': 'R', 'hits': 100, 'at_bats': 350},
        {'name': 'Max Kepler', 'number': 26, 'position': 9, 
        'handedness': 'L', 'hits': 125, 'at_bats': 350},
        {'name': 'Miguel Sano', 'number': 22, 'position': 3, 
        'handedness': 'R', 'hits': 150, 'at_bats': 350}
    ]
    pitchers = [
        {'name': 'Jose Berrios', 'position': 1, 'number': 17, 
        'handedness': 'R', 'wins': 20, 'starts': 30},
        {'name': 'Lewis Thorpe', 'position': 1, 'number': 43, 
        'handedness': 'L', 'wins': 5, 'starts': 15}
    ]

    for p in players:
        player_b = Batter(name=p['name'], position=p['position'], 
        number=p['number'], handedness=p['handedness'], hits=p['hits'], 
        at_bats=p['at_bats'])
        print(player_b.box_score())
        player_b.player_statistics()
    
    for p in pitchers:
        player_p = Pitcher(name=p['name'], position=p['position'], 
        number=p['number'], handedness=p['handedness'], wins=p['wins'], 
        starts=p['starts'])
        print(player_p.box_score())
        player_p.advertise()
