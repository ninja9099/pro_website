requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'jquery',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
        TweenMax:'https://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenMax.min',
        cookie : 'lib/jquery.cookie',
    },
     shim: {
        "underscore": {
           exports: "_"
        }
    }
});


define(['jquery', 'underscore', 'lib/cookieCutter', 'pop_animate', 'cookie'], function($, _, cookieCutter, animate, cookie){

		$.ajaxSetup({
	        headers: {
	            'X-CSRFToken': $.cookie('csrftoken')
	        },
     	});
		$( ".like" ).bind( "click", function(){	
			var like_request = 'blah blah'
			$.ajax({
	  		  	url: $(this).attr('data-url'),
	  		  	beforeSend:function(xhr){
	  		  		debugger;
	  		  	},
			  	type: "POST",
			  	data:{
			  		'article_id': $(this).attr('data-id'),
			  	 	'user_id': $(this).attr('data-user'),
			  	 	},
			  	dataType: "application/json",
			  	success:function(response){
			  		confirm('you liked an article');
			  	},
		  		error: function(xher, error){
		  			if (xher.status === 403){
		  				$('#wrap').css('display', 'block')
		  				animate.breakGlass('reverse');
		  			}
		  		}
  			});
		});
		$('.login-button').click(function(){
  			animate.breakGlass();
  			setTimeout(function(){
		         $('#wrap').delay(2000).css('display', 'none')
		     },500);
  				
		});
		$('.close').click(function(){
  			animate.breakGlass();
  			setTimeout(function(){
		         $('#wrap').delay(2000).css('display', 'none')
		     },500);
  				
		});
});