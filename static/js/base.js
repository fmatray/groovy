// Base.js

$( document ).ready(function() {
    // Datapickers
    $("input[name*='_date']").each(function () {
            $(this).datepicker({format:"yyyy-mm-dd"});
        });

    //Tooltips
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })

});

