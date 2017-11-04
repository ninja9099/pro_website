requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'lib/jquery',
        bootstrap:'lib/bootstrap.min',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
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