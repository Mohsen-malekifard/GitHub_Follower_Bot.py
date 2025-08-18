import requests

TOKEN = "ghp_****"  # Put Your Token GitHub Here
HEADERS = {"Authorization": f"token {TOKEN}"}

def search_users(keyword, pages=100, per_page=1000):
    users = []
    for page in range(1, pages + 1):
        url = f"https://api.github.com/search/users?q={keyword}&per_page={per_page}&page={page}"
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        users.extend(r.json()["items"])
    return users

def follow_user(username):
    url = f"https://api.github.com/user/following/{username}"
    r = requests.put(url, headers=HEADERS)
    if r.status_code == 204:
        print(f"✅ Followed {username}")
    else:
        print(f"⚠ Failed to follow {username}: {r.status_code}")

if __name__ == "__main__":
    keyword = input("🔍 Enter keyword (e.g., react, python): ")
    users = search_users(keyword, pages=1, per_page=1000)
    print(f"Found {len(users)} users")
    
    for user in users:
        print(f"👤 {user['login']} - {user['html_url']}")
        follow_user(user['login'])
