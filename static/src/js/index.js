define(['jquery', 'app'], function(jquery) {
	$(document).ready(function(){
		$( window ).scroll(function() {
			var height = $(window).scrollTop()
			if (height >= 70){
	  			$( ".row1" ).addClass('fix');
			}
			else{
	  			$( ".row1" ).removeClass('fix');
			}
		});
		
		$('.card__share > a').on('click', function(e){ 
	    e.preventDefault() // prevent default action - hash doesn't appear in url
	      $(this).parent().find( 'div' ).toggleClass( 'card__social--active' );
	    $(this).toggleClass('share-expanded');
	    });
	    
	    $(".Collapsable").click(function () {
        $(this).parent().children().toggle();
        $(this).toggle();
    	});
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