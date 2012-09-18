$(document).ready(function() {

	console.log('document ready');
	
	$('#buttonSubmit').live('click', function(e) {
		
		e.preventDefault();
		
		var data = {
			'name': $('#inputName').val(),
			'email': $('#inputEmail').val(),
			'comment': $('#inputComment').val()
		};
		
		console.log(data);
		
		var url = 'feedback.php';

		$.ajax({
			url: url,
			data: data,
			type: 'POST',
			dataType: 'json',
			success: function(data) {
				// console.log(data);
				var validation = data.validation;
				
				$('.control-group').removeClass('error');
				
				for(k in validation) {
					
					var v = validation[k];
					
					if (v.status != true) {
						if(k == 'email') {
							$('#inputEmail').parents('.control-group').addClass('error');
							$('.help-inline', $('#inputEmail').parents('.control-group')).html(v.error);
						}
						
						if(k == 'name') {
							$('#inputName').parents('.control-group').addClass('error');
							$('.help-inline', $('#inputName').parents('.control-group')).html(v.error);
						}
						
						if(k == 'comment') {
							$('#inputComment').parents('.control-group').addClass('error');
							$('.help-inline', $('#inputComment').parents('.control-group')).html(v.error);

						}
					} else {

						if(k == 'email') {
							$('#inputEmail').parents('.control-group').addClass('success');
						}
					}
					
					console.log(k, v);
				}
				
				
			}
		});
		
		
	});
	
});