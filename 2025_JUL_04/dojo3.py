# https://leetcode.com/problems/length-of-last-word/description/


def ultima_palavra(s):
    splitado = s.split()
    return len(splitado[-1])

assert ultima_palavra('gato pula') == 4
assert ultima_palavra('   fly me   to   the moon  ') == 4
assert ultima_palavra('luffy is still joyboy') == 6