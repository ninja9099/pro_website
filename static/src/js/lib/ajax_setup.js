define('ajax',
	['jquery','cookie'],
	function($, cookie){
		return {
			init:function(){
				$.ajaxSetup({
		    		headers: {
		        		'X-CSRFToken': $.cookie('csrftoken')
		    		}	
				});
			},
			start:function(){
					this.init();
			}	
		}
});