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

company = input("Company: ")
position = input("Position: ")
status = input("Status: ")
location = input("Location: ")
date = input("Date: ")
link = input("Link: ")
notes = input("Notes: ")

row = [
    company,
    position,
    status,
    location,
    date,
    link,
    notes
]

worksheet.append_row(row)
print("application added")
