from time import sleep

testing: bool = False

cookies: int = 0
buildings_owned: dict[str, int] = {"Clicker": 0, "Grandma": 0}
click_delay: float = 0.5

def openLog(buildings_owned: dict[str, int]):
    print()
    for key, value in buildings_owned.items():
        print(f"{key}: {value}")
        sleep(0.5)

def cookieTap(buildings_owned: dict[str, int], click: int, mult: float):
    building_amount: int = 0
    for key, value in buildings_owned.items():
        match key:
            case "Clicker":
                building_amount += value * 1
            case "Grandma":
                building_amount += value * 5
            case _:
                pass

    sleep(click_delay)
    return int((click + building_amount) * mult)

def openShop(buildings: dict[str, int], cookies: int):
    print("Shop:")
    print("1. Clicker -> 15 cookies")
    print("2. Grandma -> 100 cookies")

    checkout = 0

    user_selection: str = input("Enter a number >>> ")
    
    match user_selection:
        case "1":
            if cookies >= 15:
                print(f"{buildings["Clicker"]} -> {buildings["Clicker"] + 1}")
                buildings["Clicker"] += 1
                checkout -= 15
            else:
                print("Not enough cookies...")
        case "2":
            if cookies >= 100:
                print(f"{buildings["Grandma"]} -> {buildings["Grandma"] + 1}")
                buildings["Grandma"] += 1
                checkout -= 100
            else:
                print("Not enough cookies...")
        case _:
            print("Invalid command...")

    return checkout

def main():
    global cookies
    global buildings_owned

    if not testing:
        print("Welcome to Cookie Tapper!\n")
        print("Loading", end="", flush=True)

        sleep(1)
        print(".", end="", flush=True)

        sleep(1)
        print(".", end="", flush=True)

        sleep(1)
        print(".", end="", flush=True)

        sleep(2)
    else:
        pass

    while True:
        print(f"\nYou have {cookies} cookies")
        user_input: str = input("Press ENTER >>> ")

        match user_input:
            case "":
                cookies += cookieTap(buildings_owned, 1, 1)
            case "shop":
                print()
                cookies += openShop(buildings_owned, cookies)
            case "quit":
                print("\nGoodbye!")
                sleep(click_delay)
                exit()
            case "log":
                openLog(buildings_owned)
            case _:
                print("???")

if __name__ == "__main__":
    main()

