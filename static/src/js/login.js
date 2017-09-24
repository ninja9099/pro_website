require(['jquery'], function ($) {
	$(document).ready(function(){
		$('button').on('click', function(e){
			
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
					debugger;
					if (response.login){
						window.location.reload($("[name='next']").val())
					}
					alert('Logged in successfully');
				},
				error:function(errorType, errorMessage){
					alert('error occured please after sometime');
				},
				beforeSend:function(){
					$('.login-button').text('Please Wait ...');
				},
				complete:function(){
					$('.login-button').text('Submit');
				}


			})
		});

	});
});