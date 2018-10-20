// função que gera numero aleatorio
function num_aleatorio() {
    let dataAtual = new Date();
    let ano_agora = dataAtual.getFullYear();
    let n_aleatorio = Math.floor(Math.random() * 100001);
    return ano_agora + "" + n_aleatorio
}


// numero aleatorio no formulario de pedido
$('#form_pedido').ready(function() {
    $('#numero_pedido').val(num_aleatorio());
})


