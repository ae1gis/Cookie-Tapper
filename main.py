from time import sleep

testing = True

cookies: int = 0
buildings_owned: dict[str, int] = {"Grandma": 0, "Placeholder": 0}

def cookieTap(buildings: int, click: int, mult: float):
    return int((click + buildings) * mult)

def openShop(buildings: dict[str, int]):
    print("Shop:")
    print("1. Grandma -> 100 cookies")
    print("2. Placeholder -> 1 cookies")

    user_selection: str = input("Enter a number >>> ")
    
    match user_selection:
        case "1":
            print(f"{buildings["Grandma"]} -> {buildings["Grandma"] + 1}")
        case "2":
            print(buildings["Grandma"])
        case _:
            pass

def main():
    global cookies

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
                cookies += cookieTap(0, 1, 1)
            case "shop":
                print("Shop executed")
                openShop(buildings_owned)
            case "quit":
                exit()
            case "list":
                print("List executed")
            case _:
                print("???")

if __name__ == "__main__":
    main()

