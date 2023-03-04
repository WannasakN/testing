def caesarCipher(s, k):
    encrypted = ""
    for char in s:
        if char.isalpha():
            char_code = ord(char)
            base_code = 65 if char.isupper() else 97 #หากเป็นตัวอักษรจะตรวจสอบว่าเป็นตัวพิมพ์ใหญ่หรือตัวพิมพ์เล็กโดยใช้ isupper() 
            shifted_code = (char_code - base_code + k) % 26 + base_code
            encrypted += chr(shifted_code) #จากนั้นแปลงตัวอักษรเป็นรหัส ASCII โดยใช้ ord() คำนวณรหัส ASCII ใหม่โดยใช้ค่าเปลี่ยน k และแปลงรหัสใหม่กลับเป็นอักขระโดยใช้ฟังก์ชัน chr()
        else:
            encrypted += char
    return encrypted
