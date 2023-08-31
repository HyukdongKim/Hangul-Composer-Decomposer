# This code is suggeted by ChatGPT-4 and modified by me.

# Initial consonants (초성)
initials = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# Medial vowels (중성)
medials = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]

# Final consonants (종성)
finals = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# Unicode value for the base syllable "가"
BASE = 0xAC00

# Offsets to syllable
def composer(initial, medial, final):
    """
    Given the characters for initial consonant, medial vowel, and final consonant,
    return the corresponding Hangul syllable.
    """
    initial_offset = initials.index(initial)
    medial_offset  = medials.index(medial)
    final_offset   = finals.index(final)
    unicode_val    = BASE + (initial_offset * 588) + (medial_offset * 28) + final_offset
    return chr(unicode_val)

# Syllable to offsets
def decomposer(syllable):
    """
    Given a Hangul syllable, return the characters for initial consonant, medial vowel, and final consonant.
    """
    unicode_val    = ord(syllable) - BASE
    initial_offset = unicode_val // 588
    unicode_val   %= 588
    medial_offset  = unicode_val // 28
    final_offset   = unicode_val % 28
    return initials[initial_offset], medials[medial_offset], finals[final_offset]
