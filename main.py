from google.oauth2.credentials import Credentials
import gspread

credentials = Credentials.from_authorized_user_file(
    "token.json",
    ["https://www.googleapis.com/auth/spreadsheets"]
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(
    "1h3hbBPRAsv9vNnYM8VDe-m38tWlxlfFiYeScgwGy9oo"
)

worksheet = spreadsheet.sheet1

headers = [
    "Company",
    "Position",
    "Status",
    "Location",
    "Date",
    "Link",
    "Notes"
]

worksheet.append_row(headers)

worksheet.format("A1:G1", {
    "backgroundColor": {
        "red": 0.1,
        "green": 0.4,
        "blue": 0.8
    },
    "textFormat": {
        "bold": True,
        "foregroundColor": {
            "red": 1,
            "green": 1,
            "blue": 1
        }
    }
})

print("the headers were added")
