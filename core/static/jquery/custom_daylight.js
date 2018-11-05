
$("#pedidoFormsetTable").ready(function () {
    let qtd = $('#qtd_pedido').val();
    let vlr_unitario = $('#vlr_unit_pedido').val();
    let t_item = $('#total_item').val();
});


// Função formset (add line e delete line)
$('#pedidoFormsets tbody tr').formset({
    prefixo: '{{ form_item.prefix }}'
});

$('#compraFormsets tbody tr').formset({
    prefixo: '{{ form_item.prefix }}'
});

$('#serviceFormsets tbody tr').formset({
    prefixo: '{{ form_item.prefix }}'
});


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
