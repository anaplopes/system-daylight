
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


// Função formset (add line e delete line)
$(function () {
    $('#pedidoFormsetTable tbody tr').formset();
    prefix: '{{ form_itempedido.prefix }}';
});

$(function () {
    $('#compraFormsetTable tbody tr').formset();
    prefix: '{{ form_itemcompra.prefix }}';
});

$(function () {
    $('#servicoFormsetTable tbody tr').formset();
    prefix: '{{ form_itemservico.prefix }}';
});



// Mascara Telefone
$('#telefone').keydown(function () {
    $("#telefone").mask("(99)99999-9999");
});


// Mascara CEP
$('#cep').keydown(function () {
    $("#cep").mask("99999-999");
});


// Mascara Data
$('#datacompra').keydown(function () {
    $("#datacompra").mask("99/99/9999");
});

$('#dataentrega').keydown(function () {
    $("#dataentrega").mask("99/99/9999");
});

$('#dataservico').keydown(function () {
    $("#dataservico").mask("99/99/9999");
});


// Mascara CPF Usuario
$('#cpf_user').keydown(function () {
    $("#cpf_user").mask("999.999.999-99");
});


// Mascara CPF/CNPJ
$("#cpfcnpj").keydown(function () {
    let classif = $("#class_fiscal").val();

    if (classif === 'PF') {
        $("#cpfcnpj").mask("999.999.999-99");
    } else if (classif === 'PJ') {
        $("#cpfcnpj").mask("99.999.999/9999-99");
    }
});


