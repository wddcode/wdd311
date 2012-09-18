// alert('ok');


Animal = function() {
	
	this.name = false;
	
	this.make_noise = function() {
		alert('making some noise');
	};

}

Dog = function() {
	
};

Dog.prototype = new Animal();

Dog.prototype.make_noise = function() {
	alert('WuffWuff');
};



//d = new Dog();
//d.make_noise();
