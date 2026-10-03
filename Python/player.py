class Player: 
    name = ''
    matches = ''
    runs =''

    def set_stats(self, name, matches, runs):
        self.name = name
        self.matches = matches
        self.runs = runs

    def show_stats(self): 
        print(f'NAME: {self.name}')
        print(f'MATCHES: {self.matches}')
        print(f'RUNS: {self.runs}')

my_player = Player()
my_player.set_stats('Shakib Al Hasan', 230, 7200)
my_player.show_stats()
