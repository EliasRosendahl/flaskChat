var socket = io.connect('http://' + document.domain + ':' + location.port);
$(document).ready(function(){ 
    $("#SendButton").click(function(){
        var input = $('#InputString').val();
        if(input !== ""){
            socket.emit('message', {msg: input});
            $('#InputString').val("");
        }
    });
});

socket.on('connect', function() {
    socket.emit('connectEvent', {data: 'I\'m connected!'});
});

socket.on('connectResponce', function(chatLog){
    console.log(chatLog);
    console.log("con resp");
    $('#ChatArea').val(chatLog);
})

socket.on('responce', function(msg){
    console.log(msg);
    if(msg !== ""){
        if($("#ChatArea").val() === "\n"){
        console.log("It's e");
        $("#ChatArea").val(msg);                    
        }
        else{
            $("#ChatArea").val( $("#ChatArea").val() + "\n" + msg);
        }    
    }
    
});