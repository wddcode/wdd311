$(document).ready(function() {

	console.log('docoment ready');
		
	var avtive_result = -1;
	var active_value = '';
	var active_id = false;
	var active_data = new Array;
	
	$('#input_1').live('change', function(e) {
		if($(this).val() != active_value) {
			avtive_result = -1;
		}
	});	
		
	$('#input_1').live('keyup', function(e) {
		
		console.log(e.keyCode);
		
		var value = $(this).val();
		
		if(value.length < 2) {
			$('#display_1').html('');
			return;
		}
		
		
		if(e.keyCode == 40 || e.keyCode == 38) {

			$('ul#display_1 > li').removeClass('active');

			if(e.keyCode == 40) {
				avtive_result += 1;
			}
			if(e.keyCode == 38) {
				avtive_result -= 1;
			}
			
			$('#result_' + avtive_result).addClass('active');
			
			return;
		}
		
		if(e.keyCode == 13) {
			id = $('span.id', $('li.active')).html();
			update_data(id);
			return;	
		}
		

		var url = 'api.php?q=' + value;

		$.ajax({
			url: url,
			dataType: 'json',
			success: function(data) {
				$('#display_1').html('');
				console.log(data);
				
				
				for(i in data) {
					
					
					var html = '<li id="result_' + i + '">';
					
					html += '<span class="id">' + data[i]['id'] + '</span> ';
					html += '<span class="name">' + data[i]['name'] + '</span> ';
					html += '<span class="email">' + data[i]['email'] + '</span>';
					html += '</li>';
					
					
					$('#display_1').append(html);
					
					
					active_data[data[i]['id']] = data[i];
					
				}
			}
		});

	});
	
	$('ul#display_1 > li').live('click', function(e) {
		var id = $('span.id',this).html();
		update_data(id);
	});
	
	update_data = function(id) {
		var data = active_data[id];
		
		$('#input_1').val(data['name']);
		$('#display_1').html('');
		
		var form = $('#update_form');
		
		$('.name', form).val(data['name']);
		$('.email', form).val(data['email']);
		$('.id', form).val(data['id']);
		
	}
	
	
	
	
	
	$('#update_form .submit').live('click', function(e) {
		
		e.preventDefault();
		
		var form = $('#update_form');
		
		data = {
			'name': $('.name', form).val(),
			'email': $('.email', form).val(),
			'id': $('.id', form).val(),
		};
		
		var url = 'api.php';

		$.ajax({
			url: url,
			data: data,
			type: 'POST',
			dataType: 'json',
			success: function(data) {
				console.log(data);
				$('#update_form .result').append(data.message + '<br />');
			}
		});

	});
	
});



	


