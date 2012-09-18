
var httpRequest;


if (window.XMLHttpRequest) { // Mozilla, Safari, ...
	httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 8 and older
	httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
}





































httpRequest.onreadystatechange = function() {
	// process the server response
	/*
	 0 (uninitialized)
	 1 (loading)
	 2 (loaded)
	 3 (interactive)
	 4 (complete)
	 */

	if (httpRequest.readyState === 4) {
		// alert('orsc');

		if (httpRequest.status === 200) {
			// perfect!
			
			data = JSON.parse(httpRequest.responseText);
			// data = httpRequest.responseText;
			
			console.log(data);
			
		} else {
			// there was a problem with the request,
			// for example the response may contain a 404 (Not Found)
			// or 500 (Internal Server Error) response code
		}

	} else {
		// still not ready
	}

};





// make the request

var url = 'api.php';
var q = 'j'; 

httpRequest.open('GET', url);
httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
httpRequest.send('q=' + encodeURIComponent(q));







