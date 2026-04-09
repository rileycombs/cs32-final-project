# cs32-final-project
CS32 Final Project with Leah and Riley
characters = [
    {
        "name": "Michael Scott",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "management",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Dwight Schrute",
        "gender": "male",
        "hair": "brown",
        "glasses": True,
        "has_office_romance": True,
        "role": "sales",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Jim Halpert",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "sales",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Pam Beesly",
        "gender": "female",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "reception",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Angela Martin",
        "gender": "female",
        "hair": "blonde",
        "glasses": False,
        "has_office_romance": True,
        "role": "accounting",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Kevin Malone",
        "gender": "male",
        "hair": "bald",
        "glasses": False,
        "has_office_romance": True,
        "role": "accounting",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Oscar Martinez",
        "gender": "male",
        "hair": "black",
        "glasses": False,
        "has_office_romance": False,
        "role": "accounting",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Stanley Hudson",
        "gender": "male",
        "hair": "black",
        "glasses": True,
        "has_office_romance": False,
        "role": "sales",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Phyllis Vance",
        "gender": "female",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": False,
        "role": "sales",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Andy Bernard",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "sales",
        "has_catchphrase": True,
        "season_introduced": 3
    },
    {
        "name": "Ryan Howard",
        "gender": "male",
        "hair": "black",
        "glasses": False,
        "has_office_romance": True,
        "role": "temp",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Kelly Kapoor",
        "gender": "female",
        "hair": "black",
        "glasses": False,
        "has_office_romance": True,
        "role": "customer_service",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Toby Flenderson",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": False,
        "role": "hr",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Creed Bratton",
        "gender": "male",
        "hair": "gray",
        "glasses": False,
        "has_office_romance": False,
        "role": "quality_assurance",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Meredith Palmer",
        "gender": "female",
        "hair": "red",
        "glasses": False,
        "has_office_romance": False,
        "role": "supplier_relations",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Darryl Philbin",
        "gender": "male",
        "hair": "black",
        "glasses": False,
        "has_office_romance": True,
        "role": "warehouse",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Jan Levinson",
        "gender": "female",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "corporate",
        "has_catchphrase": True,
        "season_introduced": 1
    },
    {
        "name": "Holly Flax",
        "gender": "female",
        "hair": "red",
        "glasses": True,
        "has_office_romance": True,
        "role": "hr",
        "has_catchphrase": False,
        "season_introduced": 4
    }
]

# Questions: (currently limited, need to expand)
questions = [
    ("gender", "Is your character male? (yes/no): ", "male"),
    ("glasses", "Does your character wear glasses? (yes/no): ", True),
    ("facial_hair", "Does your character have an office romance? (yes/no): ", True),
    ("hair", "Does your character have brown hair? (yes/no): ", "brown"),
    ("role", "Does your character work in sales? (yes/no): ", "sales"),
    ("has_catchphrase", "Does your character have a catchphrase? (yes/no): ", True),
]

# Filtering function
def filter_characters(characters, attribute, value):
    return [c for c in characters if c[attribute] == value]

# Game function
def play_game(characters):
    remaining = characters.copy()

    print("\nThink of a character from The Office!")
    print("-------------------------------------")

    for attribute, question_text, yes_value in questions:
        if len(remaining) <= 1:
            break

        answer = input(question_text).strip().lower()

        if answer == "yes":
            remaining = filter_characters(remaining, attribute, yes_value)
        elif answer == "no":
            remaining = [c for c in remaining if c[attribute] != yes_value]
        else:
            print("Please answer 'yes' or 'no'.")
            continue

        # Show remaining possibilities
        print("\nRemaining characters:")
        for c in remaining:
            print("-", c["name"])
        print()

    # Final result
    if len(remaining) == 1:
        print(f"I guess your character is {remaining[0]['name']}!")
    elif len(remaining) == 0:
        print("No matching character found. Were your answers consistent?")
    else:
        print("I'm not completely sure. Possible characters:")
        for c in remaining:
            print("-", c["name"])

# Replay loop
while True:
    play_game(characters)
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
