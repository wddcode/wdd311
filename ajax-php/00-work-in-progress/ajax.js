var httpRequest;


if (window.XMLHttpRequest) { // Mozilla, Safari, ...
	httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 8 and older
	httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
};

httpRequest.onreadystatechange = function() {
	
	var state = httpRequest.readyState;

	if(state == 4) {
		console.log('state: completed');
		
		if (httpRequest.status === 200) {
		// weiter
		
		var result = httpRequest.responseText;
		
		var result = JSON.parse(result);
		
		
		/*
		for(r in result) {
			console.log(result[r]);
		}
		*/
		
		console.log(result);
		
			
		} else {
			alert('error: ' + httpRequest.status);
		}
		
	}
	
};


var url = 'api.php?q=jo';
httpRequest.open('GET', url);
httpRequest.send();

