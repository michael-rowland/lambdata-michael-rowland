
class Batter(object):
    def __init__(self, name, position, stance, hits, at_bats):
        self.name = name
        self.position = position
        self.stance = stance
        self.hits = hits
        self.at_bats = at_bats

    @property #REVIEW THIS
    def batting_average(self):
        return self.hits / self.at_bats

    @property
    def position_map(self):
        pmap = {
            1: 'P', 2: 'C', 3: '1B',
            4: '2B', 5: '3B', 6: 'SS',
            7: 'LF', 8: 'CF', 9: 'RF'
            }
        return pmap[self.position]

    def player_statistics(self):
        print(f'{self.name}, {self.position_map}, {self.stance}')
        print(f'Batting Average: {self.batting_average:.3f}')

    @staticmethod
    def advertise_generic():
        print(f"Our team has the best players!")

class Pitcher(object):
    def __init__(self, name, position, handedness):
        super().__init__(name, position)
        self.handedness = handedness

    def advertise(self):
        print(f'{self.handedness} Handed Starting Pitcher: {self.name}')

if __name__ == "__main__":

    players = [
        {'name': 'Byron Buxton', 'position': 8, 'stance': 'R', 'hits': 100, 'at_bats': 350},
        {'name': 'Max Kepler', 'position': 9, 'stance': 'L', 'hits': 125, 'at_bats': 350},
        {'name': 'Miguel Sano', 'position': 3, 'stance': 'R', 'hits': 150, 'at_bats': 350}
    ]
    pitchers = [
        {'name': 'Jose Berrios', 'position': 1, 'handedness': 'Right'},
        {'name': 'Lewis Thorpe', 'position': 1, 'handedness': 'Left'}
    ]

    for p in players:
        player = Batter(name=p['name'], position=p['position'], 
        stance=p['stance'], hits=p['hits'], at_bats=p['at_bats'])
        player.player_statistics()
    
    # for p in pitchers:
    #     thrower_of_the_baseball = Pitcher(name=p['name'], position=p['position'], handedness=p['handedness'])
    #     thrower_of_the_baseball.advertise()
