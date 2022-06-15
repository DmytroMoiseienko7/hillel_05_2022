team = [
    {"name": "John", "age": 20, "number": 5},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def player_update(num, players, name, age):
    my_team = [player["number"] for player in players]
    if num in my_team:
        for player in players:
            if player["number"] == num:
                result = player.update({"name": name, "age": age})
    else:
        result = print("> -> -> No player with such number <- <- <-")
    return result


def repr_players(players, my_sort=True, my_key="number") -> None:
    print("TEAM:")
    if my_sort is True:
        my_team = sorted(players, key=lambda x: x[f"{my_key}"])
        for player in my_team:
            print(
                f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}"
            )
    else:
        for player in players:
            print(
                f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}"
            )
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ***")


def add_player(num, name, age, team=team) -> None:
    player = {"name": name, "number": num, "age": age}
    collector = []
    for players in team:
        collector.append(players["number"])
    if player["number"] not in collector:
        team.append(player)
        log(message=f"Adding {player['name']}")
    else:
        print("-> -> -> Player with the same number could not be added <- <- <-")


def remove_player(players, num) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def main():
    player_update(5, team, "Dmytro", 28)

    repr_players(team, my_key="name")

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    repr_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
