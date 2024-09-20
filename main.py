from random import choice

attacks = [
    {"name": "smack", "damage":10},
    {"name": "tickle", "damage":1},
]

print("Battle Brightbulb")

name = input("Who are you?")

player = {
    "hp": 100,
}
opponent = {
    "hp": 100,
}

def battle():
    while True:
        print(f"{name} has {player['hp']} hp.")
        print(f"Opponent has {opponent['hp']} hp.")
        for i, attack in enumerate(attacks):
            print(f"{i}. {attack['name']} ({attack['damage']} damage)")
            
        attack_num = int(input("Select your attack"))
        attack = attacks[attack_num]
        
        opponent_attack = choice(attacks)

        print(f"You chose {attack['name']}.")
        print(f"Opponent chose {opponent_attack['name']}.")
        player["hp"] = player["hp"] - opponent_attack["damage"]
        opponent["hp"] = opponent["hp"] - attack["damage"]
        
        if player["hp"] <= 0:
            print("You are literally fainted")
            break
            
        if opponent["hp"] <= 0:
            print("I guess you win?")
            break

while True:
    ready = "I'm scared"
    while ready.lower() != "yes":
        ready = input("Are you ready to battle?")
    battle()