define(['jquery', 'app'], function(jquery) {
	$(document).ready(function(){
        $(window).bind('mousewheel', function(event) {   
            if (event.originalEvent.wheelDelta >= 0 && ($(window).scrollTop() != 0)) {
                $( ".row1" ).addClass('fix');
                $( ".row1" ).addClass('bounceInDown');
                $( ".row1" ).addClass('animated');
            }
            else {
                $( ".row1" ).removeClass('fix');
                $( ".row1" ).removeClass('bounceInDown');
                $( ".row1" ).removeClass('animated');
            }
        });
        $('select').addClass('form-control');
        $('select').addClass('dob');
        $("[name='signup_submit']").click(function(){
            $(this).addClass('hinge')});
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