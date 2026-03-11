def reverse_string(s: str) -> str:
    return s[::-1]


def capitalize_words(s: str) -> str:
    return s.title()


def remove_whitespace(s: str) -> str:
    return "".join(s.split())


def count_words(s: str) -> int:
    return len(s.split())


def is_palindrome(s: str) -> bool:
    clean = "".join(s.split()).lower()
    
    return clean == clean[::-1]
