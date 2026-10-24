import os
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def token_path() -> Path:
    config_home = Path(
        os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")
    ).expanduser()
    return config_home / "shukatsu" / "token.json"

def client_secrets_path() -> Path:
    return token_path().with_name("credentials.json")

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        str(client_secrets_path()),
        SCOPES,
    )

    credentials = flow.run_local_server(port=0)

    path = token_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(credentials.to_json(), encoding="utf-8")
    path.chmod(0o600)

    print(f"authentication was successful, token saved to {path}")

if __name__ == "__main__":
    authenticate()
