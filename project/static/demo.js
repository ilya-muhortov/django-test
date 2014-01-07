
$(document).ready(function() {

    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var editable_defaults = {
        indicator : 'Loading...',
        tooltip   : "Click to edit...",
        style  : "inherit",
        datepicker: {
            dateFormat: 'dd.mm.yy'
        },
        ajaxoptions: {
            dataType: 'json'
        },
        submitdata : function(value, settings) {
            return {
                'field': $(this).attr('data-field'),
                'object_pk': $(this).attr('data-pk')
            }
        },
        callback : function(result, settings) {
            if (result.error !== undefined) {
                $(this).html(result.value).trigger('click');
                $(this).after('<span>' + result.error + '</span>');
            }
            else if (result.value !== undefined) {
                $(this).html(result.value);
            }
        },
        onsubmit: function(form, el) {
            $(el).next('span').remove();
        }
    };

    function init_editable(url) {
        $('.edit-field[data-type="IntegerField"], .edit-field[data-type="CharField"]')
            .editable(url, $.extend(editable_defaults, {'type': 'text'}));

        $('.edit-field[data-type="DateField"]')
            .editable(url, $.extend(editable_defaults, {'type': 'datepicker'}));
    }

    $(document).on('click', '.sidebar > a', function(){
        var self = this;
        $.get($(self).attr('href'), {}, function(data){
            $('#content').empty().append(tmpl("table-data", data));
            init_editable($(self).attr('href'));
        }, 'json');

        return false;
    });
});