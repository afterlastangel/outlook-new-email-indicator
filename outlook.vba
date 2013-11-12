'Author: Le Kien Truc <afterlastangel@gmail.com>
'https://github.com/afterlastangel/outlook-new-email-indicator
'GPL V3
'
'
'


Public Sub SendUbuntuNotification(Item As Outlook.MailItem)
 
Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")
   URL = "http://10.20.12.141:8001/email"
   objHTTP.Open "GET", URL, False
   objHTTP.setRequestHeader "User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
   lResolve = 4 * 1000
   lConnect = 4 * 1000
    lSend = 4 * 1000
    lReceive = 4 * 1000 'waiting time to receive data from server
    objHTTP.setTimeOuts lResolve, lConnect, lSend, lReceive

   objHTTP.Send ("")
 End Sub
