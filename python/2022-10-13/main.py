def decrypt(char: str, offset: int) -> str:
    return chr((ord(char)-97-offset) % 26 + 97)


print(decrypt('c', 4))
