from time import sleep

testing = True

cookies: int = 0
buildings_owned: dict[str, int] = {"Grandma": 0, "Placeholder": 0}

def cookieTap(buildings_owned: dict[str, int], click: int, mult: float):
    building_amount: int = 0
    for key, value in buildings_owned.items():
        print(key, value)
        building_amount += value 

    return int((click + building_amount) * mult)

def openShop(buildings: dict[str, int], cookies):
    print("Shop:")
    print("1. Grandma -> 100 cookies")
    print("2. Placeholder -> 1 cookies")

    checkout = 0

    user_selection: str = input("Enter a number >>> ")
    
    match user_selection:
        case "1":
            if cookies >= 100:
                print(f"{buildings["Grandma"]} -> {buildings["Grandma"] + 1}")
                buildings["Grandma"] += 1
                checkout -= 100
            else:
                print("Not enough cookies...")
        case "2":
            print(buildings["Grandma"])
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
                print("Shop executed")
                cookies += openShop(buildings_owned, cookies)
            case "quit":
                exit()
            case "list":
                print("List executed")
            case _:
                print("???")

if __name__ == "__main__":
    main()

