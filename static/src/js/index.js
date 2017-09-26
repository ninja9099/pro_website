define(['jquery', 'app'], function(jquery) {
	$(document).ready(function(){
		$( window ).scroll(function() {
			var height = $(window).scrollTop()
			if (height >= 30){
	  			$( ".row1" ).addClass('fix');
			}
			else{
	  			$( ".row1" ).removeClass('fix');
			}
		});
		
		$('.card__share > a').on('click', function(e){ 
	    e.preventDefault() // prevent default action - hash doesn't appear in url
	      $(this).parent().find( 'div' ).toggleClass( 'card__social--active' );
	    $(this).toggleClass('share-expanded');
	    });
	});
});