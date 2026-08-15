def clean_text(text):
    cleaned_text = " ".join(text.lower().split())
    return cleaned_text


def word_count(text):
    count = 0
    for _ in text.split():
        count += 1
    return count
