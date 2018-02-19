$(document).ready(function init() {
    $("form").submit(function (event) {
        event.preventDefault();
        $.ajax({
            url: "../../../cgi-bin/cgi_save.py",
            data: $(this).serialize()
        });
    });
    $("#jenson1").click(function () {
        $("#pokaz").hide();
        $("#dodaj").show();
    });
    $("#jenson").click(function () {
        $("#dodaj").hide();
        $("#pokaz").show();
        $.ajax({
            url: "../../../cgi-bin/cgi_read.py"
        }).done(function (responseText) {
            console.log(responseText);
            $("#ajax").html(responseText);
        });
    });
});

