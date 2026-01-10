def research_response(question):
    q = question.lower()

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
