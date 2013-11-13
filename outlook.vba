'Author: Le Kien Truc <afterlastangel@gmail.com>
'https://github.com/afterlastangel/outlook-new-email-indicator
'GPL V3
'
'
'


Private Sub Application_Reminder(ByVal Item As Object)
    SendNotification ("reminder")
End Sub

Private Sub Application_NewMail()
    SendNotification ("email")
End Sub
Private Sub SendNotification(notiCode As String)
    Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")
    URL = "http://10.20.12.141:8001/" + notiCode
   objHTTP.Open "GET", URL, False
   objHTTP.setRequestHeader "User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
   lResolve = 10 * 1000
   lConnect = 10 * 1000
    lSend = 10 * 1000
    lReceive = 10 * 1000 'waiting time to receive data from server
    objHTTP.setTimeOuts lResolve, lConnect, lSend, lReceive
    objHTTP.Send ("")
End Sub


