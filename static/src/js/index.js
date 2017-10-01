define(['jquery', 'app'], function(jquery) {
	$(document).ready(function(){
		$( window ).scroll(function() {
			var height = $(window).scrollTop()
			if (height >= 65){
                $( ".row1" ).addClass('fix');
                $( ".row1" ).addClass('bounceInUp');
	  			$( ".row1" ).addClass('animated');
			}
			else{
                $( ".row1" ).removeClass('fix');
                $( ".row1" ).removeClass('bounceInUp');
	  			$( ".row1" ).removeClass('animated');
			}
		});
        $('select').addClass('form-control');
        $('select').addClass('dob');
        $("[name='signup_submit']").click(function(){
            $(this).addClass('hinge')});

        // $(".wrapper").hover(
        //       function() {
        //         $( this ).addClass('rotateInUpRight');
        //       }, function() {
        //         $( this ).removeClass('rotateInUpRight');
        //       }
        // );
	});
	(function($){
    $.fn.filetree = function(method){
        var settings = { // settings to expose
            animationSpeed      : 'fast',            
            collapsed           : true,
            console             : false
        }
        var methods = {
            init : function(options){
                // Get standard settings and merge with passed in values
                var options = $.extend(settings, options); 
                // Do this for every file tree found in the document
                return this.each(function(){
                    
                    var $fileList = $(this);
                   
                    $fileList
                        .addClass('file-list')
                        .find('li')
                        .has('ul') // Any li that has a list inside is a folder root
                            .addClass('folder-root closed')
                            .on('click', 'a[href="#"]', function(e){ // Add a click override for the folder root links
                                e.preventDefault();
                                $(this).parent().toggleClass('closed').toggleClass('open');
                                return false;
                            });
                    
                    //alert(options.animationSpeed); Are the settings coming in

                });
                
                
            }
        }

        if (typeof method === 'object' || !method){
            return methods.init.apply(this, arguments);
        } else {
            $.on( "error", function(){
                console.log(method + " does not exist in the file exploerer plugin");
            } );
        }  
    }
    
}(jQuery));

	$(".file-tree").filetree();
});