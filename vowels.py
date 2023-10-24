def is_vowel(letter):
  """Checks whether a letter is a vowel or a consonant.

  Args:
    letter: The letter to check.

  Returns:
    True if the letter is a vowel, False otherwise.
  """

  vowels = ["a", "e", "i", "o", "u"]
  if letter in vowels:
    return True
  else:
    return False

# Example usage:

letter = input("Enter a letter: ")

if is_vowel(letter):
  print("The letter {} is a vowel.".format(letter))
else:
  print("The letter {} is a consonant.".format(letter))
