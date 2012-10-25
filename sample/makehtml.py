with open("chat.html", "w") as f:
    print >>f, """\
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style>
.name {
    font-weight: bold;
    float: right;
    clear: right;
    width: 70px;
}
.text {
    float: right;
    margin-right: 10px;
}
.message {
    padding: 5px 0 5px 0;
    border-bottom: 1px solid #ccc;
    float: right;
    clear: right;
    width: 600px;
}
</style>
    """
    print >>f, "<body dir='rtl'>"
    prevname = None
    message = []
    for name, text in eval(open("chat.data").read()):
        name = name.decode("utf8")
        text = text.decode("utf8")
        message.append(text)
        if not prevname:
            prevname = name
        if prevname and name != prevname:
            print >>f, ("<div class='message'><div class='name'>%s</div><div class='text'>%s</div></div>" % 
                (prevname, "<br>".join(message[:-1]))).encode("utf8")
            message = message[-1:]
            prevname = name
    print >>f, "</body>"
