$(document).ready(function(){
    //for updating the notifications
    update_badge();
    $("#notifications").on('click', fetch_notifications);

    // for header fixing the animations
    var lastScrollTop = 0;
    $(window).scroll(function(event){
       var st = $(this).scrollTop();

       if (st > lastScrollTop || st===0 ){
           $('.navbar').removeClass('fix-navbar');
       } else {
          // up scroll code
           $('.navbar').addClass('fix-navbar');

       }
       lastScrollTop = st;
    });

});