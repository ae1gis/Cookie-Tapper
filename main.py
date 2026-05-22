from time import sleep

def startGame(quickStart: bool):
    print("Welcome to Cookie Tapper!\n")

    if quickStart:
        return

    print("loading", end="", flush=True)

    for _ in range(8):
        sleep(0.5)
        print(".", end="", flush=True)
    print("\n\n")

    print("------ COMMANDS ------")
    print("ENTER -> Tap the cookie")
    print("shop -> Enter the shop")
    print("log -> Show owned items")
    #debug -> Enables debug tools
    print("quit -> Exit the game\n")

def calculateCPS(building: dict[str, dict[str, int]], upgrade: dict[str, dict[str, bool | int | str]]):
    cps: int = 1
    baseIncome: int = 0

    for nameBuilding, statBuilding in building.items():
        baseIncome = statBuilding["cps"] * statBuilding["owned"]
        multiplier: float = 1.0

        for _, statUpgrade in upgrade.items():
            if statUpgrade["appliesTo"] == nameBuilding and statUpgrade["owned"]:
                multiplier += (float(statUpgrade["multiplier"]) - 1.0)

        cps += int(baseIncome * multiplier)
        baseIncome = 0

    return cps

def attemptBuildingPurchase(cookies: int, building: dict):
    if cookies >= building["cost"]:
        building["owned"] += 1
        return cookies - building["cost"]
    else:
        print("Not enough cookies...\n")
        return cookies

def attemptUpgradePurchase(cookies: int, upgrade: dict):
    if upgrade["owned"]:
        print("You already own this upgrade...\n")
    elif cookies >= upgrade["cost"]:
        upgrade["owned"] = True
        cookies -= upgrade["cost"]
    else:
        print("Not enough cookies...\n")

    return cookies

def openShop(building: dict[str, dict[str, int]], upgrade: dict[str, dict[str, bool | int | str]], cookies: int):
    while True:
        print("--- Shop ---")
        print("1. Clicker: +1CPS -> 15 cookies")
        print("2. Grandma: +5CPS -> 100 cookies")
        print("3. Bakery: +20CPS -> 1000 cookies")
        print("4. Factory: +50CPS -> 5000 cookies")
        print("5. Clicker I: Clicker 2x Mult")
        print("6. Grandma I: Grandma 2x Mult\n")

        print(f"You have {cookies} cookies")

        userInput: str = input(">>> ")

        match userInput:
            case "1":
                cookies = attemptBuildingPurchase(cookies, building["Clicker"])
            case "2":
                cookies = attemptBuildingPurchase(cookies, building["Grandma"])
            case "3":
                cookies = attemptBuildingPurchase(cookies, building["Bakery"])
            case "4":
                cookies = attemptBuildingPurchase(cookies, building["Factory"])
            case "5":
                cookies = attemptUpgradePurchase(cookies, upgrade["Clicker I"])
            case "6":
                cookies = attemptUpgradePurchase(cookies, upgrade["Grandma I"])
            case "quit":
                return cookies
            case _:
                print("Invalid command...")

def openLog():
    pass

def enableDebugTools():
    pass

def main():
    cookies: int = 0

    building: dict[str, dict[str, int]] = {
        "Clicker": {"owned": 0, "cost": 15, "cps": 1},
        "Grandma": {"owned": 0, "cost": 100, "cps": 5},
        "Bakery": {"owned": 0, "cost": 1000, "cps": 20},
        "Factory": {"owned": 0, "cost": 5000, "cps": 50}
    }

    upgrade: dict[str, dict[str, bool | int | str]] = {
        "Clicker I": {"owned": False, "cost": 200, "multiplier": 2, "appliesTo": "Clicker"},
        "Grandma I": {"owned": False, "cost": 1000, "multiplier": 2, "appliesTo": "Grandma"}
    }

    startGame(quickStart=False)

    while True:
        print(f"\nCookies -> {cookies}")

        userInput: str = input(">>> ")

        match userInput:
            case "":
                cookies += calculateCPS(building, upgrade)
            case "shop":
                cookies = openShop(building, upgrade, cookies)
            case "log":
                openLog()
            case "debug":
                pass
            case "quit":
                print("\nGoodbye...")
                sleep(1)
                exit()
            case _:
                print("\nWARNING: Unrecongized command...")


if __name__ == "__main__":
    main()
