$(window).scroll(function(){
	var scroll = $(window).scrollTop();

	if(scroll >= 400){
		$("#myNav").addClass('bg-dark');
	} else{
		$("#myNav").removeClass('bg-dark');
	}

});