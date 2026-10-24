from google.oauth2.credentials import Credentials
import gspread
from gspread.utils import ValidationConditionType

credentials = Credentials.from_authorized_user_file(
    "token.json",
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
    "interview Completed",
    "Rejected",
    "Ghosted",
    "Dropped",
    "Offer",
]

worksheet.add_validation(
    "C2:C",
    condition_type=ValidationConditionType.one_of_list,
    values=status_options,
    strict=True,
    showCustomUi=True,
)

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
