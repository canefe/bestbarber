
$(function() {
    $('#customerBtn').on('click',function(){
        $('#customer-confirmation-dialog').removeClass('hidden');
    }
    );

    $('#customer-cancel-btn').on('click', function() {
  // Hide the confirmation dialog if the user clicks "Cancel"
        $('#customer-confirmation-dialog').addClass('hidden');
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
                $('#success').removeClass('hidden');
        // change the html of #success > div > .message 

                $('#success > div > .message').html("<p class='text-lg font-bold'>Success!</p><p>You are now a customer.</p> <p>Redirecting you to index page in 3 seconds</p>");
                setTimeout(function(){
                    window.location.href = "/";
                }
                  , 3000);

            },
            error: function(xhr, status, error) {
          // Handle errors
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
                $('#success').removeClass('hidden');
        // change the html of #success > div > .message 

                $('#success > div > .message').html("<p class='text-lg font-bold'>Success!</p><p>You are now a barber.</p> <p>Redirecting you to index page in 3 seconds</p>");
            },
            error: function(xhr, status, error) {
          // Handle errors

            }
        });

  // Hide the confirmation dialog
        $('#barber-confirmation-dialog').addClass('hidden');
    });
});