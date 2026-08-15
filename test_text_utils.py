from text_utils import clean_text, word_count


assert clean_text("  Hello August  ") == "hello august"
assert clean_text("Hello\tAugust\n") == "hello august"
assert word_count("Open source tools") == 3

print("All tests passed")
