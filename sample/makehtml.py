print "<body dir='rtl'>"
print """\
<style>
/*
table, tr, td {
    border-collapse: collapse;
}
*/
td {
    padding-top: 10px;
    padding-bottom: 10px;
    vertical-align: top;
}
td.message {
    border-bottom: 1px solid #ccc;
}
td.name {
    padding-left: 20px;
    //color: #ccc;
    font-weight: bold;
}
</style>
"""
print "<table>"
prevname = None
message = []
for name, text in eval(open("chat.data").read()):
    name = name.decode("utf8")
    text = text.decode("utf8")
    message.append(text)
    if not prevname:
        prevname = name
    if prevname and name != prevname:
        print ("<tr><td class='name'>%s</td><td class='message'>%s</td></tr>" % (prevname, "<br>".join(message[:-1]))).encode("utf8")
        message = message[-1:]
        prevname = name
print "</table>"
print "</body>"
