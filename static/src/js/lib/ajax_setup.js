define(['jquery','lib/jquery.cookie'], function($, cookie){
	$.ajaxSetup({
	    headers: {
	        'X-CSRFToken': $.cookie('csrftoken')
	    },
	});
});