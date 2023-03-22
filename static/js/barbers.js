// Use JQuery and GSAP to animate book buttons with class book on hover indivudually 
// avoid them all animating at the same time
$(function() {
    $('.book').on('mouseenter',function(){
        gsap.to(this, {duration: 0.5, scale: 1.1});
    });
    $('.book').on('mouseleave',function(){
        gsap.to(this, {duration: 0.5, scale: 1});
    });
});



