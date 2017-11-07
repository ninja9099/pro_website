define('header'
	['jquery'],
	function($){
		return {
			animate:function animate($){
				$(window).scroll(function(e){
	            if ($(this).scrollTop() > 100) {
	                $('header').slideDown();
	                $('header').addClass('fix')	
	            } else {
	               $('header').removeClass('fix')
	            }
	        });
		},
	}
});