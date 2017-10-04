requirejs.config({
    baseUrl: '/static/src/js',
    paths: {
        jquery: 'jquery',
        ck: 'lib/ckeditor/ckeditor',
        underscore: 'lib/underscore-min',
    },
     shim: {
        "underscore": {
           exports: "_"
        }
    }
});