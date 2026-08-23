company = input("Company: ")
position = input("Position: ")
status = input("Status: ")
location = input("Location: ")
date = input("Date: ")
link = input("Link: ")
notes = input("Notes: ")

application = {
    "company": company,
    "position": position,
    "status": status,
    "location": location,
    "date": date,
    "link": link,
    "notes": notes
}

row = [
    application["company"],
    application["position"],
    application["status"],
    application["location"],
    application["date"],
    application["link"],
    application["notes"]
]

print("\nApplication:")
print(f"Company: {company}")
print(f"Position: {position}")
print(f"Status: {status}")
print(f"Location: {location}")
print(f"Date: {date}")
print(f"Link: {link}")
if not notes:
    print("No notes.")
else:
    print(f"Notes: {notes}")

print(row)
