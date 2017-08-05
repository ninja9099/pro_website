$(document).ready(function(){
	$('.main-slider').slick({
		dots: false,
	    prevArrow: false,
	    nextArrow: false,
		infinite: true,
		slidesToShow: 1,
		speed: 300,
		accessibility:true,
		autoplay:true,
		autoplaySpeed:3000,
		arrows:true,
		useCSS:true,
		useTransform:true,
		dots:true,
	});
});