
$(document).ready(function () {
    $("#date-popover").popover({
        html: true,
        trigger: "manual"
    });
$("#date-popover").hide();
    $("#date-popover").click(function (e) {
    $(this).hide();
});

    $("#my-calendar").zabuto_calendar({
    action: function () {
        return myDateFunction(this.id, false);
},
    action_nav: function () {
        return myNavFunction(this.id);
},
    ajax: {
    url: "",
modal: true
},
});
});

function myNavFunction(id) {
    $("#date-popover").hide();
var nav = $("#" + id).data("navigation");
var to = $("#" + id).data("to");
console.log('nav ' + nav + ' to: ' + to.month + '/' + to.year);
}