$(function() {
    function submitMessage() {
        text = $("#message").val();
        text = text.replace(/^\n*/, "").replace(/\n*$/, "").replace(/\n/g, "<br>");
        author = $("#author").val()
        // FIXME: this duplicates the code in templates/messages.html
        $("#history").append("<p><strong>" + author + "</strong>: " + text + "</p>");
        $("#message").val("").focus();
        $.post("/message", {author : author, text : text}, function (data, textStatus, jqXHR) {
            reloadHistory();
        });
    }

    function reloadHistory() {
        $.ajax("/history", {success: function (data, textStatus, jqXHR) {
            $("#history").empty().append(data);
            $(document).scrollTop($(document).height());
        }});
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

    setInterval(reloadHistory, 1000);
});
