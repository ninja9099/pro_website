define('ajax',
	['jquery','cookie'],
	function($, cookie){
		console.log('ajax_setup completed');
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