# cs32-final-project
#CS32 Final Project with Leah and Riley
characters = [
    {
        "name": "Michael Scott",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "management",
        "department_detail": "scranton_management",
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
        "department_detail": "scranton_sales",
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
        "department_detail": "scranton_sales",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Pam Beesly",
        "gender": "female",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": True,
        "role": "reception",
        "department_detail": "scranton_front_desk",
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
        "department_detail": "scranton_accounting",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Kevin Malone",
        "gender": "male",
        "hair": "bald",
        "glasses": False,
        "has_office_romance": True,
        "role": "accounting",
        "department_detail": "scranton_accounting",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Oscar Martinez",
        "gender": "male",
        "hair": "black",
        "glasses": False,
        "has_office_romance": False,
        "role": "accounting",
        "department_detail": "scranton_accounting",
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
        "department_detail": "scranton_sales",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Phyllis Vance",
        "gender": "female",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": False,
        "role": "sales",
        "department_detail": "scranton_sales",
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
        "department_detail": "scranton_sales",
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
        "department_detail": "scranton_temp",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Kelly Kapoor",
        "gender": "female",
        "hair": "black",
        "glasses": False,
        "has_office_romance": True,
        "role": "customer_service",
        "department_detail": "scranton_customer_service",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Toby Flenderson",
        "gender": "male",
        "hair": "brown",
        "glasses": False,
        "has_office_romance": False,
        "role": "hr",
        "department_detail": "scranton_hr",
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
        "department_detail": "scranton_quality_assurance",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Meredith Palmer",
        "gender": "female",
        "hair": "red",
        "glasses": False,
        "has_office_romance": False,
        "role": "supplier_relations",
        "department_detail": "scranton_supplier_relations",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Darryl Philbin",
        "gender": "male",
        "hair": "black",
        "glasses": False,
        "has_office_romance": True,
        "role": "warehouse",
        "department_detail": "warehouse",
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
        "department_detail": "corporate",
        "has_catchphrase": False,
        "season_introduced": 1
    },
    {
        "name": "Holly Flax",
        "gender": "female",
        "hair": "red",
        "glasses": True,
        "has_office_romance": True,
        "role": "hr",
        "department_detail": "scranton_hr",
        "has_catchphrase": False,
        "season_introduced": 4
    }
]

# All possible characteristics we can ask about
question_bank = [
    ("gender", "Is your character male? (yes/no): ", "male"),
    ("glasses", "Does your character wear glasses? (yes/no): ", True),
    ("has_office_romance", "Does your character have an office romance? (yes/no): ", True),
    ("hair", "Does your character have brown hair? (yes/no): ", "brown"),
    ("role", "Does your character work in sales? (yes/no): ", "sales"),
    ("has_catchphrase", "Does your character have a catchphrase? (yes/no): ", True),
    ("department_detail", "Do they work in accounting? (yes/no): ", "scranton_accounting"),
    ("department_detail", "Do they work in HR? (yes/no): ", "scranton_hr"),
    ("department_detail", "Do they work in customer service? (yes/no): ", "scranton_customer_service"),
    ("season_introduced", "Were they introduced in season 1? (yes/no): ", 1),
    ("season_introduced", "Were they introduced in season 3 or later? (yes/no): ", 3),
]

# Filtering function
def filter_characters(characters, attribute, value):
    return [c for c in characters if c[attribute] == value]

# Best questions function
def choose_best_question(remaining, used_questions):
    best_attr = None
    best_score = 0

    for attr, question_text, yes_value in question_bank:
        if attr in used_questions:
            continue

        # count how many values differ
        values = [c[attr] for c in remaining]
        score = len(set(values))  # more variety = better question

        if score > best_score:
            best_score = score
            best_attr = attr

    return best_attr

# Game function
def play_game(characters):
    remaining = characters.copy()
    used_questions = set()

    print("\nThink of a character from The Office!")

    while len(remaining) > 1:

        attr = choose_best_question(remaining, used_questions)

        if not attr:
            break

        # Unpack question_bank
        question_text = None
        yes_value = None

        for a, q, v in question_bank:
            if a == attr:
                question_text = q
                yes_value = v
                break

        used_questions.add(attr)

        answer = input(question_text).strip().lower()

        if answer == "yes":
            remaining = filter_characters(remaining, attr, yes_value)
        elif answer == "no":
            remaining = [c for c in remaining if c[attr] != yes_value]
        else:
            print("Please answer yes or no.")
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
