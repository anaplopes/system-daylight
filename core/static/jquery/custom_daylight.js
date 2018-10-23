
function addline(linha) {
    $.ajax({
        url: "/comercial/registrarpedido/",
        type: 'POST',
        data: {
            add: linha
        },
        success: function (data) {
        }
    });
};


/*
$("#qtd_pedido").change(function () {
    let qtd = $('#qtd_pedido').val();
    let vlr_unitario = $('#vlr_unit_pedido').val();
    let t_item = $('#total_item').val(vlr_unitario*qtd);
});

$("#vlr_unit_pedido").change(function () {
    let qtd = $('#qtd_pedido').val();
    let vlr_unitario = $('#vlr_unit_pedido').val();
    let t_item = $('#total_item').val(vlr_unitario * qtd);
});
*/