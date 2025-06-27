from flask import Flask, request

app = Flask(__name__)

@app.route('/api/notify-bg-done', methods=['POST'])
def notify_bg_done():
    data = request.json
    print("新图片处理完成：", data)
    # 这里可以扩展为写入你主项目数据库、发消息等
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=8000) 