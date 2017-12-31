
//for setting up the ajax env
(function ajax_set_up(){
	$.ajaxSetup({
		headers: {
			'X-CSRFToken': $.cookie('csrftoken')
		}
	});
})();