Usage: run server.py then client.py

Need the while loop because the server buffer is only set to 20. So we need to keep recieving / sending until the entire message is done. Jank way of stopping it all though, by checking for hardcoded substring "@)" and "END". But theoretically, the server should persist even after the client leaves.
