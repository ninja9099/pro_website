$(document).ready(function(){
    //for updating the notifications
    update_badge();
    $("#notifications").on('click', fetch_notifications);

    $('#id_search_button').click(function (e){
        e.preventDefault()
        $("#search-form").toggleClass('search_active');
        $(this).parent().toggleClass('border-active')
    });

    // for header fixing the animations
    var lastScrollTop = 0;
    $(window).scroll(function(event){
       var st = $(this).scrollTop();
       if (st > lastScrollTop){
           $('.navbar').addClass('nav-up');
       } else {
          // up scroll code
           $('.navbar').removeClass('nav-up');

       }
       lastScrollTop = st;
    });
    

});
