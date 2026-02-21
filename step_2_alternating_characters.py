def alternating_characters(s):
    deletions = 0
    # วนลูปเช็คตัวอักษรปัจจุบันกับตัวถัดไป
    for i in range(len(s) - 1):
        # ถ้าตัวที่ติดกันเหมือนกัน (เช่น AA) เราต้องลบออก 1 ตัว
        if s[i] == s[i+1]:
            deletions += 1
    return deletions