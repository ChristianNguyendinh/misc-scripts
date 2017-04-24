// Basic connection to a postgresDB

var pg = require('pg');

var conString = 'postgres://localhost:5432/<DB_NAME>'

pg.connect(conString, (err, client) => {
    if (err) return console.error(err);

    client.query('SELECT * FROM test;', (err, result) => {
        if (!err) {
            for (let i = 0; i < result.rowCount; i++) {
                console.log("GOT DATA: id: %s, name: %s", result.rows[i].id, result.rows[i].name);
            }
        }
    }).then(() => client.end());
});