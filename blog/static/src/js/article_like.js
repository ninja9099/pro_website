define(
	['jquery','cookie'],
	function($, cookie){
		debugger;
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