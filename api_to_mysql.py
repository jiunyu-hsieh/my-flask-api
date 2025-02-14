# 示例：用Python Flask写API（文件名：app.py）
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    # 连接数据库（用你注册时获得的信息替换下面内容）
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="xjy20000506",
        database="charitydb"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Donations")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run()