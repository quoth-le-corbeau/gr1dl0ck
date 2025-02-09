"""
function hex_to_bytes(hex_string):
    return decode hex_string into raw bytes

function xor_decrypt(ciphertext, key):
    plaintext = ""
    for each byte in ciphertext:
        plaintext += (byte XOR key)
    return plaintext

function english_score(text):
    score = 0
    common_chars = "ETAOIN SHRDLU"  # Most common letters in English
    for char in text:
        if char is in common_chars:
            score += some_weight
    return score


"""


def _hex_to_bytes(hex_string: str) -> bytes:
    pass


def find_best_key(hex_string: str) -> tuple[str, str]:
    cipher_text = _hex_to_bytes(hex_string)
    best_score = 0
    best_key = None
    best_plaintext = ""
    for key in range(256):
        plain_text = xor_decrypt(cipher_text, key)
        score = _get_english_score(english_text=plain_text)
        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plain_text
    return best_key, best_plaintext


hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
key, message = find_best_key(hex_string)
print("Key:", key, "Message:", message)
