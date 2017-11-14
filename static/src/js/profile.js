require(['config'], function(){
	require(['jquery', 'underscore', 'bootstrap'], function($, _, bootstrap){
	    $(document).ready(function(){
	    	$('[data-toggle="tooltip"]').tooltip(); 
		});
	});
});