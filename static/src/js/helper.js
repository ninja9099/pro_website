define(['cookie'], function(cookie){
    //just testing away the things here
    var privateMethod = function(){};

    var ajaxObject = {
        init:function (jQuery) {
            console.log('INFO ==> Starting ajax header setup')
            jQuery.ajaxSetup({
                headers: {
                    'X-CSRFToken': $.cookie('csrftoken')
                }
            });
        },
        start: function () {
            this.init(jQuery)
            console.log('INFO ==> ajax setup completed')
        }
    }
    return ajaxObject;
});