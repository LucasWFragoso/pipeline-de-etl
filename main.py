from extractIds import extract_ids_csv, users
from apiSDW import get_user_api, update_user
from generateNews import generate_ai_news


users_list = users()

for user in users_list:
    news = generate_ai_news(user)
    user["news"].append(
        {
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news,
        }
    )
    update_user(user)
