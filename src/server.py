from flask import Flask, jsonify
from dotenv import load_dotenv
from pathlib import Path
import requests
import os

app = Flask(__name__)
dotenv_path = Path('/srv/src/.env')
load_dotenv(dotenv_path=dotenv_path)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_API_BASE_URL = "https://discord.com/api/v10/"

@app.route("/avatar/<user_id>")
def get_user_avatar(user_id):
    api_endpoint = f"{DISCORD_API_BASE_URL}users/{user_id}"

    headers = {
        "Authorization": f"Bot {DISCORD_BOT_TOKEN}"
    }

    try:
        response = requests.get(api_endpoint, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data['avatar']}"
            return jsonify({"avatar_url": avatar_url})

        # Handle errors (e.g., user not found)
        elif response.status_code == 404:
            return jsonify({"error": "User not found"}), 404

        else:
            return jsonify({"error": "Failed to fetch user data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)

