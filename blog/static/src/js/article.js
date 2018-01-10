$(document).ready(function(){

	//  for collapsible list
	CollapsibleLists.apply();
	// for the slick slider
	$('.slick-slides').slick({
        slidesToShow:3,
        slidesToScroll: 1,
        lazyLoad: 'ondemand',
        arrows : false,
          pauseOnFocus:true,
        autoplay:true,
        dots:true,
        responsive: [
		    {
		      breakpoint: 768,
		      settings: {
		        arrows: false,
		        centerMode: true,
		        centerPadding: '40px',
		        slidesToShow: 3
		      }
		    },
		    {
		      breakpoint: 480,
		      settings: {
		        arrows: false,
		        centerMode: true,
		        centerPadding: '40px',
		        slidesToShow: 1
		      }
		    }
    	]
    });
});