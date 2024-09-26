import socketIO from "socket.io-client";


const socket= socketIO(`http://localhost:4000`, {
    transport: ["websocket"],
  });      

export default socket