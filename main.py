from google.oauth2.credentials import Credentials
import gspread
import questionary
from auth import token_path

credentials = Credentials.from_authorized_user_file(
    str(token_path()),
    ["https://www.googleapis.com/auth/spreadsheets"]
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(
    "1h3hbBPRAsv9vNnYM8VDe-m38tWlxlfFiYeScgwGy9oo"
)

worksheet = spreadsheet.sheet1

status_options = [
    "Pending",
    "Applied",
    "Interview Scheduled",
    "Interviewing",
    "Interview Completed",
    "Rejected",
    "Ghosted",
    "Dropped",
    "Offer",
]

company = input("Company: ")
position = input("Position: ")
status = questionary.select(
    "Status:",
    choices=[
        "Pending",
        "Applied",
        "Interview Scheduled",
        "Interviewing",
        "Interview Completed",
        "Rejected",
        "Ghosted",
        "Dropped",
        "Offer",
    ],
).ask()

if status is None:
    raise SystemExit("\nStatus selection was cancelled.")

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
