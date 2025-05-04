import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "你好，这里是后端接口！"

@app.route("/api/submit_order", methods=["POST"])
def submit_order():
    boss_id = request.form.get("boss-id")
    service_type = request.form.get("service-type")
    price = request.form.get("price")
    role = request.form.get("survivor-role") or request.form.get("hunter-role")
    
    # 段位信息
    rank_now = request.form.get("survivor-rank-now") or request.form.get("hunter-rank-now")
    rank_target = request.form.get("survivor-rank-target") or request.form.get("hunter-rank-target")
    
    # 认知分信息
    point_now = request.form.get("survivor-point-now") or request.form.get("hunter-point-now")
    point_target = request.form.get("survivor-point-target") or request.form.get("hunter-point-target")

    order_id = str(uuid.uuid4())  # 生成唯一的订单编号

    print("收到提交：", boss_id, service_type, role, order_id)

    # 构建响应内容
    response_data = {
        "msg": "success", 
        "order_id": order_id, 
        "boss_id": boss_id, 
        "service_type": service_type,
        "price": price
    }

    if service_type in ['survivor', 'hunter']:
        response_data.update({
            "role": role,
            "rank_now": rank_now,
            "rank_target": rank_target,
            "point_now": point_now,
            "point_target": point_target
        })

    return jsonify(response_data)

if __name__ == "__main__":
    app.run()