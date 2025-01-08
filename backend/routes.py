from flask import jsonify, request, send_from_directory


def setup_routes(app, mysql):
    @app.route('/api/users', methods=['GET'])
    def get_users():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user_profiles")
        users = cur.fetchall()
        cur.close()
        app.logger.debug("Fetched Users: %s", users)
        return jsonify(users)

    # API Endpoint untuk menambahkan pengguna
    @app.route('/api/users', methods=['POST'])
    def add_user():
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        address = request.json['address']
        phone_number = request.json['phone_number']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO user_profiles (first_name, last_name, address, phone_number) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, address, phone_number)
        )
        mysql.connection.commit()
        cur.close()
        app.logger.debug("User added: %s %s - %s - %s", first_name, last_name, address, phone_number)
        return jsonify({"message": "User added successfully!"}, 201)

    @app.route('/')
    def home():
        return send_from_directory('../frontend', 'index.html')

    @app.route('/<path:filename>')
    def serve_static(filename):
        return send_from_directory('../frontend', filename)
