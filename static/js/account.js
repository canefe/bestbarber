var modalTemplate = `
<div class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <div class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>

    <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
      <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
        <div class="sm:flex sm:items-start">
          <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-cyan-100 sm:mx-0 sm:h-10 sm:w-10">
            <svg class="h-6 w-6 text-cyan-600" stroke="currentColor" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
          </div>
          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
              Edit Field
            </h3>
            <div class="mt-2">
              <p class="text-sm text-gray-500">
                Enter the new value for the field:
              </p>
              <input type="text" id="new-value" name="new-value" class="mt-1 focus:ring-cyan-500 focus:border-cyan-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
            </div>
          </div>
        </div>
      </div>
      <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
        <button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-cyan-600 text-base font-medium text-white hover:bg-cyan-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500 sm:ml-3 sm:w-auto sm:text-sm" id="save-changes">
          Save Changes
        </button>
        <button type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm" id="cancel">
          Cancel
        </button>
      </div>
    </div>
  </div>
</div>
`;

$(function() {
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
    // on click to any clickable-field
  $('.clickable-field').click(function() {
        // get the data-field attribute
    var field = $(this).data('field');

        // create the modal content with a form
    var modalContent = '<form>';
    modalContent += '<label for="' + field + '">' + field + '</label>';
    modalContent += '<input type="text" id="' + field + '" name="' + field + '" value="' + user.userprofile[field] + '">';
    modalContent += '</form>';

        // show the modal and get the save button
    var saveButton = showModal('Edit ' + field, modalContent);

        // add event listener to save button
    saveButton.click(function() {
          // get the new value from the form
      var newValue = $('#' + field).val();

          // update the user profile field
      user.userprofile[field] = newValue;

          // update the clickable field with the new value
      $(this).siblings('.text-gray-900').text(newValue);

          // remove the modal
      $(this).closest('.modal').remove();
    });
  });


  function showModal(title, content) {
        // create modal elements
    var modal = $('<div>').addClass('modal fixed w-full h-full top-0 left-0 flex items-center justify-center');
    var overlay = $('<div>').addClass('modal-overlay absolute w-full h-full bg-gray-900 opacity-50');
    var container = $('<div>').addClass('modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto');

        // create modal header
    var header = $('<div>').addClass('modal-header py-3 px-4 text-white bg-gray-900 rounded-t');
    var headerTitle = $('<h3>').addClass('text-lg font-semibold').text(title);
    var closeButton = $('<button>').addClass('modal-close-btn text-white hover:text-gray-300 ml-auto focus:outline-none');
    closeButton.html('&times;');
    header.append(headerTitle, closeButton);

        // create modal content
    var modalContent = $('<div>').addClass('modal-content py-4 text-left px-6');
    modalContent.html(content);

        // create modal footer
    var footer = $('<div>').addClass('modal-footer py-3 px-4 text-right bg-gray-100 rounded-b');
    var saveButton = $('<button>').addClass('modal-save-btn px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded');
    saveButton.text('Save');
    footer.append(saveButton);

        // add all elements to the modal
    container.append(header, modalContent, footer);
    modal.append(overlay, container);

        // add modal to the page
    $('body').append(modal);

        // add event listener to close modal when close button or overlay is clicked
    closeButton.click(function() {
      modal.remove();
    });
    overlay.click(function() {
      modal.remove();
    });

        // return the save button to add event listener for saving the changes
    return saveButton;
  }


});
