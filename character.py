class The7thSeaCharacter(object):
    def __init__(self):
        self.traits = {
            'Brawn': 2,
            'Finesse': 2,
            'Resolve': 2,
            'Wits': 2,
            'Panache': 2
        }
        self.trait_points_to_spend = 3
        self.nationality = None
        self.skills = {}
        self.skill_points_to_spend = 20
        self.backgrounds = {}
        self.quirks = {}
        self.arcana = {}
        self.dueling = {}
        self.sorcery = {}
        self.advantages = {}
        self.advantage_points_to_spend = 5
        self.reputations = []
        self.wealth = 0

    def increment_trait(self, trait):
        self.traits[trait] += 1
        self.trait_points_to_spend -= 1

    def decrement_trait(self, trait):
        if self.traits[trait] > 2:
            self.traits[trait] -= 1
        self.trait_points_to_spend += 1

    def increment_skill(self, skill):
        if skill in self.skills.keys():
            self.skills[skill] += 1
        else:
            self.skills[skill] = 1
        self.skill_points_to_spend -= 1

    def decrement_skill(self, skill):
        if skill in self.skills.keys():
            if self.skills[skill] != 0:
                self.skills[skill] -= 1
            self.skill_points_to_spend += 1

    def set_name(self, name):
        self.name = name

    def set_player(self, player):
        self.player = player

    def set_religion(self, religion):
        self.religion = religion

    def add_advantage(self, advantage, points):
        if advantage not in self.advantages.keys():
            self.advantages.update({advantage: 1})
        elif advantage in self.advantages.keys() and advantage.lower() == 'sorcery':
            self.advantages[advantage] += 1
        self.advantage_points_to_spend -= points

    def remove_advantage(self, advantage, points):
        if advantage in self.advantages.keys() and advantage.lower() == 'sorcery' and self.advantages[advantage] > 1:
            self.advantages[advantage] -= 1
            self.advantage_points_to_spend += points
        else:
            popped = self.advantages.pop(advantage, None)
            if popped:
                self.advantage_points_to_spend += points

    def set_nationality(self, nationality):
        self.nationality = nationality

    def add_reward(self, steps, reward):
        pass
