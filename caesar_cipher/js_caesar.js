/*

Caesar Cipher using Javascript and NodeJS' Filesystem library.

Usage: 
To Cipher:
node js_caesar.js test.txt -c 9
To Decipher:
node js_caesar.js shifted_test.txt -d 9

Takes in three arguments: file name, -d or -c, and key to shift by.
Reads from file name, then shifts or unshifts based on -d or -c by key.
Writes shifted/unshifted output to the console, and writes it to a new 
file, with a name depending on whether it was shifted or un-shifted.

Mainly done for learning and practice with NodeJS file I/O, and general Javascript.

*/

var fs = require('fs');
var buffer = null;

if (process.argv.length != 5) {
	console.error("Expected 3 arguments, got " + process.argv.length + "\n");
	console.error("Expects first argument to be file name, second to be -d \n" +
		"for decipher or -c for cipher, and third to be the key to shift by");
	process.exit();
}

if (process.argv[3] != "-d" && process.argv[3] != "-c") {
	console.error("Expects second argument to be -d \n" +
		"for decipher or -c for cipher");
	process.exit();
}

var key = parseInt(process.argv[4]);

fs.open(process.argv[2].toString(), "r", (err, fd) => {
	if (err) {
		console.error("Something went wrong with opening file: " + process.argv[2]);
		process.exit();
	}
	getStats(fd);
});

////////////////////////////
///// FUNCTIONS ////////////
////////////////////////////

function getStats(filedesc) {
	fs.fstat(filedesc, function(err, stats) {
		if (err) {
			console.error("Something went wrong getting stats.");
			process.exit();
		}
		buffer = new Buffer(stats.size);
		console.log("buffer set to size " + stats.size);

		readFromFile(filedesc);
	})
}


function readFromFile(filedesc) {
	fs.read(filedesc, buffer, 0, buffer.length, 0, function(err, bytes) {
		if (err){
			console.error("Error reading from file");
			process.exit();
		}
		console.log(bytes + " bytes read\n");

		// If read in successfully
		if(bytes > 0){

			// Print what read in from file
			console.log("\n==================== \n")
			console.log(buffer.toString());
			console.log("\n==================== \n")

			// check argument to shift or unshift
			if (process.argv[3] == "-c") {
				caesarShift(filedesc);
			}
			else if (process.argv[3] == "-d") {
				caesarUnShift(filedesc);
			}
		}
	});
}

function caesarShift(filedesc) {

	for (var i = 0; i < buffer.length; i++) {
		if (buffer[i] != 10 && buffer[i] != 32 && buffer[i] != 46) {// ASCII for a newline or space or period. Dont shift those
			if (buffer[i] + key > 126) {
				buffer[i] = 33 + (buffer[i] + key - 126) // Wrap to beginning of 'convienent' characters
			} else {
				buffer[i] += key;
			}
		}
	}

	console.log(buffer.toString());
	console.log("\n==================== \n")

	// Close the file stream
	fs.close(filedesc, function(err){
		if (err){
			console.log(err);
		} 
		console.log("\nFile closed successfully.");
	});

	fs.open("shift_" + process.argv[2].toString(), "w+", (err, fd) => {
		if (err) {
			console.error("Something went wrong with opening file: " + process.argv[2]);
			process.exit();
		}
		writeToFile(fd);
	});
}

function caesarUnShift(filedesc) {

	for (var i = 0; i < buffer.length; i++) {
		if (buffer[i] != 10 && buffer[i] != 32 && buffer[i] != 46) { // ASCII for a newline or space or period. Dont shift those
			if (buffer[i] - key < 33) {
				buffer[i] = 126 - (33 - (buffer[i] - key)) // Wrap to beginning of 'convienent' characters
			} else {
				buffer[i] -= key;
			}
		}
	}

	console.log(buffer.toString());
	console.log("\n==================== \n")

	// Close the file stream
	fs.close(filedesc, function(err){
		if (err){
			console.log(err);
		} 
		console.log("\nFile closed successfully.");
	});

	fs.open("un-shift_" + process.argv[2].toString(), "w+", (err, fd) => {
		if (err) {
			console.error("Something went wrong with opening file: " + process.argv[2]);
			process.exit();
		}
		writeToFile(fd);
	});
}

function writeToFile(filedesc) {
	fs.write(filedesc, buffer, 0, buffer.length, 0, function(err, written) {
		if (err){
			console.error("Error writing to file");
			process.exit();
		}
		console.log(written + " bytes written\n");

	});

	fs.close(filedesc, function(err){
		if (err){
			console.log(err);
		} 
		console.log("\nFile closed successfully.");
	});
}








