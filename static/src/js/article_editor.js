require(['config'], function(){
	require(['jquery', 'lib/ckeditor/ckeditor', 'bootstrap', 'lib/ajax_setup'], function($, ck, bootstrap){
		$(document).ready(function(){
	        $("[id^='id_']").addClass('form-control');

	        var editor = CKEDITOR.replace( 'id_article_content' );
	        var url = $('#url').val()
	        // method for obseving changes in editor
	  		      editor.on( 'change', function( evt ) {
				    // getData() returns CKEditor's HTML content.
				    console.log( 'Total bytes: ' + evt.editor.getData().length );
				    $('#save').addClass('unsaved')
			});
	  		      
	        $("#preview").click(function(e){
	        	var data = CKEDITOR.instances.id_article_content.getData();
		        e.preventDefault()
			    $.ajax({
			      url: '/blog/article/preview',
			      data: {'article_content':data},
			      cache: false,
			      type: 'post',
			      timeout: 3000,
			      beforeSend: function () {
			        $('#save').addClass('saving')
			      },
			      success: function (data) {
			      	$('#save').removeClass('saving')
			        $("#article_preview .modal-body").html($.parseHTML(data));
			      	$('.modal').modal('show')
			      }
			    });
		  	});

		  	// for saving the article
		  	$("#save").click(function(e){
		        e.preventDefault()
		        for ( instance in CKEDITOR.instances ){
		        	CKEDITOR.instances[instance].updateElement();
		    	}
		        var data = $('form').serialize()
			    $.ajax({
			      url: url,
			      data: data,
			      cache: false,
			      type: 'post',
			      timeout: 30000,
			      beforeSend: function () {
			      	$('#save').addClass('saving')
			      },
			      success: function (data) {
			      	if (data.success){
			      		$('#save').removeClass('saving')
			      		$('#save').removeClass('unsaved')
				        $("#article_preview .modal-body").html(data.message);
				      	$('.modal').modal('show')
			      	}
			      	else{
			      		$('#save').removeClass('saving')
			      		$("#article_preview .modal-body").html($.parseHTML(data.error));
				      	$('.modal').modal('show')
			      	}
			      	},
			      	error:function(data){
			      		$('#save').removeClass('saving')
			      		$("#article_preview .modal-body").text(data);
				      	$('.modal').modal('show')
			      	}
			    });
		  	});
	    });
	});
});