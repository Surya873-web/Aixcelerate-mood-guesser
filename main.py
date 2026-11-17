# AIXcelerate Mood Guesser
# A beginner-friendly rule-based program for Happy/Sad sentence examples.

# Training data: (sentence, correct mood)
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]

# The assignment requires exactly one clue word in each list.
happy_words = ["won"]
sad_words = ["lost"]


def count_moods(data):
    """Return the number of Happy and Sad labels in data."""
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


def get_words(sentence):
    """Lowercase a sentence and split it into words safely.

    Punctuation becomes a space so it cannot accidentally join two words.
    For example, "won,lost" becomes ["won", "lost"].
    """
    cleaned_characters = []

    for character in sentence.lower():
        if character.isalnum():
            cleaned_characters.append(character)
        else:
            cleaned_characters.append(" ")

    cleaned_sentence = "".join(cleaned_characters)
    return cleaned_sentence.split()


def guess_mood(sentence):
    """Guess Happy or Sad using the clue words; ties are classified Sad."""
    words = get_words(sentence)
    happy_count = 0
    sad_count = 0

    for word in happy_words:
        if word in words:
            happy_count += 1

    for word in sad_words:
        if word in words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"
    return "Sad"


def main():
    print("LEVEL 1 - MOOD COUNT")
    print("Mood Count:", count_moods(train_data))

    practice_data = [
        ("I won a medal in the sports meet", "Happy"),
        ("I lost my notebook before the exam", "Sad"),
        ("My friends gave me a lovely surprise", "Happy"),
        ("The train was late and I felt upset", "Sad"),
        ("Today was a great day", "Happy"),
    ]

    print("\nLEVEL 3 - PRACTICE TEST")
    correct = 0

    for sentence, actual_mood in practice_data:
        predicted_mood = guess_mood(sentence)
        print("\nSentence:", sentence)
        print("Actual Mood:", actual_mood)
        print("Predicted Mood:", predicted_mood)

        if predicted_mood == actual_mood:
            correct += 1

    total_sentences = len(practice_data)
    accuracy = (correct / total_sentences) * 100

    print("\nCorrect Predictions:", correct)
    print("Total Sentences:", total_sentences)
    print("Accuracy:", accuracy, "%")


if __name__ == "__main__":
    main()
