def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# 用户交互
choice = input("请选择操作 (1: 加密, 2: 解密): ")

if choice == '1':
    user_text = input("请输入要加密的文本: ")
    shift = int(input("请输入偏移量 (整数): "))
    print(caesar_cipher_encrypt(user_text, shift))
elif choice == '2':
    user_text = input("请输入要解密的文本: ")
    shift = int(input("请输入偏移量 (整数): "))
    print(caesar_cipher_decrypt(user_text, shift))
else:
    print("无效选择!")
