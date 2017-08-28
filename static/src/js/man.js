$(document).ready(function(){
	// scrollbar-function
	$( window ).scroll(function() {
		var height = $(window).scrollTop()
		if (height >= 80){
  			$( ".row1" ).addClass('fix');
		}
		else{
  			$( ".row1" ).removeClass('fix');
		}
	});
});
