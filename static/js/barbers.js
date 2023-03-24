// Use JQuery and GSAP to animate book buttons with class book on hover indivudually 
// avoid them all animating at the same time
$(function() {
    $('.book').on('mouseenter',function(){
        gsap.to(this, {duration: 0.5, scale: 1.1});
    });
    $('.book').on('mouseleave',function(){
        gsap.to(this, {duration: 0.5, scale: 1});
    });

    context_dict['attributes'] = ["Clean",
                                      "Cheap",
                                      "Boring",
                                      "Long_wait",
                                      "Professional",
                                      "Student",
                                      "Fun"
                                      ]


});


$(document).ready(function(){
    $('.Clean').addClass('text-green-700');
    $('.Fun').addClass('text-green-700');
    $('.Clean').addClass('text-green-700');
    $('.Student').addClass('text-green-700');
    $('.Cheap').addClass('text-green-700');
    $('.Long_wait').addClass('text-red-500');
    $('.Professional').addClass('text-green-700');
    $('.Boring').addClass('text-red-500');

});



