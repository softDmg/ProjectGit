from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='attendance_db'
)

cursor = mydb.cursor()

@app.route('/login', methods = ['POST'])
def login():
    try:
        #Get Username and Password from the request
        data = request.json
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        sql = ""
        if role == 'admin':
            sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
        elif role == 'professor':
            sql = "SELECT * FROM professor WHERE username = %s AND password = %s"
        else:
            return jsonify({'message': 'Invalid role'})


        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        print(result)

        if result:
            data = {'message': 'User Login Successful'}
            return jsonify(data)
        else:
            print('User Login Failed')
            return jsonify({'message': 'User Login Failed'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500
    # finally:
    #     cursor.close()
    #     mydb.close()


if __name__ == '__main__':
    app.run(debug=True)