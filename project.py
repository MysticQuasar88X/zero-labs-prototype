def main():
    print("=== Zero Labs R&D Console ===")
    print("Research and Development Prototype")
    print()

    question = input("Ask a research question: ").strip()

    if not question:
        print("No question entered.")
        return

    print()
    print("Research Response")
    print("-----------------")
    print(
        "This question has been received by Zero Labs.\n"
        "It is a valid research inquiry.\n"
        "Further investigation and development may be required."
    )
    print()
    print("Zero Labs session complete.")


if __name__ == "__main__":
    main()
