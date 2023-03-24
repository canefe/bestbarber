$(document).ready(function() {
    $('.peer').on('input', function() {
        console.log('input');
        var $span = $(this).siblings('.peer-span');
        if ($(this).val().length > 0) {
            $span.addClass('!-top-12');
            $span.addClass('!text-xs');
        }
    });
    //focus out
    $('.peer').on('focusout', function() {
        var $span = $(this).siblings('.peer-span');
        if ($(this).val().length == 0) {

            $span.removeClass('!-top-12');
            $span.removeClass('!text-xs');
        } else if ($(this).val().length > 0) {
            $span.addClass('!-top-12');
            $span.addClass('!text-xs');
        }
    });
});