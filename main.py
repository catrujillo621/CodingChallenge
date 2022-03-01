from collections import defaultdict
import requests
import json


def main():
    number = int(input("Please, insert the number: "))
    list = search(number)
    return list


def search(total):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    data = json.loads(response.text)
    players = data["values"]
    d = defaultdict(list)
    for player in players:
        d[int(player['h_in'])].append(player['first_name'] + " " + player['last_name'])
    return [player + " & " + other
            for height in d
            if total - height in d
            for other in d[total - height]
            for player in d[height]
            if player < other
            ]



if __name__ == "__main__":
    result = main()
    end = len(result)
    while end == 0:
        print("No matches found")
        result = main()
        end = len(result)
    print(result)
