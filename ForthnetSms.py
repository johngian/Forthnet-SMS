import mechanize
import cookielib

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

r = br.open('https://www.forthnet.gr/secure/webSMS/default.aspx')

#Site-authentication (email/password)

br.select_form(nr=0)

print "Email:"
login_email = raw_input()
br.form['Username'] = login_email

print "Password:"
password = raw_input()
br.form['Password'] = password

br.submit()

#Send sms
br.select_form(nr=0)

print "Phone Number:"
number = raw_input()
br.form['txtTo'] = number

print "Sms Text:"
message = raw_input()
br.form['txtMessage'] = message

br.submit()

