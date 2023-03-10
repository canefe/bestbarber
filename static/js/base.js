$(function() {
    $('#logo').on('click',function(){window.location.href="/"})
});

// Make a gsap animation for the logo to scale up and down on hover 
// and make it clickable to go to the home page
$(function() {
    $('#logo').on('mouseenter',function(){
        gsap.to('#logo', {duration: 0.5, scale: 1.1});
    });
    $('#logo').on('mouseleave',function(){
        gsap.to('#logo', {duration: 0.5, scale: 1});
    });
    
    $('.menuitem').on('mouseenter',function(){
        gsap.to(this, {duration: 0.5, scale: 1.1});
    });
    $('.menuitem').on('mouseleave',function(){
        gsap.to(this, {duration: 0.5, scale: 1});
    });


});
