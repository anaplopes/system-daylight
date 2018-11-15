

// $('#pedidoFormsets').on('submit', function(e){
//     $('#printPedidoModal').modal('show');
//     e.preventDefault();
// });


// calculo total geral (pedido, compra e serviço)
$('.vlr_unitario').blur(function () {
    let total = 0;
    $('.totalitem').each(function(){
        let valor = Number($(this).val());
        total += valor;
    });
    $("#id_valor_total").val(total.toFixed(2));
});


// calculo de total de linha
function calcTotalPedido(){
    let total_form = parseInt($('#id_itempedido_set-TOTAL_FORMS').val());
    let index=0;
    while (index < total_form){
        let qtd = Number($("#id_itempedido_set-"+index+"-quantidade").val());
        let valor_unit= Number($("#id_itempedido_set-"+index+"-valor_unitario").val());
        $("#id_itempedido_set-"+index+"-valor_total").val((valor_unit * qtd).toFixed(2));
        index++
    }
}

function calcTotalCompra(){
    let total_form = parseInt($('#id_itemcompra_set-TOTAL_FORMS').val());
    let index=0;
    while (index < total_form){
        let qtd = Number($("#id_itemcompra_set-"+index+"-quantidade").val());
        let valor_unit= Number($("#id_itemcompra_set-"+index+"-valor_unitario").val());
        $("#id_itemcompra_set-"+index+"-valor_total").val((valor_unit * qtd).toFixed(2));
        index++
    }
}

function calcTotalServico(){
    let total_form = parseInt($('#id_itemservico_set-TOTAL_FORMS').val());
    let index=0;
    while (index < total_form){
        let qtd = Number($("#id_itemservico_set-"+index+"-quantidade").val());
        let valor_unit= Number($("#id_itemservico_set-"+index+"-valor_unitario").val());
        $("#id_itemservico_set-"+index+"-valor_total").val((valor_unit * qtd).toFixed(2));
        index++
    }
}


// Disable em item compra
// $('#item_c_tecido').on('change', function () {
//     $('#item_c_material').attr('disabled', 'disabled')
// });

// $('#item_c_material').on('change', function () {
//     $('#item_c_tecido').attr('disabled', 'disabled')
// });


// Texto
$(".textuppercase").keyup(function () {
    $(this).val($(this).val().toUpperCase());
});

$(".textlowercase").keyup(function () {
    $(this).val($(this).val().toLowerCase());
});

$('.textcapitalize').keyup(function () {
    let texto = $(this).val();
    let separar = texto.split(" ");
    for (let i = 0; i < separar.length; i++) {
        let letra_maiuscula = separar[i].charAt(0).toUpperCase();
        separar[i] = letra_maiuscula + separar[i].substr(1);
    }
    $(this).val(separar.join(" "));
});


// Mascara Telefone
$('.telefone').keydown(function () {
    $(".telefone").mask("(99)99999-9999");
});


// Mascara CEP
$('.cep').keydown(function () {
    $(".cep").mask("99999-999");
});


// Mascara Data
$('.data').keydown(function () {
    $(".data").mask("99/99/9999");
});


// Mascara CPF Usuario
$('.cpf').keydown(function () {
    $(".cpf").mask("999.999.999-99");
});


// Mascara CPF/CNPJ
$(".cpfcnpj").keydown(function () {
    let classif = $(".class_fiscal").val();

    if (classif === 'PF') {
        $(".cpfcnpj").mask("999.999.999-99");
    } else if (classif === 'PJ') {
        $(".cpfcnpj").mask("99.999.999/9999-99");
    }
});


// Mascara CPF/CNPJ Pesquisa
$(".pesq_cpfcnpj").keydown(function () {
    try {
        $(".pesq_cpfcnpj").unmask();
    } catch (e) { }

    let tamanho = $(".pesq_cpfcnpj").val().length;

    if (tamanho < 11) {
        $(".pesq_cpfcnpj").mask("999.999.999-99");
    } else if (tamanho >= 11) {
        $(".pesq_cpfcnpj").mask("99.999.999/9999-99");
    }

    // ajustando foco
    let elem = this;
    setTimeout(function () {
        // mudo a posição do seletor
        elem.selectionStart = elem.selectionEnd = 10000;
    }, 0);
    // reaplico o valor para mudar o foco
    let currentValue = $(this).val();
    $(this).val('');
    $(this).val(currentValue);
});


// API Correios
$(document).ready(function () {

    function limpa_formulário_cep() {
        // Limpa valores do formulário de cep.
        $("#rua").val("");
        $("#bairro").val("");
        $("#cidade").val("");
        $("#uf").val("");
    }

    //Quando o campo cep perde o foco.
    $(".cep").blur(function () {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if (validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $(".rua").val("...");
                $(".bairro").val("...");
                $(".cidade").val("...");
                $(".uf").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $(".rua").val(dados.logradouro);
                        $(".bairro").val(dados.bairro);
                        $(".cidade").val(dados.localidade);
                        $(".uf").val(dados.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });
});


function checkAll() {
    let checkAll_item = $('input[name=checkAll]:checked');
    if (checkAll_item.length){
        $('input[name=check]').each(function() {
            this.checked=true;
        });
    }
    else{
        $('input[name=check]').each(function() {
            this.checked=false;
        });
    }
}


$('#btn_pedidoentregue').click(function() {
    let pedido_check = $('input[name=check]:checked');

    if (!pedido_check.length){
        addAlertMessage('Você deve selecionar pelo menos um pedido para finalizar.',
            'error', 'Nenhuma pedido selecionado');
        return false;
    }

    let lista_pedido = [];
    pedido_check.each(function() {
        lista_pedido.push($(this).val());
    });

    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: 'POST',
        url: "/expedicao",
        data:{
            'lista': lista_pedido,
        },
        dataType: 'json',
        beforeSend: function(xmlHTTPRequest){
            xmlHTTPRequest.setRequestHeader('X-CSRFToken', csrftoken)
        },
        success : function(data){
        },
        error : function (error) {
        }
    });
});
