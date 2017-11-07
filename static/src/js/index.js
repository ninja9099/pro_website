require(['config'], function(){
    define(['jquery', 'bootstrap', 'lib/header'], function($, bootstrap, header){
        console.log(header)
        $("#myCarousel").carousel();
    });
});
