from datetime import datetime

FILENAME = "todays_entry.txt"

def main():
    entry = input("whats today??\n> ").strip()

    if not entry:
        print("Empty entry. Nothing saved.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_entry = (
        "\n"
        "==============================\n"
        f"Time: {timestamp}\n"
        f"{entry}\n"
    )

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(formatted_entry)

    print("Entry saved.")

if __name__ == "__main__":
    main()
