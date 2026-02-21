def funny_string(s): # สร้างสตริงย้อนกลับ
    r = s[::-1]
    n = len(s)
    
    for i in range(1, n): # วนลูปเช็คค่าความต่าง ASCII
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        
        if diff_s != diff_r:   # ถ้ามีตำแหน่งไหนไม่เท่ากัน ให้ตอบ Not Funny ทันที
            return "Not Funny"
            
    return "Funny"