$(document).ready(function(){
    //for updating the notifications
    $('[data-toggle="tooltip"]').tooltip(); 
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
    

    // for back to top 
    $("#backtotop").click(function () {
      debugger;
        $("body,html").animate({
            scrollTop: 0
        }, 600);
    });
    $(window).scroll(function () {
        if ($(window).scrollTop() > 150) {
            $(".back-to-top").addClass("visible");
        } else {
            $(".back-to-top").removeClass("visible");
        }
    });
});
