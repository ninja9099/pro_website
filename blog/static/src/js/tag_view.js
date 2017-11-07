require('tagView', ['config'], function(){
    require(['jquery', 'lib/imagesloaded.pkgd.min'], function(){
      debugger;
      $(document).ready(function(){
              var $container1 = $(".col-md-3");
            //   $container1.imagesLoaded(function() {
            //     $container1.masonry({
            //     itemSelector: '.card-view',
            //     columnWidth: 302
            //   });
            // });

            $.fn.stars = function() {
              return $(this).each(function() {
                var num = $(this).data("star");
                $(this).html($("<span />").width(Math.max(0, Math.min(5, num)) * 12));
              })
            };

            $(function() {

              $('.Switch').click(function() {
                $(this).toggleClass('list').toggleClass('card');
                // check current view mode: 'list' or 'card'
                if($(this).hasClass('list')) {
                  console.log('List view');
                  $(".card-view").attr("class", "list-view");
                  $(".list-view").removeAttr("style");
                } else {
                  console.log('Card view');
                  $(".list-view").attr("class", "card-view");
                  var container1 = document.querySelector('.col-md-3');
                  // Reload masonry again
                  var msnry = new Masonry( container1, {
                    itemSelector: '.card-view',
                    columnWidth: 302
                  });
                }
              });
            });
            $("span#c_stars").stars(); 
        });
    });
});
