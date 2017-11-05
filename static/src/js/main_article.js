requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'lib/jquery',
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


define(['jquery', 'underscore', 'index', 'lib/ajax_setup'], function($, _ , cookie){
        'use strict'
		var ajax_caller = (function(self, $){

				var errorHtml = _.template("<ul><li class='error'>Error: <%= error %>"
					+ "</li><li class='error'>Error Code: <%= error_code %></li>"
					+ "</ul>")  
		        var genericRpc = function(self){
		            var request = $.ajax({
		                url: $(self).attr('href'),
		                type: self.method,
		                data: {'article_id': $(self).attr('data-id'), 'user_id': $(self).attr('data-user')},
		                dataType: 'json',
		            })
		            return resolver(request, self)
		        };

		        var makeCall = function(event){
    				var self = this	
    				event.preventDefault()
		        	if ($(this).hasClass('down')){
		        		this.method = 'delete';
		        	}
		        	else{
		        		this.method = 'post'
		        	};

		        	return genericRpc(this)
		        };
		        var resolver = function(request, self){
		        	request.fail(function(response){
		        		
			        	$('#popup1 .content').html(ajax_caller.errorHtml({error: response.responseJSON.error ||response.responseJSON.detail , error_code: response.responseJSON.error_code ||response.responseJSON.status_code}));
			        	$('#popup1').show()
			        });
			        request.done(function(response) {
				        $(self).prev().val(response.total_likes);
				        $(self).toggleClass('down');
				        // $(self).find('i.fa').toggleClass('shake').toogleClass('rotateInUpRight');
				        $(self).find('i.fa').toggleClass('fa-thumbs-o-up').toggleClass('fa-thumbs-up')
				        if(this.type == 'DELETE'){
				        	$(self).find('i.fa').removeClass('zoomIn').addClass('rotateInUpRight');
				        }
				        else{
				        $(self).find('i.fa').removeClass('rotateInUpRight').addClass('zoomIn');

				        }
				        setTimeout(function(){
				        	$(self).addClass('rotateInUpRight')
				        }, 400);
		        	});
			    };
		        return{
		        	makeCall:makeCall,
		        	errorHtml:errorHtml,
		        }
		}(this, $));
	    $('.close').click(function(){
	    	$(this).parent().parent().hide()
	    });
    
    var like_list = $('.like');

    _.each(like_list, function(item){
    	$(item).on('click', _.bind(ajax_caller.makeCall, item))
    });
});