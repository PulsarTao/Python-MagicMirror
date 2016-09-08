$(document).ready(function(){
	console.log("文档加载完毕");
	
	var julius = new Julius();
	console.log("Require Success");
	julius.onrecognition = function(sentence) {
	    console.log(sentence);
	    $("audio").remove();
	    sendMessage(sentence);
	};
	
	$("#send").click(function(){
		$("audio").remove();
		if(checkMessage()){
			var message =$("#message").val();
			sendMessage();
		}
	});
	$(document).keyup(function(e){
	    if (e.keyCode == 27) 
	    {
	    	if(checkMessage()){
	            sendMessage();
	    	}
	    }
	})
});
function checkMessage(){
	if($("#message").val()!==""&&$("#message").val()!==null){
		return true;
	}else{
		return false;
	}
}
function sendMessage(Sdata){
	$.ajax({
		url:"/roobot",
		dataType:"html",
		type:"POST",
		data:{"message":Sdata},
		success:function(data){
			var Video="<audio autoplay='autoplay' style='display:none;'><source src='data:audio/x-mpeg;base64,"+data+"'></source></audio>";
			$("body").append(Video);
		},
		complete:function(){
			console.log("消息加载完毕");
		}
	});
}