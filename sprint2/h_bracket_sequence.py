def is_correct_bracket_seq(s: str) -> bool:
    unclosed_brackets = []
    for ch in s:
        if ch in '[({':
            unclosed_brackets.append(ch)
            continue
        if not unclosed_brackets:
            return False
        last_open = unclosed_brackets.pop()
        if (last_open, ch) not in {('[', ']'), ('(', ')'), ('{', '}')}:
            return False
    return not unclosed_brackets


if __name__ == '__main__':
    s = input()
    print(is_correct_bracket_seq(s))
