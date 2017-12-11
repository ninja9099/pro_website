$(document).ready(function(){

// notification handler portion
var badge = $("#notification_badge");

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        }
    });

    function make_ajax_call(url, before){
        return $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend:before,
        });
    }
    function update_badge() {
        var url = badge.attr('data-url');
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                if(response.unread_count){
                    badge.html(response.unread_count);
                }
                else{
                    badge.hide();
                    $(".fa-bell").css('color', "#ddd");
                }
            },
            fail: function (xhr) {
                //    no cover for failures
                console.log(xhr)
            }
        });
        setTimeout(update_badge, 100000)
    }

    function fetch_notifications() {
        var self = this
        var url = $(self).attr('data-url') + '?mark_as_read=true';
        var def = make_ajax_call(url, function () {
            $("#notification_board").html('<img class="loader" width="50" height="50" src="/static/src/images/loader.gif"/>')
        });

        def.done(function (data, textStatus, jqXHR) {
            var notifications;
            if (data.unread_list) {
                notifications = $.map(data.unread_list, function (item) {
                    var message = "";
                    debugger;
                    if (typeof item.actor !== 'undefined') {
                        message = item.actor;
                    }
                    if (typeof item.verb !== 'undefined') {
                        message = message + " " + item.verb;
                    }
                    if (typeof item.target !== 'undefined') {
                        message = message + " " + item.target;
                    }
                    if (typeof item.timestamp !== 'undefined') {
                        message = message + " " + new Date(item.timestamp).toDateString();
                    }
                    return '<li>' + message + '</li>';
                }).join('')
                $("#notification_board").html(notifications);
                badge.hide();
                $(".fa-bell").css('color', "#ddd");
            }
            else {
                $("#notification_board").html("<li> All well </li>");
            }
        });
    }
    update_badge();
    $("#notifications").on('click', fetch_notifications);
//
//   fetch notifications ends here
});