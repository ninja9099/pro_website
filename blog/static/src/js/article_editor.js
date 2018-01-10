$(document).ready(function(){
	var url = $('#url').val()
	$('.note-editor').css("width", "100%");
	$("#preview").click(function(e){
		debugger;
		var data = $("#id_article_content").val();
		e.preventDefault()
		$.ajax({
		  url: '/blog/article/preview',
		  data: {'article_content':data},
		  cache: false,
		  type: 'post',
		  timeout: 3000,
		  beforeSend: function () {
			$('#preview').addClass('saving');
		  },
		  success: function (data) {
			$('#preview').removeClass('saving');
			$("#article_preview").find(".modal-body").html($.parseHTML(data));
			$('.modal').modal('show')
		  }
		});
	});

	// for saving the article
	$("#save").click(function(e){
		e.preventDefault()

		var formData = new FormData($('form')[0]);
		var img = $('#id_article_image')[0].files[0];
		debugger;
		formData.append('img', img);

		$.ajax({
		  url: url,
		  data: formData,
		  cache: false,
		  type: 'POST',
		  contentType: false,
		  processData: false,
		  timeout: 30000,
		  beforeSend: function () {
			$('#save').addClass('saving')
		  },
		  success: function (data) {
			if (data.success){
				$('#save').removeClass('saving unsaved');
				$("#article_preview").find(".modal-body").html(data.message);
				$('.modal').modal('show')
			}
			else{
				$('#save').removeClass('saving');
				$("#article_preview").find(".modal-body").html($.parseHTML(data.error));
				$('.modal').modal('show');
			}
			},
			error:function(data){
				$('#save').removeClass('saving');
				$("#article_preview").find(".modal-body").text(data);
				$('.modal').modal('show');
			}
		});
	});
});