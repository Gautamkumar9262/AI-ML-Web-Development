Character = [
    "Narendra Modi",
    "Elon Musk",
    "Ajay Devgn",
    "Virat Kohli",
    "Sundar Pichai",
    "Ratan Tata",
    "Deepika Padukone",
    "Salman Khan",
    "Priyanka Chopra",
    "Amitabh Bachchan"
]

Action = [
    "launches",
    "criticizes",
    "invests in",
    "wins",
    "announces",
    "collaborates on",
    "reveals",
    "supports",
    "challenges",
    "celebrates"
]

Object = [
    "a new tech startup",  
    "a blockbuster movie",
    "a charity initiative",
    "a sports tournament",
    "a space mission",
    "a groundbreaking invention",
    "a global summit",
    "a fashion line",
    "a music album",
    "a social media campaign"
]

import random 

def generate_fake_headline():
        character = random.choice(Character)
        action = random.choice(Action)
        obj = random.choice(Object)
        headline = character + " " + action + " " + obj + "."
        return headline
print("\n-------------------------------------------------------")
print("-------------------------------------------------------\n")
print("Headline:", generate_fake_headline())
print("\n-------------------------------------------------------")
print("-------------------------------------------------------\n")



while True:
        user_input = input("\nDo you want to generate another fake headline" \
        "Yes/No: ").strip().lower()

        if user_input == 'yes':
            print("\n-------------------------------------------------------")
            print("-------------------------------------------------------\n")
            print("Headline:", generate_fake_headline())
            print("\n-------------------------------------------------------")
            print("-------------------------------------------------------\n")
        elif user_input == 'no':
               print("\n*****Thank for your interest Good byy!*****")
               break
        else:
            print("Invalid Input")
        
