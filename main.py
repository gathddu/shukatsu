import argparse
import sys

from google.oauth2.credentials import Credentials
import gspread
import questionary
from auth import authenticate, token_path

SPREADSHEET_ID = "1h3hbBPRAsv9vNnYM8VDe-m38tWlxlfFiYeScgwGy9oo"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

STATUS_OPTIONS = [
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

def add_application():
    path = token_path()
    if not path.is_file():
        raise SystemExit("not set up yet. run 'shukatsu init'.")

    credentials = Credentials.from_authorized_user_file(str(path), SCOPES)
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    worksheet = spreadsheet.sheet1

    company = input("Company: ")
    position = input("Position: ")
    status = questionary.select(
        "Status:",
        choices = STATUS_OPTIONS).ask()

    if status is None:
        print("\nstatus selection was cancelled.")
        return

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

def list_applications(status_filter=None):
    path = token_path()
    if not path.is_file():
        raise SystemExit("not set up yet. run 'shukatsu init'.")

    credentials = Credentials.from_authorized_user_file(str(path), SCOPES)
    client = gspread.authorize(credentials)
    worksheet = client.open_by_key(SPREADSHEET_ID).sheet1
    applications = worksheet.get_all_records()

    if status_filter is not None:
        applications = [
            application
            for application in applications
            if str(application.get("Status", "")).strip().casefold()
            == status_filter.strip().casefold()
        ]

    if not applications:
        print("no matches.")
        return

    for application in applications:
        print(
            f"{application.get('Company', '')} | "
            f"{application.get('Position', '')} | "
            f"{application.get('Status', '')} | "
            f"{application.get('Location', '')} | "
            f"{application.get('Date', '')} | "
        )

def main():
    parser = argparse.ArgumentParser(prog="shukatsu")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="set up google sign-in")
    commands.add_parser("add", help="add a job application")
    list_command = commands.add_parser("list", help="list job applications")
    list_command.add_argument("--status", help="filter by status")

    args = parser.parse_args()

    try:
        if args.command == "init":
            authenticate()
        elif args.command == "add":
            add_application()
        elif args.command == "list":
            list_applications(args.status)
    except KeyboardInterrupt:
        print("cancelled.")
        return 130
    return 0

if __name__ == "__main__":
    sys.exit(main())
