const bodyParser = require('body-parser');
const express = require('express');
const mysql = require('mysql2');

const app = express()
const port = 6000;

// Json Parser Middleware
app.use(bodyParser.json())

// Mysql Connection Configuration
const db = mysql.createConnection({
    host: '172.17.0.4',
    port: 3306,
    user: 'admin',
    password: 'Admin2025',
    database: 'simple_db'

});

// Connection Check
db.connect((err) => {
    if (err){
        console.error('Connection Failed.. ', err);
    } else {
        console.log('Connection Succeed..');
    }
});

// GET all user_profiles
app.get('/api/users', (req, res) => {
    db.query('SELECT * FROM user_profiles', (err, results) => {
        if (err) {
            console.error(err);
        } else {
            res.json(results);
        }
    });
});

// CREATE new user_profile
app.host('/api/users', (req, res) => {
    const { first_name, last_name, address, phone_number } = req.body;
    const sql = 'INSERT INTO user_profiles (first_name, last_name, address, phone_number) VALUES (?, ?, ?, ?)';
    db.query(sql, [first_name, last_name, address, phone_number], (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).json({ error: 'Failed to add data' });
        } else {
            res.json({ message: 'Data added succesfully...', id: result.insertId });
        }
    })
});

// start server
app.listen(port, () => {
    console.log('Server running in http://localhost:$port}');
});