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
        'use strict'
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': $.cookie('csrftoken')
            },
        });
		var ajax_caller = (function(self, $){
				var errorHtml = _.template("<ul><li>Error: <%= error %></li><li>Error Code<%= error_code %></li></ul>")  
		        var genericRpc = function(self){
		            var request = $.ajax({
		                url: $(self).attr('href'),
		                type: self.method,
		                data: {'article_id': $(self).attr('data-id'), 'user_id': $(self).attr('data-user')},
		                dataType: 'json',
		            });
		            return request;
		        };

		        var makeCall = function(){

		        	if ($(this).hasClass('down')){
		        		this.method = 'delete';
		        	}
		        	else{
		        		this.method = 'post'
		        	};

		        	return genericRpc(this)
		        };
		        return{
		        	makeCall:makeCall,
		        	errorHtml:errorHtml,
		        }
		}(this, $));

	   	$( ".like" ).on("click", function(event){
	    	event.preventDefault()
	    	var defered = ajax_caller.makeCall.call(this);
	    	var self = this;
	        defered.fail(function(response){
	        	$('#popup1 .content').html(ajax_caller.errorHtml({error: response.responseJSON.error ||response.responseJSON.detail , error_code: response.responseJSON.error_code ||response.responseJSON.status_code}));
	        	$('#popup1').show()
	        });
	        defered.done(function(response) {
	        	debugger;
		        $(self).prev().val(response.total_likes);
		        $(self).toggleClass('down');
		        $(self).find('i.fa').toggleClass('shake');
		        $(self).find('i.fa').toggleClass('fa-thumbs-o-up').toggleClass('fa-thumbs-up')
		        setTimeout(function(){
		        	$(self).addClass('shake')
		        }, 400);

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
	    	$(this).parent().parent().hide()
	    });
    // end of login interaction
});