$(function() {
    function submitMessage() {
        text = $("#message").val();
        text = text.replace(/^\n*/, "").replace(/\n*$/, "").replace(/\n/g, "<br>");
        $("#history").append("<p><strong>אני</strong>: " + text + "</p>");
        $("#message").val("").focus();
        $(document).scrollTop($(document).height());
    }

    $("#message").keypress(function(e) {
        var text = $("#message").val();
        if (e.keyCode === 13 && text.match(/\n$/)) {
            if (text.replace(/\n/g, "") !== "") {
                submitMessage();
            }
            e.preventDefault();
        }
    });

    $("#submit").click(function(e) {
        submitMessage();
    })

    $("#message").focus();

});
