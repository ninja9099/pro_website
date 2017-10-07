define(['jquery'], function(jquery) {
  (function($){
    $.fn.filetree = function(method){
        var settings = { // settings to expose
            animationSpeed      : 'slow',            
            collapsed           : true,
            console             : true,
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
    
}(jquery)); 
	
    $(document).ready(function(){
        $(window).scroll(function(e){
            if ($(this).scrollTop() > 100) {
                $('header').slideDown();
                $("header").addClass('fix')

            } else {
                // $("header").removeClass('fix')
                $("header").removeClass('fix')
                $('.fix').slideUp();
        }
    });

        $('select').addClass('form-control');
        $('select').addClass('dob');
        $("[name='signup_submit']").click(function(){
        $(this).addClass('hinge')});
        $(".file-tree").filetree();
    });
    });