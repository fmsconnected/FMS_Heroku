$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columns: [
            {
                data: 'username',
                orderable: true,
                searchable: true,
                className: "center"
            },
            {
                data: 'email',
                orderable: true,
                searchable: true,
                className: "center"
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: USERS_LIST_JSON_URL
    });
});