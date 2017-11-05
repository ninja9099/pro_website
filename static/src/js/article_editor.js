require(['config'], function(){
	require(['jquery', 'lib/ckeditor/ckeditor', 'bootstrap', 'lib/ajax_setup'], function($, ck, bootstrap){
		$(document).ready(function(){
	        $("[id^='id_article']").addClass('form-control');

	        var editor = CKEDITOR.replace( 'id_article_content' );
	        // method for obseving changes in editor
	  //       editor.on( 'change', function( evt ) {
			// 	    // getData() returns CKEditor's HTML content.
			// 	    console.log( 'Total bytes: ' + evt.editor.getData().length );
			// });
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
			        $("#article_preview .modal-body").html("<div style='text-align: center; padding-top: 1em'><img src='/static/src/images/loader.gif'></div>");
			        $('.modal').modal('show')
			      },
			      success: function (data) {
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
	        	debugger;
			    $.ajax({
			      url: '/blog/article_submitt/',
			      data: data,
			      cache: false,
			      type: 'post',
			       timeout: 30000,
			      beforeSend: function () {
			        $("#article_preview .modal-body").html("<div style='text-align: center; padding-top: 1em'><img src='/static/src/images/loader.gif'></div>");
			        $('.modal').modal('show')
			      },
			      success: function (data) {
			      	debugger;
			      	if (data.success){
				      	debugger;
				        $("#article_preview .modal-body").html("your article have bin saved successfuly go to your profile for edit it further");
				      	$('.modal').modal('show')
			      	}
			      	else{
			      		$("#article_preview .modal-body").html($.parseHTML(data.error));
				      	$('.modal').modal('show')
			      	}
			      }
			    });
		  	});


	    });
	});
});