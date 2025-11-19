# 🎮 XO Game - Tic Tac Toe

> เกม XO (Tic Tac Toe) สุดคลาสสิก! เล่นกับบอทอัจฉริยะที่ใช้ Minimax Algorithm ในธีมดำขาวสวยงาม ✨

## 🌟 ฟีเจอร์หลัก

- **🎯 เล่นกับบอทอัจฉริยะ**: บอทใช้ Minimax Algorithm เดินอย่างเก่งที่สุด ไม่มีทางแพ้ได้ง่ายๆ!
- **🎨 UI สวยทันสมัย**: ธีมดำขาว minimalistic กับ emoji ❌ และ ⭕ ให้ดูน่ารัก
- **🔄 เริ่มเกมใหม่**: ปุ่มรีเซ็ตเกมง่ายๆ ด้วยไอคอน 🔄
- **📱 Responsive Design**: ปรับขนาดหน้าต่างและปุ่มให้เหมาะกับการเล่น
- **🏆 แสดงผลชนะ**: Highlight แถวที่ชนะด้วยสีเหลืองสดใส

## 🛠️ สิ่งที่ใช้พัฒนา

- **ภาษา**: Python 3.11
- **GUI Framework**: PyQt6
- **AI Algorithm**: Minimax with Alpha-Beta Pruning (optimized)
- **ธีม**: Modern Dark & White Theme ด้วย QSS

## 📦 การติดตั้ง

### ข้อกำหนดเบื้องต้น
- Python 3.8+ (แนะนำ 3.11)
- PyQt6 (ติดตั้งอัตโนมัติจาก requirements.txt)

### ขั้นตอนติดตั้ง
1. **โคลนหรือดาวน์โหลดโปรเจกต์** ไปที่โฟลเดอร์ เช่น `f:\โปรแกรม\XO`

2. **เปิด PowerShell** และไปที่โฟลเดอร์โปรเจกต์:
   ```powershell
   cd "f:\โปรแกรม\XO"
   ```

3. **สร้าง Virtual Environment** (แนะนำ):
   ```powershell
   & "C:/Program Files/Python311/python.exe" -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. **ติดตั้ง Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

   *หากไม่มี `requirements.txt`, ติดตั้ง PyQt6 เอง:*
   ```powershell
   pip install PyQt6
   ```

## 🚀 วิธีรันเกม

### รันปกติ
```powershell
# เปิดจากโฟลเดอร์โปรเจกต์
& "C:/Program Files/Python311/python.exe" xo_game.py
```

หรือถ้า Python อยู่ใน PATH:
```powershell
python xo_game.py
```

### เปิด GUI
- หน้าต่างเกมจะปรากฏขึ้น
- คลิกที่ช่องว่างเพื่อใส่ ❌ (ผู้เล่น)
- บอทจะเดิน ⭕ อัตโนมัติ
- เมื่อจบเกม กด "🔄 New Game" เพื่อเริ่มใหม่

## 🎮 วิธีเล่น

1. **เริ่มเกม**: ผู้เล่นเป็น ❌ (สีแดง), บอทเป็น ⭕ (สีน้ำเงิน)
2. **เดินหมาก**: คลิกช่องว่างเพื่อใส่สัญลักษณ์
3. **รอบอท**: บอทจะคิดและเดินภายในไม่กี่วินาที
4. **ชนะ/แพ้/เสมอ**: ตรวจสอบสถานะด้านบน
5. **รีเซ็ต**: กดปุ่ม 🔄 New Game เพื่อเล่นรอบใหม่

### เป้าหมาย
- จัดสัญลักษณ์ 3 ตัวในแถว/คอลัมน์/แนวทแยงก่อนบอท!

## 🐛 แก้ปัญหา

### Unicode/Emoji ไม่แสดงผล
หาก emoji ไม่แสดงในบางคอนโซล Windows:
```powershell
$OutputEncoding = [System.Text.UTF8Encoding]::new()
```

### PyQt6 ไม่พบ
```powershell
pip install PyQt6
```

### Syntax Error
ตรวจสอบโค้ด:
```powershell
& "C:/Program Files/Python311/python.exe" -m py_compile xo_game.py
```

## 📝 โครงสร้างโค้ด

```
xo_game.py
├── TicTacToeGame (คลาสหลัก)
│   ├── initUI()          # ตั้งค่า UI และธีม
│   ├── on_button_click() # จัดการคลิกผู้เล่น
│   ├── bot_move()        # AI เดินหมาก
│   ├── minimax()         # Algorithm สำหรับ AI
│   ├── check_winner()    # ตรวจสอบผู้ชนะ
│   ├── highlight_winner()# Highlight แถวชนะ
│   └── new_game()        # รีเซ็ตเกม
├── requirements.txt      # Dependencies
└── README.md             # ไฟล์นี้
```

## 🎨 ปรับแต่งธีม

แก้ไขใน `initUI()`:
- **เปลี่ยนสี**: แก้ QSS string
- **เปลี่ยน emoji**: แก้ `'❌'` และ `'⭕'`
- **ปรับขนาด**: แก้ `setFixedSize()` และ font sizes

## 📈 แผนพัฒนาในอนาคต

- [ ] เพิ่มโหมด 2 ผู้เล่น
- [ ] เลือกความยากของ AI
- [ ] เก็บสถิติเกม
- [ ] เพิ่มเสียงและเอฟเฟกต์
- [ ] รองรับธีมอื่นๆ

## 📄 ลิขสิทธิ์

โปรเจกต์นี้เป็นโอเพนซอร์ส สามารถแก้ไขและแจกจ่ายได้ตาม MIT License.

---

**สนุกกับการเล่น XO Game!** 🎉 ถ้ามีคำถามหรือต้องการเพิ่มฟีเจอร์ บอกได้เลย! 🚀#


