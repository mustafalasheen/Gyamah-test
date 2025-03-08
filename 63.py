from g4f.providers.response import quote_title

# Test with normal text
text = "This   is   a    test"
print(f"Original: '{text}'")
print(f"Cleaned:  '{quote_title(text)}'\n")

# Test with messy formatting
messy_text = """This
    has weird
        spacing"""
print(f"Original: '{messy_text}'")
print(f"Cleaned:  '{quote_title(messy_text)}'\n")

# Test with empty input
empty = ""
print(f"Original: '{empty}'")
print(f"Cleaned:  '{quote_title(empty)}'")