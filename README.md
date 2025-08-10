
# GitHub Auto Follow Bot

A Python script that automatically searches for GitHub users by a keyword and follows them using the **official GitHub API**.  
⚠ This script is intended for **educational and personal use** only. Please follow GitHub's [Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).

---

## Features
- Search for GitHub users by keyword.
- Automatically follow multiple users.
- Supports pagination (follow hundreds of users in one run).
- Uses **GitHub REST API** (safe & legal).

---

## Requirements
- Python 3.7+
- GitHub Personal Access Token (**Classic**)

---

## Getting Started

### 1️⃣ Create a Personal Access Token (Classic)
1. Go to **[GitHub Tokens Settings](https://github.com/settings/tokens)**.
2. Click **"Generate new token" → "Generate new token (classic)"**.
3. Give it a name (e.g., `follow-bot`).
4. Select **these permissions**:
   - ✅ `user`
   - ✅ `user:follow`
5. Set an expiration date (recommended: 30 days).
6. Click **"Generate token"** and copy it (you will need it later).

---

### 2️⃣ Install Dependencies
```bash
pip install requests

---
### 3️⃣ Configure the Script

Edit the TOKEN variable in the script:

TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"


---

### 4️⃣ Run the Script

python github_follow_bot.py

You will be prompted to enter a keyword (e.g., react, python), and the bot will search for users and follow them.


---

Example Output

🔍 Enter keyword (e.g., react, python): react
Found 500 users
✅ Followed gaearon
✅ Followed acdlite
✅ Followed kentcdodds
...
