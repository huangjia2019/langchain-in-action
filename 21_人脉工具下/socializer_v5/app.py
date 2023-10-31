# 导入所需的库和模块
from flask import Flask, render_template, request, jsonify
from findbigV import find_bigV
import json

# 实例化Flask应用
app = Flask(__name__)

# 主页路由，返回index.html模板
@app.route("/")
def index():
    return render_template("index.html")

# 处理请求的路由，仅允许POST请求
@app.route("/process", methods=["POST"])
def process():
    # 获取提交的花的名称
    flower = request.form["flower"]
    # 使用find_bigV函数获取相关数据
    response_str = find_bigV(flower=flower)
    # 使用json.loads将字符串解析为字典
    response = json.loads(response_str)

    # 返回数据的json响应
    return jsonify(
        {
            "summary": response["summary"],
            "facts": response["facts"],
            "interest": response["interest"],
            "letter": response["letter"],
        }
    )    

# 判断是否是主程序运行，并设置Flask应用的host和debug模式
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
