define(['jquery', 'ck'], function($){
	$(document).ready(function(){
        $("[id^='id_article']").addClass('form-control')
        $('.fieldWrapper').addClass('form-group')
        CKEDITOR.replace('id_article_content' );
        $('.row1').addClass('fix');
    });
    
})