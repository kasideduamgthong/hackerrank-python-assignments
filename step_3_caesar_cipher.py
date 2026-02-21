def caesar_cipher(s, k):
    result = ""
    shift = k % 26  # จัดการกรณี k > 26
    
    for char in s:
        if 'a' <= char <= 'z':
            # สูตร: (ลำดับตัวอักษร + ระยะเลื่อน) % 26
            # ลำดับตัวอักษรหาได้จาก ord(char) - ord('a')
            new_pos = (ord(char) - ord('a') + shift) % 26
            result += chr(new_pos + ord('a'))
        elif 'A' <= char <= 'Z':
            new_pos = (ord(char) - ord('A') + shift) % 26
            result += chr(new_pos + ord('A'))
        else:
            # ไม่ใช่ตัวอักษร ให้ใส่ตัวเดิม
            result += char
            
    return result