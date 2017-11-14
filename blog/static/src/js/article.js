require(['config'], function(){
	require(['lib/CollapsibleLists', 'article_like', 'login'], function(col,article_like, login){
		debugger;
		CollapsibleLists.apply();
		$( ".login-popup a" ).hover(function() {
    			$( '.popup' ).show();
  			});
		$('#close').click(function(){
			$('.popup').hide();
		});

		var fixmeTop = $('.fixme').offset().top;       // get initial position of the element

		$(window).scroll(function() {                  // assign scroll event listener

		    var currentScroll = $(window).scrollTop() - 210; // get current position

		    if (currentScroll >= fixmeTop) {           // apply position: fixed if you
		        $('.fixme').addClass('scrollfix bounceInDown animated');

		    } else {                                   // apply position: static
		        $('.fixme').removeClass('scrollfix bounceInDown animated');
		    }
		});
	})
});

