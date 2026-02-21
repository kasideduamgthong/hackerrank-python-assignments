def caesar_cipher(s, k):
    result = ""
    
    k = k % 26 # k อาจจะมากกว่า 26 (จำนวนตัวอักษร) จึงต้องใช้ modulo เพื่อให้ได้ค่าที่เหมาะสม
    
    for char in s:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A') # ตรวจสอบว่าเป็นตัวพิมพ์เล็กหรือใหญ่เพื่อหาจุดเริ่มต้นในตาราง ASCII
           
            shifted_char = chr((ord(char) - start + k) % 26 + start)  # คำนวณตำแหน่งใหม่
            result += shifted_char
        else:
            result += char  # ถ้าไม่ใช่ตัวอักษร (เช่น - หรือ !) ให้คงไว้เหมือนเดิม
            
    return result