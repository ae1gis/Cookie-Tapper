from time import sleep

testing: bool = False

cookies: int = 0
buildings_owned: dict[str, int] = {"Clicker": 0, "Grandma": 0}
upgrades_owned: dict[str, dict[str, bool | float | str]] = {
    "Clicker MK2": {"owned": False, "mult": 2, "affects": "Clicker"},
    "Grandma MK2": {"owned": False, "mult": 2, "affects": "Grandma"}
}
click_amount: int = 1
universal_mult: float = 0
click_delay: float = 0.5

def openLog(buildings_owned: dict[str, int], upgrades_owned: dict[str, dict[str, bool | float | str]]):
    print()
    for key, value in buildings_owned.items():
        print(f"{key}: {value}")
        sleep(0.5)

    for key, value in upgrades_owned.items():
        if value["owned"]:
            print(f"{key}: {value['mult']}")
        sleep(0.5)

def cookieTap(buildings_owned: dict[str, int], upgrades: dict[str, dict[str, bool | float | str]], click_amount: int):
    building_amount: int = 0
    for key, value in buildings_owned.items():
        match key:
            case "Clicker":
                if upgrades["Clicker MK2"]["owned"]:
                    building_amount += (1 * int(upgrades["Clicker MK2"]["mult"])) * value
                else:
                    building_amount += 1 * value
            case "Grandma":
                if upgrades["Grandma MK2"]["owned"]:
                    building_amount += (5 * int(upgrades["Grandma MK2"]["mult"])) * value
                else:
                    building_amount += 5 * value
            case _:
                pass

    sleep(click_delay)
    return int(click_amount + building_amount)

def openShop(buildings: dict[str, int], cookies: int, upgrades: dict[str, dict[str, bool | float | str]]):
    print("Shop:")
    print("1. Clicker -> 15 cookies")
    print("2. Grandma -> 100 cookies")

    print("3. Clicker MK2 -> 250 cookies")
    print("4. Grandma MK2 -> 500 cookies")

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
        case "3":
            if upgrades["Clicker MK2"]["owned"] == True:
                print("You already own Clicker MK2...")
                return 0
            elif cookies >= 250:
                upgrades["Clicker MK2"]["owned"] = True
                checkout -= 250
            else:
                print("Not enough cookies...")
        case "4":
            if upgrades["Grandma MK2"]["owned"] == True:
                print("You already own Grandma MK2...")
                return 0
            elif cookies >= 500:
                upgrades["Grandma MK2"]["owned"] = True
                checkout -= 500
            else:
                print("Not enough cookies...")
        case _:
            print("Invalid command...")

    return checkout

def main():
    global cookies
    global buildings_owned
    global upgrades_owned
    global click_amount

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
                cookies += cookieTap(buildings_owned, upgrades_owned, click_amount)
            case "shop":
                print()
                cookies += openShop(buildings_owned, cookies, upgrades_owned)
            case "quit":
                print("\nGoodbye!")
                sleep(click_delay)
                exit()
            case "log":
                openLog(buildings_owned, upgrades_owned)
            case _:
                print("???")

if __name__ == "__main__":
    main()

