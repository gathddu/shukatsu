from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES,
    )

    credentials = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(credentials.to_json())

    print("authentication was successful")

if __name__ == "__main__":
    authenticate()
