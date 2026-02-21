def grid_challenge(grid):
    # 1. เรียงลำดับตัวอักษรในแต่ละแถว (Row) ให้จากน้อยไปมาก (เช่น 'cba' -> 'abc')
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    # 2. ตรวจสอบว่าในแต่ละคอลัมน์ (Column) เรียงจากน้อยไปมากหรือไม่ (จากบนลงล่าง)
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    for c in range(cols):
        for r in range(rows - 1):
            # ถ้าตัวอักษรแถวบน (r) มีค่า ASCII มากกว่าแถวล่าง (r+1) ในคอลัมน์เดียวกัน
            if sorted_grid[r][c] > sorted_grid[r+1][c]:
                return "NO"
                
    return "YES"