with open("chat.html", "w") as f:
    print >>f, "<body dir='rtl'>"
    print >>f, """\
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
    table, tr, td {
        border-collapse: collapse;
    }
    td {
        padding-top: 10px;
        padding-bottom: 10px;
        vertical-align: top;
        border-bottom: 1px solid #ccc;
    }
    td.name {
        padding-left: 20px;
        font-weight: bold;
    }
    </style>
    """
    print >>f, "<table>"
    prevname = None
    message = []
    for name, text in eval(open("chat.data").read()):
        name = name.decode("utf8")
        text = text.decode("utf8")
        message.append(text)
        if not prevname:
            prevname = name
        if prevname and name != prevname:
            print >>f, ("<tr><td class='name'>%s</td><td class='message'>%s</td></tr>" % (prevname, "<br>".join(message[:-1]))).encode("utf8")
            message = message[-1:]
            prevname = name
    print >>f, "</table>"
    print >>f, "</body>"
