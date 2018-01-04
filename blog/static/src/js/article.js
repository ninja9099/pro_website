require(['config'], function(){
	require(['lib/CollapsibleLists', 'article_like', 'login'], function(col,article_like, login){
		
		CollapsibleLists.apply();
		$( ".login-popup a" ).hover(function() {
    			$( '.popup' ).show();
  			});
		$('#close').click(function(){
			$('.popup').hide();
		});


    });
});

