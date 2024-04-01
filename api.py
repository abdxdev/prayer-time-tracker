import requests
from bs4 import BeautifulSoup
import json
import re


def main():
    response = requests.get("https://aladhan.com/ramadan-prayer-times/2024/Lahore/Pakistan").text
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find("table")
    table_header = table.find("thead")
    table_body = table.find("tbody").find_all("tr")
    table = [table_header.text.strip().split("\n")]
    for row in table_body:
        tempT = row.text.strip().split("\n")[:-2]
        tempT.pop(1)
        table.append(tempT)
    table_dict = []
    for row in table[1:]:
        table_dict.append({table[0][i]: row[i] for i in range(len(row))})
    main_result_frame = {}
    for row in table_dict:
        if match := re.match(r"(\d{2}) (\w+), (\d{4}) \((\d{2}) (\w+), (\d{4})\)", row["Date"]):
            temp = {}
            temp["gregorian_date"] = {
                "day": int(match.group(4)),
                "month": match.group(5),
                "year": int(match.group(6)),
            }
            temp["hijri_date"] = {
                "day": int(match.group(1)),
                "month": match.group(2),
                "year": int(match.group(3)),
            }
        tempT = {}
        for key, val in row.items():
            if match := re.match(r"(\d{2}):(\d{2}) \((\w+)\)", val):
                tempT[key.lower()] = {
                    "hour": int(match.group(1)),
                    "minute": int(match.group(2)),
                    "timezone": match.group(3),
                }
        temp["times"] = tempT
        main_result_frame[temp["gregorian_date"]["day"]] = temp

    json.dump(main_result_frame, open("prayer_times.json", "w"), indent=4)


if __name__ == "__main__":
    main()
