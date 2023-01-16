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
            $('#show-menu').fadeOut(500);
            $('#show-filter').fadeOut(500);
        }else if($('#show-menu').is(':hidden')){
            $('#arrow-menu').animate(
                {deg: -90},
                {
                    duration: 500,
                    step: function (now) {
                        $(this).css({transform: 'rotate(' + now + 'deg)'});
                    }
                }
            );
            $('#show-menu').fadeIn(500);
            $('#show-filter').fadeIn(500);
        }
        $('#show-menu').toggleClass('disabled');
        $('#show-filter').toggleClass('disabled');
        return false;
    });

    $('.menu-home').hover(
        function() {
            $('.menu-home-img').attr("src", "../static/img/logo/bx-home.svg");
        },
        function() {
            $('.menu-home-img').attr("src", "../static/img/logo/bx-home-yellow.svg");
        }
    );

    $('.menu-resume').hover(
        function() {
            $('.menu-resume-img').attr("src", "../static/img/logo/bxs-user-detail.svg");
        },
        function() {
            $('.menu-resume-img').attr("src", "../static/img/logo/bxs-user-detail-yellow.svg");
        }
    );

    $('.menu-projects').hover(
        function() {
            $('.menu-projects-img').attr("src", "../static/img/logo/bx-list-ul.svg");
        },
        function() {
            $('.menu-projects-img').attr("src", "../static/img/logo/bx-list-ul-yellow.svg");
        }
    );

    $('.menu-contact').hover(
        function() {
            $('.menu-contact-img').attr("src", "../static/img/logo/bxs-contact.svg");
        },
        function() {
            $('.menu-contact-img').attr("src", "../static/img/logo/bxs-contact-yellow.svg");
        }
    );

});
