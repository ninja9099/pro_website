$(document).ready(function(){
	// // dropdown animation
	// $('.dropdown-toggle').click(function () {
 //    	$(this).next('.dropdown-menu').slideToggle(400);
	// });

	// $('.dropdown-toggle').focusout(function () {
 //    	$(this).next('.dropdown-menu').slideUp(400);
	// });

	// card hover animations
	$('.hover').click(function(e){
	    $( this ).addClass('flip');
	});
	$('.hover').mouseleave(function(){
	    $( this ).removeClass('flip');
	});
});
