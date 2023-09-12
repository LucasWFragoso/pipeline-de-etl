import pandas as pd
from apiSDW import get_user_api
import json


def extract_ids_csv(csv):
    data = pd.read_csv(csv)

    user_ids = data["UserID"].tolist()

    return user_ids


def user():
    ids = extract_ids_csv("data.csv")
    users = [user for id in ids if (user := get_user_api(id)) is not None]

    print(json.dumps(users, indent=2))
