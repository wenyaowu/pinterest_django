$('button.like-button').click(function(){
    var pinid;
    pinid = $(this).attr("data-pinid");
        $.get('/pinterest/like_pin/', {pin_id: pinid},
            function(data){
            $('span.likes-count[data-pinid="'+pinid+'"]').html(data);
            $('button.like-button[data-pinid="'+pinid+'"]').prop("disabled",true);
        });
    });