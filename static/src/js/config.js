console.log('config file loaded')
requirejs.config({

    baseUrl: '/static/src/js',
    paths: {
        jquery: 'lib/jquery',
        bootstrap:'lib/bootstrap.min',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
        cookie : 'lib/jquery.cookie',
        ajax:'lib/ajax_setup'
    },
     shim: {
        'jquery': {
            exports: '$'
        },
        "underscore": {
           exports: "_"
        },
        'bootstrap' : {
            deps : [ 'jquery'],
        }
    }
});