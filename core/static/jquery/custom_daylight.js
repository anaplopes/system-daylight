


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
$('.cpf_user').keydown(function () {
    $(".cpf_user").mask("999.999.999-99");
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
    let checkAll_novidade = $('input[name=checkAll]:checked');
    if (checkAll_novidade.length){
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
