/*
 * AutocompleteUi
 */


AutocompleteUi = function() {

	var self = this;
	
	this.api_url = false;
	this.input_form_id = false;
	this.edit_form_id = false;
	
	
	this.active_result = -1;
	this.active_value = '';
	this.active_id = false;
	this.active_data = new Array;
	
	
	this.init = function() {
		
		console.log('init AutocompleteUi');
		self.bindings();
		self.iface();
	};
	
	this.iface = function() {
		
	};

	this.bindings = function() {
				
		self.ac_input = $('input', $('#' + self.input_form_id));
		self.ac_input_result = $('ul.autocomplete', $('#' + self.input_form_id));

		self.ac_edit_form = $('#' + self.edit_form_id);
		
		// AUTOCOMPLETE PART
		
		// reset on change
		self.ac_input.live('change', function(e) {
			if($(this).val() != self.active_value) {
				self.avtive_result = -1;
			}
		});	
		
		// keyup handler
		self.ac_input.live('keyup', function(e) {
			// console.log(e.keyCode);
			
			// get the current value from input
			var value = $(this).val();
			
			// empty the result display
			if(value.length < 2) {
				self.ac_input_result.html('');
				return;
			}
			
			// catch keyup / keydown
			if(e.keyCode == 40 || e.keyCode == 38) {
				
				e.preventDefault();
	
				$('li', self.ac_input_result).removeClass('active');
	
				if(e.keyCode == 40) {
					// make sure not going abov max results					
					if(self.active_result < self.object_size(self.active_data)) {
						self.active_result += 1;
					}
				}
				if(e.keyCode == 38) {
					// make sure not going below -1
					if(self.active_result >= 0) {
						self.active_result -= 1;
					}
				}
				
				console.log(self.active_result, 'active result');
				
				$('#result_' + self.active_result).addClass('active');
				
				return;
			}
			
			// catch return key
			if(e.keyCode == 13) {
				e.preventDefault();
				id = $('span.id', $('li.active', self.ac_input_result)).html();
				self.set_ac_result(id);
				return;	
			}
			
			// nothing catched, process with lookup
			self.get_ac_result(value);
			
			
		});	
		
		// click handler for ac_results
		$('li', self.ac_input_result).live('click', function(e) {
			var id = $('span.id',this).html();
			self.set_ac_result(id);
		});
		
		// set focus on ac_input
		self.ac_input.focus();
		
		
		// EDIT PART
		$('button.submit', self.ac_edit_form).live('click', function(e) {
			e.preventDefault();
			self.post_form();
		});
		$('button.reset', self.ac_edit_form).live('click', function(e) {
			e.preventDefault();
			$('input', self.ac_edit_form).val('')
			self.reset_ac();
		});
		
		
		
		// GENERAL PART
		
		// prevent form submit
		$(window).keydown(function(event){
			if(event.keyCode == 13) {
				event.preventDefault();
				return false;
			}
		});
	
	};
	
	this.get_ac_result = function(value) {
		
		var url = self.api_url + '?q=' + value;
		
		// reset active data
		self.active_data = [];
		self.ac_input_result.html('');
		
		$.getJSON(url, function(data) {
				
			
			// loop the result
			for(i in data) {
				// compose every result element (quite hackish here...)
				var html = '<li id="result_' + i + '">';				
				html += '<span class="id">' + data[i]['id'] + '</span> ';
				html += '<span class="name">' + data[i]['name'] + '</span> | ';
				html += '<span class="email">' + data[i]['email'] + '</span>';
				html += '</li>';
				
				self.ac_input_result.append(html);
				
				// populate active data
				self.active_data[data[i]['id']] = data[i];
				
			}
		});
	};
	
	this.set_ac_result = function(id) {
		if(id) {
			var data = self.active_data[id];
			
			self.ac_input.val(data['name']);
			self.ac_input_result.html('');
						
			var edit_form = $('#' + self.edit_form_id);

			$('input.name', edit_form).val(data['name']);
			$('input.email', edit_form).val(data['email']);
			$('input.id', edit_form).val(data['id']);
						
			self.reset_ac();
		};
	};
	
	this.reset_ac = function() {
		self.active_data = [];
		self.active_result = -1;
		self.active_value = '';
		self.active_id = false;
		self.ac_input_result.html('');
		
		$('div.result', self.ac_edit_form).hide(100);
	};
	
	
	
	this.post_form = function() {
		
		var edit_form = $('#' + self.edit_form_id);
		
		data = {
			'name': $('input.name', edit_form).val(),
			'email': $('input.email', edit_form).val(),
			'id': $('input.id', edit_form).val(),
		};
		
		var url = self.api_url

		$.ajax({
			url: url,
			data: data,
			type: 'POST',
			dataType: 'json',
			success: function(data) {
				self.show_form_message(data);
			}
		});
	};
	
	this.show_form_message = function(data) {
		
		var edit_form = $('#' + self.edit_form_id);
		var div_result = $('div.result', edit_form);
		
		div_result.show(50);
		
		
		console.log(data);
		
		if(!data.success) {
			div_result.removeClass('alert-success');
			div_result.addClass('alert-error');
			div_result.html(data.message);
		} else {
			div_result.removeClass('alert-error');
			div_result.addClass('alert-success');
			div_result.html(data.message);
		}
		
		
		
	};
	
	
	// calculate items in object
	this.object_size = function(obj) {
	    var size = 0, key;
	    for (key in obj) {
	        if (obj.hasOwnProperty(key)) size++;
	    }
	    return size;
	};
	

};


// dom ready, init ac (and other things...)
$(document).ready(function() {
	
	ac = new AutocompleteUi();
	
	ac.api_url = 'api.php';
	ac.input_form_id = 'ac_input_form';
	ac.edit_form_id = 'ac_edit_form';
	
	ac.init();
	
});

