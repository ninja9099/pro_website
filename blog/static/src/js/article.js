require(['config'], function(){
	require(['lib/CollapsibleLists', 'article_like', 'login'], function(col,article_like, login){
		debugger;
		CollapsibleLists.apply();
		$( ".login-popup a" ).hover(function() {
    			$( '.popup' ).show();
  			});
  		// $('.popup').mouseleave(function() {
   	//  			$('.popup').hide();
  		// 	});
		$('#close').click(function(){
			$('.popup').hide();
		});
	})
});

