#!/usr/bim/env python3

import cgi
out_form = cgi.FieldStorage()
firstname = out_form.getfirst("firstname","not valid")
piz = out_form.getfirst("piz","")
number = out_form.getfirst("number","not valid")
add = out_form.getfirst("address")
print("Content-type: text/html")
print()
print("Thank you, ",firstname, "for using our services","\n","Your Pizza: ", piz, "was arrived to: ", add)