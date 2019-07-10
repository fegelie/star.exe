from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return a

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetIntenntRequest']['payload'][data]['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
    if (userText == 'hitler') :
        sendText(user,'Adolf hitler is the German persidrent in the Nazi republic.')
    elif (userText == 'America') :
        sendText(user,'ขยะ')
    elif (userText == 'Sieg Heil') :
        sendText(user,'Heil hitler')
    elif (userText == 'คนที่ผมชอบ') :
        sendText(user,'น้องนนท์ของท่านผู้นำไง แล้วท่านก็อย่านอกใจละ')
    elif (userText == 'ใครน่ารัก') :
        sendText(user,'น้องนนท์ของท่านผู้นำไง ละ')
    elif (userText == 'SS') :
        sendText(user,'Schutzstaffel หรือ เอ็สเอ็ส (SS, "ᛋᛋ" ที่เป็นอักษรรูน) เป็นองค์กรกำลังกึ่งทหารสังกัดพรรคนาซีภายใต้คำสั่งของอดอล์ฟ ฮิตเลอร์ เดิมมีชื่อองค์กรว่า ซาล-ซุทซ์ (Saal-Schutz) ซึ่งมีสมาชิกเป็นอาสาสมัครของพรรคนาซีเพื่อคุ้มกันและดูแลความปลอดภัยในการประชุมพรรคที่เมืองมิวนิก เมื่อไฮน์ริช ฮิมเลอร์เข้าร่วมองค์กรในปีค.ศ. 1925 ก็มีการเปลี่ยนชื่อหน่วยเป็น "ชุทซ์ชตัฟเฟิล" เอ็สเอ็สภายใต้การนำของฮิมเลอร์ได้ขยายตัวจากมีสมาชิกสองร้อยคนกลายเป็นองค์กรขนาดมหึมาที่มีสมาชิกกว่าล้านคนและกลายเป็นหนึ่งในองค์กรที่มีอิทธิพลที่สุดในเยอรมนี หน้าที่ขององค์กรนี้คือสอดส่องดูแลความมั่นคงภายในไรช์')
    elif (userText == 'ท่านจะจงรักภักดีและจะไม่มีวันทรยศต่อแผ่นดินนี้หรือไม่') :
        sendText(user,'ใช่ครับ-ข้าพเจ้า เป็นทหารแห่งกองทัพบกไทยข้าพเจ้า จะปฎิบัติหน้าที่เพื่อชาติ ศาสตร์ กษัตริย์และประชาชนข้าพเจ้า จะปฏิบัติงานของตนและสนับสนุนผู้อื่นเพื่อประโยชน์ของชาติเป็นสำคัญ ข้าพเจ้า จะมีความทรหดอดทนทั้งร่างกายและจิตใจ ข้าพเจ้า จะมุ่งมั่นในการฝึกอย่างไม่ย่อท้อ ให้มีความเชี่ยวชาญในการรบ เพื่อชัยชนะ ข้าพเจ้า จะทุ่มเทปฎิบัติภารกิจให้สำเร็จ ข้าพเจ้า จะต่อสู้เคียงข้างประชาชน เพื่อจำกัดศัตรูของชาติ ข้าพเจ้า จะพิทักษ์รักษา เอกราช และราชบัลลังก์ไว้ด้วยชีวิต ข้าพเจ้า จะไม่ทอดทิ้งเพื่อนทหารไม่ว่าจะบาดเจ็บหรือเสียชีวิต เป็นอันขาด')
    elif (userText == 'Nazi') :
        sendText(user,'Sieg Heil')
    elif (userText == 'Soviet') :
        sendText(user,'communist ')
    return '',200
def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
