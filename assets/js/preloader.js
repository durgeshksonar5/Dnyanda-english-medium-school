(function($) {
    "use strict";

    /* ==================================================
        Preloader Init
     ===============================================*/
    function loader() {
        setTimeout(function() {
            $('#edufix-preloader').addClass('loaded');
            $("#loading").fadeOut(500);
            // Once preloader finishes, enable normal page scroll and remove elements
            if ($('#edufix-preloader').hasClass('loaded')) {
                $('#preloader').delay(900).queue(function() {
                    $(this).remove();
                });
            }
        }, 2000);
    }
    loader();

})(jQuery);
