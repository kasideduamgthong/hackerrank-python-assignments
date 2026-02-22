Readme.md สำหรับโปรเจกต์ HackerRank
HackerRank Python Assignments (Steps 1-5)

โปรเจกต์นี้เป็นการรวบรวมแนวทางการแก้ปัญหาจาก HackerRank ทั้งหมด 5 ข้อ โดยเน้นการเขียนโปรแกรมด้วยภาษา Python และการทำ Unit Testing ให้ได้ Code Coverage 100%

รายชื่อโจทย์

1.  Step 1: Funny String
2.  Step 2: Alternating Characters
3.  Step 3: Caesar Cipher
4.  Step 4: Two Characters
5.  Step 5: Grid Challenge

วิธีการรันโปรเจกต์

1. การเตรียมความพร้อม (Prerequisites)
ติดตั้ง Library สำหรับวัด Coverage:
pip install coverage

2. วิธีการรัน Unit Test
ใช้คำสั่งนี้เพื่อตรวจสอบความถูกต้องของโปรแกรมทั้งหมด (19 Test Cases):
python -m unittest discover 

รันที่ละข้อ (พร้อมระบุชื่อไฟล์)
python -m unittest test_step_1_funny_string.py 

3. วิธีการรัน Algorithm ทั่วไป รันเพื่อดูผลลัพธ์ของแต่ละข้อ (พร้อมระบุชื่อไฟล์)
  python step_1_funny_string.py

4. วิธีการตรวจสอบ Code Coverage
หากต้องการดูความครอบคลุมของการทดสอบ (เป้าหมาย 100%):
coverage run -m unittest discover
coverage report


โครงสร้างไฟล์
แต่ละข้อจะแบ่งเป็น 2 ไฟล์หลัก:

  - step_X_...py - ไฟล์ Algorithm ต้นฉบับ
  - test_step_X_...py - ไฟล์ Unit Test