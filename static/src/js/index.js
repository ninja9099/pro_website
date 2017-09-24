define(['jquery.min', 'app'], function(jquery) {
	$(document).ready(function(){
		$( window ).scroll(function() {
			var height = $(window).scrollTop()
			if (height >= 50){
	  			$( ".row1" ).addClass('fix');
			}
			else{
	  			$( ".row1" ).removeClass('fix');
			}
		});
	});
});