def funny_string(s):
    # 1. สร้างสตริงย้อนกลับ
    r = s[::-1]
    n = len(s)
    
    # 2. วนลูปเช็คค่าความต่าง ASCII
    for i in range(1, n):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        
        # ถ้ามีตำแหน่งไหนไม่เท่ากัน ให้ตอบ Not Funny ทันที
        if diff_s != diff_r:
            return "Not Funny"
            
    return "Funny"