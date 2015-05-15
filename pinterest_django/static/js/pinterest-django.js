  $(window).load(function()
  {
   var container = document.querySelector('#pin-masonry-container');
   var msnry = new Masonry( container );
  });

$('button.like-button').click(function(){
    var pinid;
    pinid = $(this).attr("data-pinid");
        $.get('/pinterest/like_pin/', {pin_id: pinid},
            function(data){
            $('span.likes-count[data-pinid="'+pinid+'"]').html(data);
            $('button.like-button[data-pinid="'+pinid+'"]').prop("disabled",true);
        });
    });

$('button.close-button').click(function(){
   var pinid;
   var container = document.querySelector('#pin-masonry-container');
   var msnry = new Masonry( container );
   pinid = $(this).attr("data-pinid");
    $('div.pin-container[data-pinid="'+pinid+'"]').remove();
    msnry.layout()
});

// .on(events[, selector][, data], function(e));
$('body').on('click', '#pin_pin_button', function() {
   alert('Successfully pin the pin');
});
