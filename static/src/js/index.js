require(['config'], function(){
    console.log('config file loaded');
    require(['jquery', 'bootstrap'], function(){
        $(document).ready(function(){
            // $(window).scroll(function(e){
            //     if ($(this).scrollTop() > 100) {
            //         $('header').slideDown();
            //         $("header").addClass('fix')
            //     } else {
            //         // $("header").removeClass('fix')
            //         $("header").removeClass('fix')
            //         $('.fix').slideUp();

            //     }
            // });
            $("#myCarousel").carousel();
            $('#myCarousel').bind('slide.bs.carousel', function (e) {
                  $('')
                });
        });
    });
});


