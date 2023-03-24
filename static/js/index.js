
// Make a gsap animation for the logo to scale up and down on hover 
// and make it clickable to go to the home page
$(function() {
    $('.barbershop').on('mouseenter',function(){
        gsap.to(this, {duration: 0.5, scale: 1.1});
    });
    $('.barbershop').on('mouseleave',function(){
        gsap.to(this, {duration: 0.5, scale: 1});
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    // On Click to customerBtn or barberBtn send ajax request to server

    $('#customerBtn').on('click',function(){
        $('#customer-confirmation-dialog').removeClass('hidden');
    }
    );

    $('#customer-cancel-btn').on('click', function() {
        // Hide the confirmation dialog if the user clicks "Cancel"
        $('#customer-confirmation-dialog').addClass('hidden');
    });

    $('#customer-confirm-btn').on('click', function() {
        // Send an AJAX request to the server if the user clicks "Yes"
        $.ajax({
            url: window.location.href,
            type: 'POST',
            data: {
                'action': 'customer'
            },
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function(data) {
                // Handle the server's response
                alert("You are now a customer");
                // reload the page
                location.reload();

            },
            error: function(xhr, status, error) {
                // Handle errors
                alert(error);
            }
        });

        // Hide the confirmation dialog
        $('#customer-confirmation-dialog').addClass('hidden');
    });

    $('#barberBtn').on('click', function() {
        // Show a dialog to confirm the user's action
        $('#barber-confirmation-dialog').removeClass('hidden');
    });

    $('#barber-cancel-btn').on('click', function() {
        // Hide the confirmation dialog if the user clicks "Cancel"
        $('#barber-confirmation-dialog').addClass('hidden');
    });

    $('#barber-confirm-btn').on('click', function() {
        // Send an AJAX request to the server if the user clicks "Yes"
        console.log("{{ csrf_token}}")
        $.ajax({
            url: window.location.href,
            type: 'POST',
            data: {
                'action': 'barber'
            },
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function(data) {
                // Handle the server's response
                alert("You are now a Barber!");
               // reload the page
                location.reload();

            },
            error: function(xhr, status, error) {
                // Handle errors
                alert(error);
            }
        });

        // Hide the confirmation dialog
        $('#barber-confirmation-dialog').addClass('hidden');
    });

});
