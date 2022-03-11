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

    $('.menu-home').hover(
        function() {
            $('.menu-home-img').attr("src", "./img/logo/bx-home.svg");
        },
        function() {
            $('.menu-home-img').attr("src", "./img/logo/bx-home-yellow.svg");
        }
    );

    $('.menu-resume').hover(
        function() {
            $('.menu-resume-img').attr("src", "./img/logo/bxs-user-detail.svg");
        },
        function() {
            $('.menu-resume-img').attr("src", "./img/logo/bxs-user-detail-yellow.svg");
        }
    );

    $('.menu-projects').hover(
        function() {
            $('.menu-projects-img').attr("src", "./img/logo/bx-list-ul.svg");
        },
        function() {
            $('.menu-projects-img').attr("src", "./img/logo/bx-list-ul-yellow.svg");
        }
    );

    $('.menu-contact').hover(
        function() {
            $('.menu-contact-img').attr("src", "./img/logo/bxs-contact.svg");
        },
        function() {
            $('.menu-contact-img').attr("src", "./img/logo/bxs-contact-yellow.svg");
        }
    );

});
