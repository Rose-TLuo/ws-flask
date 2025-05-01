from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 添加这行代码来启用CORS，对所有路由开放跨域

@app.route("/")
def home():
    return "你好，这里是后端接口！"

@app.route("/api/submit_order", methods=["POST"])
def submit_order():
    boss_id = request.form.get("boss-id")
    service_type = request.form.get("service-type")
    # 其他字段同理……
    print("收到提交：", boss_id, service_type)
    return jsonify({"msg": "success", "boss_id": boss_id, "service_type": service_type})

if __name__ == "__main__":
    app.run()