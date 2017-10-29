requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'jquery',
        bootstrap:'lib/bootstrap.min',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
        TweenMax:'lib/TweenMax.min',
        cookie : 'lib/jquery.cookie',
    },
     shim: {
        "underscore": {
           exports: "_"
        },
        bootstrap : {
            deps : [ 'jquery'],
        },
    }
});

define(['jquery', 'underscore', 'bootstrap'], function($, _, bootstrap){
    $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});
});
