$(document).ready(function() {

    $('#show-button').click(function() {
        if($('#show-menu').is(':visible')){
            $('#arrow-menu').animate(
                {deg: 0},
                {
                    duration: 500,
                    step: function (now) {
                        $(this).css({transform: 'rotate(' + now + 'deg)'});
                    }
                }
            );
        }else {
            $('#arrow-menu').animate(
                {deg: -90},
                {
                    duration: 500,
                    step: function (now) {
                        $(this).css({transform: 'rotate(' + now + 'deg)'});
                    }
                }
            );
        }
        $('#show-menu').toggleClass('disabled');
        $('#show-filter').toggleClass('disabled');
        return false;
    });

});
