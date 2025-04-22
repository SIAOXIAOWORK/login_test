import csv
import json
import pytest

def load_csv_data():
    data = []
    with open("login_test_data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((row["username"],row["password"],row["expected"]))

        return data


def load_json_data():
    data = []
    with open("login_test_data.json",encoding="utf-8") as f:
        reader = json.load(f)
        for item in reader:
            param =((item["username"],item["password"],item["expected"],))
            
            if item.get("xfail"):
                data.append(pytest.param(*param, marks = pytest.mark.xfail(reason="預期失敗",)))

            else :
                data.append(param)

        return data
