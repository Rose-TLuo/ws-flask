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

    # 获取角色和段位信息
    survivor_role = request.form.get("survivor-role")
    hunter_role = request.form.get("hunter-role")
    
    # 段位信息
    survivor_rank = f"{request.form.get('survivor-star-from1', '无')}阶{request.form.get('survivor-star-from2', '无')} {request.form.get('survivor-star-from3', '无')}颗星"
    hunter_rank = f"{request.form.get('hunter-star-from1', '无')}阶{request.form.get('hunter-star-from2', '无')} {request.form.get('hunter-star-from3', '无')}颗星"

    # 目标信息（同样的格式）
    survivor_target_rank = f"{request.form.get('survivor-star-to1', '无')}阶{request.form.get('survivor-star-to2', '无')} {request.form.get('survivor-star-to3', '无')}颗星"
    hunter_target_rank = f"{request.form.get('hunter-star-to1', '无')}阶{request.form.get('hunter-star-to2', '无')} {request.form.get('hunter-star-to3', '无')}颗星"
    
    # 认知分信息
    point_now = request.form.get("survivor-point-now") or request.form.get("hunter-point-now")
    point_target = request.form.get("survivor-point-target") or request.form.get("hunter-point-target")

    order_id = str(uuid.uuid4())  # 生成唯一的订单编号

    print("收到提交：", boss_id, service_type, survivor_role if survivor_role else hunter_role, order_id)

    # 构建响应内容
    response_data = {
        "msg": "success", 
        "order_id": order_id, 
        "boss_id": boss_id, 
        "service_type": service_type,
        "price": price,
        "survivorRole": survivor_role,
        "hunterRole": hunter_role,
        "rank_now": survivor_rank if service_type == 'survivor' else hunter_rank,
        "rank_target": survivor_target_rank if service_type == 'survivor' else hunter_target_rank,
        "point_now": point_now,
        "point_target": point_target
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run()