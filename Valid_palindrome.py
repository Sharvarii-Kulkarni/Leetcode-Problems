def palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while r > l and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False

        l = l + 1
        r = r - 1

        return True


def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('1') <= ord(c) <= ord('9'))


s = "A man, a plan, a canal: Panama"
print(palindrome(s))
