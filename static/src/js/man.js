$(document).ready(function(){
	// dropdown animation
	$('.dropdown-toggle').click(function () {
    	$(this).next('.dropdown-menu').slideToggle(400);
	});

	$('.dropdown').mouseleave(function () {
    	$(this).next('.dropdown-menu').slideUp(400);
	});

	// scrollbar-function
	$( window ).scroll(function() {
		var height = $(window).scrollTop()
		if (height >= 70){
  			$( ".navbar" ).addClass('opaque');
		}
		else{
  			$( ".navbar" ).removeClass('opaque');
		}
	});
	// card hover animations
	$('.hover').click(function(e){
	    $( this ).addClass('flip');
	});
	$('.hover').mouseleave(function(){
	    $( this ).removeClass('flip');
	});
});
