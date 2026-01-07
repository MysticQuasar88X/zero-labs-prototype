def main():
    print("=== Zero Labs R&D Console ===")
    print("Structured thinking. Experimental ideas. Logged inputs.")
    print()

    topic = input("Enter a research topic or idea: ").strip()

    if not topic:
        print("No input provided. Session terminated.")
        return

    print()
    print("Research Log Entry")
    print("------------------")
    print(f"Topic: {topic}")
    print("Status: Logged for future development")
    print()
    print("Zero Labs session complete.")


if __name__ == "__main__":
    main()
