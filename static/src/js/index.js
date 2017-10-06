define(['jquery', 'app', 'lib/jQuery.scrollSpeed'], function(jquery, smoothScroll) {
  (function($){
    $.fn.filetree = function(method){
        var settings = { // settings to expose
            animationSpeed      : 'slow',            
            collapsed           : true,
            console             : true,
        }
        var methods = {
            init : function(options){
              debugger;
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

// (function($) {
// $.fn.menumaker = function(options) {  
//  var cssmenu = $(this), settings = $.extend({
//    format: "dropdown",
//    sticky: false
//  }, options);
//  return this.each(function() {
//    $(this).find(".button").on('click', function(){
//      $(this).toggleClass('menu-opened');
//      var mainmenu = $(this).next('ul');
//      if (mainmenu.hasClass('open')) { 
//        mainmenu.slideToggle().removeClass('open');
//      }
//      else {
//        mainmenu.slideToggle().addClass('open');
//        if (settings.format === "dropdown") {
//          mainmenu.find('ul').show();
//        }
//      }
//    });
//    cssmenu.find('li ul').parent().addClass('has-sub');
// multiTg = function() {
//      cssmenu.find(".has-sub").prepend('<span class="submenu-button"></span>');
//      cssmenu.find('.submenu-button').on('click', function() {
//        $(this).toggleClass('submenu-opened');
//        if ($(this).siblings('ul').hasClass('open')) {
//          $(this).siblings('ul').removeClass('open').slideToggle();
//        }
//        else {
//          $(this).siblings('ul').addClass('open').slideToggle();
//        }
//      });
//    };
//    if (settings.format === 'multitoggle') multiTg();
//    else cssmenu.addClass('dropdown');
//    if (settings.sticky === true) cssmenu.css('position', 'fixed');
// resizeFix = function() {
//   var mediasize = 700;
//      if ($( window ).width() > mediasize) {
//        cssmenu.find('ul').show();
//      }
//      if ($(window).width() <= mediasize) {
//        cssmenu.find('ul').hide().removeClass('open');
//      }
//    };
//    resizeFix();
//    return $(window).on('resize', resizeFix);
//  });
//   };
// })($);
$(function() {  

    jQuery.scrollSpeed(100, 800);

}); 
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