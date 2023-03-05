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
    
    $('#menu1').on('mouseenter',function(){
        gsap.to('#menu1', {duration: 0.5, scale: 1.1});
    });
    $('#menu2').on('mouseenter',function(){
        gsap.to('#menu2', {duration: 0.5, scale: 1.1});
    });
    $('#menu3').on('mouseenter',function(){
        gsap.to('#menu3', {duration: 0.5, scale: 1.1});
    });
    // General mouseleave function for all menu items starting from #menu1
    $('#menu1').on('mouseleave',function(){
        gsap.to('#menu1', {duration: 0.5, scale: 1});
    });
    $('#menu2').on('mouseleave',function(){
        gsap.to('#menu2', {duration: 0.5, scale: 1});
    });
    $('#menu3').on('mouseleave',function(){
        gsap.to('#menu3', {duration: 0.5, scale: 1});
    });

});
