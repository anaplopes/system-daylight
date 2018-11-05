function imprime_alertas(){
    let alertas = $('.alert_message');
    alertas.each(function(){
        new PNotify({
            type: $(this).attr('data-type'),
            styling: 'bootstrap3',
            title: $(this).attr('data-title'),
            buttons: {closer: true, sticker: false},
            text: $(this).text(),
            delay: 1000,
        });
        $(this).remove();
    });
};

$(document).ready(function() {
    imprime_alertas();
});

function addAlertMessage(text, type, title=null){
    div = document.createElement('div');
    $(div).addClass('alert_message')
        .html(text)
        .attr('data-type', type)
        .attr('data-title', title)
        .hide()
        .appendTo($('body'));

    imprime_alertas();
};