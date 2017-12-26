define(['jquery'], function($){
    //just testing away the things here
    var privateMethod = function(){};

    var ajaxObject = {
        init:function (jQuery) {
            jQuery.ajaxSetup({
                headers: {
                    'X-CSRFToken': $.cookie('csrftoken')
                }
            });
        },
        start: function () {
            this.init(jQuery)
        }
    }
    return ajaxObject;
});