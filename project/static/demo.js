$(document).ready(function() {

    var editable_defaults = {
        indicator : "<img src='img/indicator.gif'>",
        tooltip   : "Click to edit...",
        style  : "inherit",
        submitdata : function(value, settings) {
            return {
                'field': $(this).attr('data-field'),
                'object_pk': $(this).attr('data-pk')
            }
        }
    };

    $(".edit-text").editable("/save/", $.extend(editable_defaults, {'type': 'text'}));
    $(".edit-textarea").editable("/save/", $.extend(editable_defaults, {'type': 'textarea'}));

});