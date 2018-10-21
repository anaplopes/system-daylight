
$('#bn_addLine').on('click', function() {
    let addline = 1
    $.ajax({
        url: "{% url 'register_pedido' %}",
        type: 'POST',
        data: {
            'addline': addline
        },
        success: function (data) {
        }
    });
});
