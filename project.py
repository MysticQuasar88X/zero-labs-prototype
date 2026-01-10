def research_response(question):
    """Return a short research-oriented response for the given question.

    This function is defensive: it accepts non-string inputs, strips whitespace,
    and returns a clear message for empty questions.
    """
    # Make robust to None or non-string inputs
    q = "" if question is None else str(question).strip()
    if not q:
        return "No question entered. Please provide a research question."

    q = q.lower()

    # Biology / Animals
    if any(word in q for word in ["dog", "cat", "bird", "chicken", "bull", "animal"]):
        return (
            "This is a biological or behavioral research question. "
            "Animal behaviors are typically influenced by evolution, "
            "environmental pressures, survival needs, and learned responses. "
            "Further study may involve zoology, ethology, or neuroscience."
        )

    # Human behavior / psychology
    elif any(word in q for word in ["sex", "love", "desire", "emotion", "relationship"]):
        return (
            "This question relates to human behavior and psychology. "
            "Such topics are influenced by biology, culture, experience, "
            "and individual variation."
        )

    # Science / mechanisms
    elif any(word in q for word in ["why", "how", "physics", "chemistry", "energy", "fly"]):
        return (
            "This is a scientific inquiry aimed at understanding mechanisms or causes. "
            "Scientific research typically involves observation, experimentation, "
            "and evidence-based reasoning."
        )

    # Substances (neutral)
    elif any(word in q for word in ["drug", "medicine", "chemical", "substance"]):
        return (
            "This question involves substances or chemical compounds. "
            "Research typically examines effects, risks, benefits, "
            "and regulatory considerations."
        )

    # Default
    else:
        return (
            "This question has been logged as a general research inquiry. "
            "It may require multidisciplinary analysis."
        )


# Minimal single main loop for interactive use
def main():
    """Run a simple interactive console for asking research questions."""
    import sys
    # If arguments were passed, answer them as a single question
    if len(sys.argv) > 1:
        print(research_response(" ".join(sys.argv[1:])))
        return

    # Interactive prompt: single main loop
    print("=== Zero Labs R&D Console ===")
    print("Research and Development Prototype")
    print()

    try:
        while True:
            q = input("Ask a research question (blank to exit): ").strip()
            if not q:
                print("No question entered. Exiting.")
                break
            print()
            print("Research Response")
            print("-----------------")
            print(research_response(q))
            print()
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")


