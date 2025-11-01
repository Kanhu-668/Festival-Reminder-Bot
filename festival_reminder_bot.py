import datetime
import json
import os

# ---------- File setup ----------
DATA_FILE = "festivals.json"

# Default sample festivals (auto-created if file not found)
SAMPLE_FESTIVALS = {
    "Holi": "2025-03-14",
    "Ganesh Chaturthi": "2025-09-01",
    "Diwali": "2025-10-20",
    "Christmas": "2025-12-25"
}

# Load festivals from JSON file (create one if missing)
def load_festivals():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(SAMPLE_FESTIVALS, f, indent=4)
        print("📁 Created 'festivals.json' with sample festivals!\n")
        return SAMPLE_FESTIVALS.copy()

    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save festivals to JSON file
def save_festivals(festivals):
    with open(DATA_FILE, "w") as f:
        json.dump(festivals, f, indent=4)

# ---------- Core Functions ----------
def add_festival(festivals):
    name = input("Enter festival name: ").strip().title()
    if name in festivals:
        print("⚠️ Festival already exists!\n")
        return

    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        festivals[name] = date_str
        save_festivals(festivals)
        print(f"✅ {name} added successfully!\n")
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.\n")

def delete_festival(festivals):
    name = input("Enter festival name to delete: ").strip().title()
    if name in festivals:
        del festivals[name]
        save_festivals(festivals)
        print(f"🗑️ {name} deleted successfully!\n")
    else:
        print("❌ Festival not found!\n")

def view_festivals(festivals):
    if not festivals:
        print("📭 No festivals saved yet.\n")
        return
    print("\n🎉 Saved Festivals:")
    for name, date in sorted(festivals.items(), key=lambda x: x[1]):
        print(f"  • {name} → {date}")
    print()

def check_reminders(festivals):
    today = datetime.date.today()
    upcoming = []

    for name, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        diff = (fest_date - today).days

        if diff == 0:
            print(f"🎊 TODAY is {name}! Celebrate!")
        elif 0 < diff <= 7:
            upcoming.append((name, diff))

    if upcoming:
        print("\n🗓️ Festivals coming within the next 7 days:")
        upcoming.sort(key=lambda x: x[1])
        for name, days in upcoming:
            print(f"  • {name} in {days} day(s)")
    else:
        print("\nNo upcoming festivals within the next 7 days.\n")
    print()

# ---------- Main Menu ----------
def main():
    festivals = load_festivals()

    while True:
        print("========== FESTIVAL REMINDER BOT ==========")
        print("1. View all festivals")
        print("2. Add a new festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_festivals(festivals)
        elif choice == '2':
            add_festival(festivals)
        elif choice == '3':
            delete_festival(festivals)
        elif choice == '4':
            check_reminders(festivals)
        elif choice == '5':
            print("👋 Exiting Festival Reminder Bot. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

# ---------- Run the bot ----------
if __name__ == "__main__":
    main()
