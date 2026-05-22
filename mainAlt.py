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

def openShop(building: dict[str, dict[str, int]], upgrade: dict[str, dict[str, bool | int | str]]):
    pass

def openLog():
    pass

def enableDebugTools():
    pass

def main():
    cookies: int = 0

    building: dict[str, dict[str, int]] = {
        "Clicker": {"owned": 5, "cost": 15, "cps": 1},
        "Grandma": {"owned": 0, "cost": 100, "cps": 5},
        "Bakery": {"owned": 0, "cost": 1000, "cps": 20},
        "Factory": {"owned": 0, "cost": 5000, "cps": 50}
    }

    upgrade: dict[str, dict[str, bool | int | str]] = {
        "Clicker I": {"owned": True, "cost": 200, "multiplier": 2, "appliesTo": "Clicker"},
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
                openShop(building, upgrade)
            case "log":
                openLog(building, upgrade)
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
