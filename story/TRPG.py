class Character:
    def __init__(self, name, race, gender, background, character_class, stats, skills, equipment, backstory, allies=[]):
        self.name = name
        self.race = race
        self.gender = gender
        self.background = background
        self.character_class = character_class
        self.stats = stats
        self.skills = skills
        self.equipment = equipment
        self.backstory = backstory
        self.allies = allies
    
    def add_ally(self, new_ally):
        self.allies.append(new_ally)
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Gender: {self.gender}")
        print(f"Background: {self.background}")
        print(f"Class: {self.character_class}")
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat}: {value}")
        print("Skills:")
        for skill in self.skills:
            print(f"  {skill}")
        print("Equipment:")
        for item in self.equipment:
            print(f"  {item}")
        print(f"Backstory: {self.backstory}")
        if self.allies:
            print("Allies:")
            for ally in self.allies:
                print(f"  {ally}")

# 기존 Nathan의 캐릭터 시트
nathan_stats = {
    "Strength": 11,
    "Dexterity": 16,
    "Constitution": 14,
    "Intelligence": 13,
    "Wisdom": 11,
    "Charisma": 15
}

nathan_skills = ["Acrobatics", "Stealth", "Perception", "Deception", "Performance"]

nathan_equipment = ["2 Daggers", "Shortbow and Arrows", "Thieves' Tools", "Lute", "Traveling Gear"]

nathan_backstory = (
    "Nathan is from the slums and learned thieving skills to survive. "
    "He poses as a bard, spreading the tales of the poor through his songs. "
    "His parents have passed away, and he takes care of his younger sister. "
    "His dream is to see the ends of the world and gather interesting stories to share with his sister."
)

nathan_allies = ["Bandit Leader and his group"]

nathan = Character(
    name="Nathan",
    race="Human",
    gender="Male",
    background="Criminal (Rogue)",
    character_class="Rogue (disguised as Bard)",
    stats=nathan_stats,
    skills=nathan_skills,
    equipment=nathan_equipment,
    backstory=nathan_backstory,
    allies=nathan_allies
)

# 새로운 동맹 추가
new_ally = "Village Elder and her advisors"
nathan.add_ally(new_ally)

# 시트 업데이트 후 출력
print("Updated Character Sheet:")
nathan.display()
