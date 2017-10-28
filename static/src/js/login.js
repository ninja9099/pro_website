require(['jquery'], function ($) {
	$(document).ready(function(){
		$('.send').on('click', function(e){
			
			e.preventDefault()
			$.ajax({
				method:'POST',
				type:'text/json',
				url:'/login/',
				data:{'username':$('#id_username').val(),
					'password':$('#id_password').val(),
					'remember_me':$('#id_remember_me').val(),
					'next_url':$('[name="next"]').val() || undefined,
					'is_ajax':true,
				},
				success:function(response){
					if (response.login){
						$('div.send').removeClass('loader');
						window.location.reload($("[name='next']").val())
					}
					else{
						alert(response.error);
						$('div.send').removeClass('loader');
					}
				},
				error:function(errorType, errorMessage){
					alert('error occured please after sometime' + errorMessage);
				},
				beforeSend:function(){
					$('div.send').addClass('loader');
				},
				complete:function(){
					$('.login-button').text('Submit');
				}
			})
		});

	});
});