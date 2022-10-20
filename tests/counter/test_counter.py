from src.counter import count_ocurrences

PATH = "src/jobs.csv"
WORD_UPPERCASE = "PYTHON"
WORD_LOWERCASE = "python"
N = 1639


def test_counter():
    word_count_uppercase = count_ocurrences(PATH, WORD_UPPERCASE)
    word_count_lowercase = count_ocurrences(PATH, WORD_LOWERCASE)
    assert word_count_uppercase == N == word_count_lowercase
