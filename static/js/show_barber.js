
    $('#editBtn').on('click',function(){
        $('#editBtn').addClass('hidden');
        $('#doneEditBtn').removeClass('hidden');
        $('#field').addClass('hidden');
        $('#editField').removeClass('hidden');
    }
    );

    $('#doneEditBtn').on('click', function() {
        $('#doneEditBtn').addClass('hidden');
        $('#editBtn').removeClass('hidden');
        $('#field').removeClass('hidden');
        $('#editField').addClass('hidden');

    }
    );




