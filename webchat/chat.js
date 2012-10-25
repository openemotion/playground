function submitMessage() {
    var text = document.getElementById("message").value;
    var history = document.getElementById("history");
    var item = document.createElement("p");
    text = text.replace(/^\n*/, "").replace(/\n*$/, "").replace(/\n/g, "<br>");
    item.innerHTML = "<strong>אני</strong>: " + text;
    history.appendChild(item);
    history.scrollTop = history.scrollHeight;
    document.getElementById("message").value = "";
    window.scrollTo(0, document.body.scrollHeight);
    document.getElementById("message").focus();
}

function onMessageKey() {
    submitTime = 0;
    var key = window.event.keyCode;
    var text = document.getElementById("message").value;
    if (key === 13 && text.match(/\n$/)) {
        if (text.replace(/\n/g, "") !== "") {
            submitMessage();
        }
        this.event.preventDefault();
    }
}
