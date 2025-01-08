from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin2025'
app.config['MYSQL_DB'] = 'simple_db'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')


# API ENDPOINT #

# Get all user profile
@app.route('/user', methods=['GET'])
def get_user():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user_profiles")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


# Create user profiles
@app.route('/user', methods=['POST'])
def add_user():
    firstName = request.json['first_name']
    lastName = request.json['last_name']
    address = request.json['address']
    phoneNumber = request.json['phone_number']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO user_profiles (first_name, last_name, address, phone_number) VALUES (%s, %s, %s, %s)",
        (firstName, lastName, address, phoneNumber)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User profile added successfully!"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
