# Import from your new package
from textutils import cleaner, analysis

raw_text = "Hello!! This is a TEST string... #Python"

# Use the modules
clean_text = cleaner.remove_special_chars(raw_text)
lower_text = cleaner.to_lowercase(clean_text)
word_count = analysis.count_words(lower_text)

print(f"Original: {raw_text}")
print(f"Cleaned:  {lower_text}")
print(f"Words:    {word_count}")
