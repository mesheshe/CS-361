var mysql = require('mysql');
var pool = mysql.createPool({
    connectionLimit: 10,
    host: 'localhost',
    user : 'root',
    password: 'password',
    database: 'dcb',
    port: '3306',
    debug: false
})

module.exports.pool = pool;