def letter_to_position(text):
    positions = []
    for letter in text:
        if letter.isalpha():
            positions.append(str(ord(letter.lower()) - 96))
    return ' '.join(positions)

# Example usage
input_text = "The sunset sets at twelve o' clock."
output_text = letter_to_position(input_text)
print(output_text)
