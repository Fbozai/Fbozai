MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' '
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    words = morse_code.split('   ')  # 3 spaces between words
    decoded_message = ""

    for word in words:
        letters = word.split(' ')
        for letter in letters:
            decoded_message += REVERSE_MORSE_CODE_DICT.get(letter, '')  # 使用.get避免未知符号
        decoded_message += ' '

    return decoded_message.strip()

def text_to_morse(text):
    encoded_message = ""

    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            encoded_message += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            encoded_message += char + ' '

    return encoded_message.strip()

# 用户交互
choice = input("请选择操作 (1: 明文转摩斯, 2: 摩斯转明文): ")

if choice == '1':
    user_text = input("请输入明文: ")
    print(text_to_morse(user_text))
elif choice == '2':
    user_morse = input("请输入摩斯密码: ")
    print(morse_to_text(user_morse))
else:
    print("无效选择!")
