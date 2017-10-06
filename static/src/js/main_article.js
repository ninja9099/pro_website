requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'jquery',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
        TweenMax:'lib/TweenMax.min',
        cookie : 'lib/jquery.cookie',
    },
     shim: {
        "underscore": {
           exports: "_"
        }
    }
});


define(['jquery', 'underscore', 'pop_animate', 'cookie', 'index'], function($, _ , animate, cookie){

		$.ajaxSetup({
	        headers: {
	            'X-CSRFToken': $.cookie('csrftoken')
	        },
     	});

     	var ajax_liker_desliker = function(self, method){
     		var request = $.ajax({
	  		  	url: $(self).attr('data-url'),
			  	type: method,
			  	data: {'article_id': $(self).attr('data-id'), 'user_id': $(self).attr('data-user')},
			  	dataType: 'json',
  			});
  			return request
     	}
		$( ".like" ).bind( "click", function(){
			var self = this
			var call_like = ajax_liker_desliker(self, "POST");
  			call_like.fail(function(jqXHR, textStatus, data){

		  		if (textStatus == 'error'){
	  				$('#wrap').css('display', 'block')
	  				setTimeout(function(){
	  					animate.breakGlass('reverse');
	  				},500)
	  			}
  			});
  			call_like.done(function( jqXHR, textStatus , data ) {
				if (textStatus == 'success'){
					$(self).hide();
					$(self).next().show();
					$(self).next().find('.fa').addClass('shake');
		  		}
  			});
		});

		// for unliking the post
		$('.unlike').bind( "click", function(){
			var self = this;
		  	var call_unlike = ajax_liker_desliker(self, 'delete');
		  	call_unlike.fail(function(jqXHR, textStatus, data){
			  		if (jqXHR.status === 'error'){
		  				$('#wrap').css('display', 'block')
		  				animate.breakGlass('reverse');
		  			}
	  			});
			call_unlike.done(function( jqXHR, textStatus , data ) {
			if (textStatus == 'nocontent'){
	  			$(self).hide();
				$(self).prev().show();
				$(self).prev().find('.fa').addClass('flip');
	  		}
			});
	});
//  for login button iteraction
	$('.login-button').click(function(){
  			animate.breakGlass();
  			setTimeout(function(){
		         $('#wrap').css('display', 'none')
		     },800);
  				
		});
	$('.close').click(function(){
			animate.breakGlass();
			setTimeout(function(){
	         $('#wrap').css('display', 'none')
	     },800);
				
	});
	// end of login interaction
});