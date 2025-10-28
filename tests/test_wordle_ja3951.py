from wordle_ja3951.wordle_ja3951 import validate_guess, is_valid_word

WORD_LIST = [
    "crane", "apple", "hello", "world", "python", 
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    
    TODO: Students should implement this test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # TODO: Implement your test cases here
    assert validate_guess("house") == True #valid lowercase
    assert validate_guess("WORLD") == False #does not accept uppercase
    assert validate_guess("cat") == False #too short
    assert validate_guess("chairs") == False #too long
    assert validate_guess("wo2ld") == False #contains number (invalid)
    assert validate_guess("") == False #empty
    assert validate_guess("cr@ne") == False #invalid character
    assert validate_guess(None) == False #no input


def test_is_valid_word():
    """
    Test the is_valid_word function.
    
    TODO: Students should implement this test function with:
    - Valid words (case insensitive)
    - Invalid words (not in list)
    - Edge cases (empty string, empty word list)
    """
    # TODO: Implement your test cases here
    #Word exists
    assert is_valid_word("dream", WORD_LIST) == True

    #Word does not exist
    assert is_valid_word("adieu", WORD_LIST) == False

    #Case-insensitive check
    assert is_valid_word("BRAIN", WORD_LIST) == True

