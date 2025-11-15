'''Mini-Profile generator'''

CURRENT_YEAR: int = 2025


def calculate_age(birth_year:int) -> int:
    """Calculates user's age.

    Args:
        birth_year (int): Year of birth.

    Returns:
        int: Age.
    """


    return CURRENT_YEAR - birth_year


def generate_profile(age:int) -> str:
    """Determines the user's life-stage.

    Args:
        age (int): Age.

    Returns:
        str: life-stage.
    """
    if (age >= 0 and age <= 12):
        return 'Child'
    if (age >= 13 and age <= 19):
        return 'Teenager'
    if (age >= 20):
        return 'Adult'


def main ():

    user_name: str
    birth_year_str: str
    birth_year: int
    current_age: int
    life_stage: str
    hobbies: list = []
    user_input: str
    user_profile: dict = {}

    print("Hello, User!")

    print("Enter your full name: ")
    user_name = input()

    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = calculate_age(birth_year)
    life_stage = generate_profile(current_age)

    print("Enter a favourite hobby or type 'stop' to finish: ")
    user_input = input()
    while user_input != 'stop':
        hobbies.append(user_input)
        print("Enter a favourite hobby or type 'stop to finish: ")
        user_input = input()

    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }

    # displaying all the info
    print('---')
    print('Profile summary: ')
    print(f'Name: {user_profile["name"]}')
    print(f'Age: {user_profile["age"]}')
    print(f'Life Stage: {user_profile["stage"]}')

    if (not user_profile["hobbies"]):
        print("You didn't mention any hobbies.")
    else:
        print(f"Favourite Hobbies ({len(user_profile['hobbies'])}): ")
        for hobby in user_profile["hobbies"]:
            print(f'- {hobby}')
    print('---')


main()
