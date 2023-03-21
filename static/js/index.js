
// Make a gsap animation for the logo to scale up and down on hover 
// and make it clickable to go to the home page
$(function() {
    $('.barbershop').on('mouseenter',function(){
        gsap.to(this, {duration: 0.5, scale: 1.1});
    });
    $('.barbershop').on('mouseleave',function(){
        gsap.to(this, {duration: 0.5, scale: 1});
    });
});
