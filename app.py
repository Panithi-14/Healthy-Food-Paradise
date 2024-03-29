from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__, static_folder='static')

categories = {
    'Meat': {'image': 'c1.jpg', 'description': 'Healthy meat options'},
    'Seafood': {'image': 'c2.jpg', 'description': 'Fresh and nutritious seafood'},
    'Plant Based': {'image': 'c3.jpg', 'description': 'Vegetarian and plant-based choices'},
    'Snack': {'image': 'c4.jpg', 'description': 'Healthy snack alternatives'},
}

menu_items = {
    'Meat': [
        {'name': 'อกไก่ปิ้ง', 'description': 'เมนูอกไก่คลีนยอดฮิตที่ดัดแปลงจากเมนูอาหารเช้าที่เราคุ้นเคยกันอย่างดี ไม่มีไขมันเลว แถมยังได้โปรตีนเน้นๆ อีกด้วย', 'image': 'm1.jpg'},
        {'name': 'โจ๊กไก่ข้าวไรซ์เบอร์รี', 'description': 'เมนูอาหารคลีนแบบประหยัด แถมอิ่มท้องจากข้าวไรซ์เบอร์รีและได้โปรตีนจากไก่อีกด้วย', 'image': 'm2.jpg'},
        {'name': 'ไข่ยัดไส้เต้าหู้หมูสับ', 'description': 'อาหารคลีนง่ายๆ “ไข่ยัดไส้เต้าหู้หมูสับ” เมนูนวลๆ รสนุ่มเหมาะกับทำเป็นอาหารกลางวันใส่กล่องไปกินที่ออฟฟิศก็ได้ สละเวลาทำไม่ถึง 20 นาที ก็ได้อาหารคลีนหน้าตาน่ากิน รสชาติประทับใจมาลองชิมกันแล้ว!', 'image': 'm3.jpg'},
        {'name': 'อกไก่ย่างอะโวคาโด', 'description': '“อกไก่ย่างอะโวคาโด” เมนูอาหารคลีนง่ายๆ ใช้เวลาไม่นาน และถึงแม้อะโวคาโดจะมีไขมันอยู่มาก แต่ไม่ทำให้เสียสุขภาพแน่นอน แถมยังช่วยลดระดับไขมันเลวในร่างกายได้อีกด้วย', 'image': 'm4.jpg'},
    ],
    'Seafood': [
        {'name': 'ซุปอะโวคาโดแซลมอนย่าง', 'description': '“ซุปอะโวคาโดแซลมอนย่าง” เมนูอาหารคลีนง่ายๆ ทำไว้ซดร้อนๆ รับเช้าวันใหม่อันสดใสได้ดีทีเดียว แถมยังมีแซลมอนย่างช่วยเสริมไขมันดีและโอเมก้า 3 อีกด้วย', 'image': 's1.jpg'},
        {'name': 'โจ๊กไข่ขาวกุ้งไมโครเวฟ', 'description': 'เมนูอาหารคลีนเอาใจเด็กหอ “โจ๊กไข่ขาวกุ้งไมโครเวฟ” นอกจากจะเป็นเมนูอาหารคลีนแบบประหยัดแล้ว ยังทำตามง่าย ใช้วัตถุดิบไม่เยอะ ไม่ต้องมีหม้อก็ทำได้!', 'image': 's2.jpg'},
        {'name': 'สเปรดอะโวคาโดโฮมเมด', 'description': '“สเปรดอะโวคาโดโฮมเมด” สูตรอาหารคลีนที่สามารถทำกินคู่กับแซนด์วิชยามเช้า โปะด้วยแซลมอนสโมก อีกทั้งยังได้เสริมไขมันดีจากอะโวคาโดอีกด้วย', 'image': 's3.jpg'},
        {'name': 'สเต๊กปลาดอร์รี', 'description': '“สเต๊กปลาดอร์รี” เมนูง่าย ๆ เป็นอาหารคลีนตอนเย็นที่กินได้แบบไม่รู้สึกผิด เพราะปลาดอร์รี่มีไขมันน้อย ลีน ยิ่งกินคู่กับผักสลัดและน้ำจิ้มแจ่ว ยิ่งแซ่บ แถมมีประโยชน์อีกต่างหาก', 'image': 's4.jpg'},
        {'name': 'ปลานึ่งสมุนไพร', 'description': '“ปลานึ่งสมุนไพร” เมนูอาหารคลีนแบบประหยัดที่มีโปรตีนสูง อัดแน่นไปด้วยวิตามิน ที่สำคัญไขมันต่ำ เหมาะกับสาวๆที่กำลังมองหาอาหารคลีนสำหรับมื้อเย็นแบบสุดๆ', 'image': 's5.jpg'},
        {'name': 'ยำสลัดอะโวคาโดกุ้ง', 'description': '“ยำสลัดอะโวคาโดกุ้ง” เมนูอาหารคลีนตอนเย็นที่ประกอบไปด้วยอะโวคาโด ผลไม้ที่อุดมไปด้วยกรดไขมันดี มีประโยชน์ต่อร่างกายในการลดปริมาณคอเลสเตอรอล ยิ่งกินคู่กับน้ำยำแซ่บๆ รับรองเลยว่าจะหลงรักอาหารคลีนเมนูนี้แบบโงหัวไม่ขึ้น!', 'image': 's6.jpg'},
    ],
    'Plant Based': [
        {'name': 'บะหมี่ผักน่องไก่นึ่ง', 'description': 'เมนูอาหารคลีน “บะหมี่ผักน่องไก่นึ่ง” ที่บอกเลยว่าได้ชิมแล้วจะฟินมาก บะหมี่ผักเหนียวนุ่มกินคู่กับอกไก่ฉ่ำๆ ใครมองหาไอเดียเมนูอาหารคลีนสำหรับแพ็คใส่กล่องกินเป็นมื้อเที่ยง ขอแนะนำเลยย', 'image': 'v1.jpg'},
        {'name': 'บะหมี่ผักผัดรวมมิตร', 'description': '”บะหมี่ผักผัดรวมมิตร” เมนูอาหารคลีนอัดแน่นด้วยเครื่องล้นจาน กุ้งตัวโต ที่มาพร้อมผักเน้นๆ เมนูเดียวได้รับอาหารครบถ้วนทุกหมู่แน่นอน ลองชิมแล้วจะวางไม่ลง', 'image': 'v2.jpg'},
        {'name': 'สปาเกตตีโฮลวีตผัดซอสมะเขือเทศ', 'description': '“สปาเกตตีโฮลวีตผัดซอสมะเขือเทศ” เมนูเส้นแบบโฮลวีตโดยตัวซอสเราจะใช้อกไก่สับ ยังคงไม่ทิ้งโปรตีนไปไหน สำหรับสายคลีนเมนูนี้จัดว่าเด็ด', 'image': 'v3.jpg'},
        {'name': 'สลัดเต้าหู้กับปลากะพง', 'description': '“สลัดเต้าหู้กับปลากะพง” เมนูสลัดโปรตีนแน่น ทั้งจากปลากะพงชิ้นโตและจากเต้าหู้จี่กรอบนอกนุ่มใน เสิร์ฟมาพร้อมน้ำสลัดงา เป็นเมนูง่ายๆ ที่จะเป็นมื้อกลางวันก็อิ่ม เป็นมื้อเย็นก็สบายท้อง', 'image': 'v4.jpg'},
        {'name': 'ลาบเห็ด', 'description': '“ลาบเห็ด” เมนูอาหารคลีนง่ายๆ สไตล์อีสาน แซ่บนัวครบรส ไม่ว่าจะเป็นรสเผ็ด เปรี้ยว และหวานนิดหน่อย รับรองประโยชน์แน่นจาน', 'image': 'v5.jpg'},
        {'name': 'พริกหวานยัดไส้ไขมันต่ำ', 'description': '“พริกหวานยัดไส้ไขมันต่ำ” อีกหนึ่งเมนูอาหารคลีนสุดครีเอทีฟ แถมเจ้าพริกหวานนี้ยังมีสารต้านอนุมูลอิสระ ช่วยคลายเครียด ยกกระตุ้นการทำงานของระบบย่อยอาหารอีกด้วย ดีขนาดนี้จะพลาดได้อย่างไร', 'image': 'v6.jpg'},
        {'name': 'ผัดฟักทองใส่ไข่', 'description': '“ผัดฟักทองใส่ไข่” เมนูผัดผักสีเหลืองสดใส รสชาติกลมกล่อม เบาสบายท้องสำหรับมื้อเย็น จะกินคู่กับข้าวไรซ์เบอร์รี ข้าวกล้อง หรือจะกินเปล่าๆ ก็ได้เลยย', 'image': 'v7.jpg'},
    ],
    'Snack': [
        {'name': 'แพนเค้กไร้แป้ง', 'description': '“แพนเค้กไร้แป้ง” อาหารเช้าคลีนง่ายๆ แพนเค้กนุ่ม หอม กลิ่นยั่วยวนชวนน้ำลายสอ แถมไม่มีแป้งอีกต่างหาก อิ่มท้องแถมดีต่อสุขภาพอย่างนี้ ไม่ลองได้ไง!', 'image': 'k1.jpg'},
        {'name': 'ลูกชิ้นอกไก่ย่าง', 'description': '“ลูกชิ้นอกไก่ย่าง” เมนูอาหารคลีนแบบประหยัดจะทำกินเล่นก็ได้ หรือจะทำเป็นมื้อเย็นก็ดี ถือเป็นอาหารคลีนสุดเก๋ แถมรสชาติไม่จำเจอีกด้วย!', 'image': 'k2.jpg'},
        {'name': 'แซนด์วิชกะเพราอกไก่ไข่ดาว', 'description': '“แซนด์วิชกะเพราอกไก่ไข่ดาว” เมนูกึ่งเช้ากึ่งกลางวัน เริ่มต้นวันแบบจัดจ้าน สูตรนี้เราก็ใช้ขนมปังโฮลวีต และใช้สเปรย์น้ำมันแค่พอผัดไม่ติดกระทะ รับรองว่ากะเพราหอมกับขนมปังนุ่มๆ มันเข้ากันจริงๆ', 'image': 'k3.jpg'},
        {'name': 'เบอร์เกอร์ข้าวกล้องอกไก่', 'description': 'ใครจะไปคิดว่าเบอร์เกอร์จะเป็นอาหารคลีนได้ แต่วันนี้เรามีสูตรเด็ดมาเสนอกับ “เบอร์เกอร์ข้าวกล้องอกไก่” สูตรอาหารคลีนกินได้ ดีต่อสุขภาพ ทำใส่กล่องไปปิกนิกชิลๆ ก็ได้นะเออ', 'image': 'k4.jpg'},
    ],
}

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/menu/<category>')
def show_menu(category):
    if category not in menu_items:
        return redirect(url_for('index'))

    menu_category = menu_items[category]
    random_item = random.choice(menu_category)

    return render_template('menu.html', category=category, menu_item=random_item)

if __name__ == '__main__':
    app.run(debug=True)
