// Instantiate the package to work with TCP, "net.js"
var net = require("net");

// Creating a array to put all clients "sockets" connected
var clientList = [];
var ids = 0

// Creating a server from "net" object 
var servidor =  net.createServer(function(client){
 // Adding all client who conect to server to clientList
 client.id = ids++
 clientList.push(client);
 client.write("ndijniunjisui\n");
 console.log(clientList[ids-1]);
 // Event actived every time a client connect to server
 client.on('connection', function(){
  // Printing on server the client ID
  console.log(client.id+" connected!");
 });
 
 // Event actived every time a client send data to server
 client.on('data', function(data){

  clientList.forEach(function(socket, index, array){
         if(socket != client){
    		socket.write(data+"\n");
		console.log('Data sent');
         }
	
         
	 
	});
    });
  
  
 
 // Event actived every time a client desconnect from server
 client.on('end', function(){
  // finding the position of desconected client
  var i = clientList.indexOf(client);
  // excluding the client from list
  clientList.splice(i, 1);
  // print a message of desconnection from a client 
  console.log(client.id+" desconnected!");
 });
});

// Setting the port to listen
servidor.listen(6066);

// Printing a message of success on server
console.log("TCP Server connected on 127.0.0.1 port 6066, waiting connections!!!");
