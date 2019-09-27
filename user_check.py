import os
import os.path
import subprocess
import datetime
import glob
import win32api
import win32con
import win32evtlog
import win32security
import win32evtlogutil
import smtplib, ssl

import email.message
email_content = """
<html>
<body>
<table width="100%" cellpadding="0" cellspacing="0" ><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>

    </tr>
  </table>
 
<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" >
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" >
          <tr>
            <td width="570" align="center"  ><h1>Everything is alright Screens user1</h1></td>
          </tr>

        </table>
      </td>
    </tr>
 
    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>

              <td width="15"></td>
            <td width="350" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://media1.tenor.com/images/78027cef144500d8112970f5499643f9/tenor.gif?itemid=12085990" width ="350" height="250" />
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>

      </td>
    </tr>
  </table>
<!-- top message -->
</td></tr></table><!-- wrapper -->
</body>
</html>
 
 
"""

time = datetime.datetime.now()
current_yearmotnhday = time.strftime("%Y%m%d")
#Check what day is today
#print(current_yearmotnhday)
#Check last hour timestamp
checktime = time -datetime.timedelta(hours = 1)
#checktime = time -datetime.timedelta(minutes = 1)

show_allusers = os.system('query user  /server:dev.mteam.md | find "user1" |find /I "Active"')
user1_dir = "F:/Folder1/folder2/user1"+current_yearmotnhday+"/"
#str(show_allusers)

print(show_allusers)
if show_allusers ==0:
    print("User exist")
    str(current_yearmotnhday)
    #print(type(current_yearmotnhday))
    check_dir = os.path.isdir(user1)
    print(user1)
    #str(check_dir)
    check_dir_dir = os.path.isdir('"F:/Folder1/folder2/user1", + current_yearmotnhday') 
    print("this is step check dir",check_dir_dir)    
    if check_dir :
        print("File exists and is readable")
        files_path = os.path.join(user1_dir,'*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        #print(files[0])
        last_file = files[0]
        print(last_file)
        st = os.stat(last_file)
        print(st.st_mtime)
        mtime = datetime.datetime.fromtimestamp(st.st_mtime)
        print(mtime)
        if mtime > checktime:
            print("fileexist")
            msg = email.message.Message()
            msg['Subject'] = 'Screens'
            msg['From'] = 'youruser@gmail.com'
            msg['To'] = 'touser@gmail.com'
            password = "!!!!!!!!!!!!!!!!!!!!!!!!!!"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())			
            print("fileexist")			

        else:
            print("file doesn exist")
            to = 'touser@gmail.com'
            gmail_user = 'youruser@gmail.com'
            gmail_pwd = '!!!!!!!!!!!!!!!!!!!!'
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo() # extra characters to permit edit
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Screens \n'
            print(header)
            msg = header + '\n Something wrong please check Screens user1 \n\n'
            smtpserver.sendmail(gmail_user, to, msg)     		
#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(files)
        #print("last modified: %s" % os.path.getctime(last_file))
        #print(latest_file) 		
    else:
        print("Either file is missing or is not readable")
        to = 'touser@gmail.com'
        gmail_user = 'youruser@gmail.com'
        gmail_pwd = '!!!!!!!!!!!!!!!!!!!!'
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo() # extra characters to permit edit
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Screens\n'
        print(header)
        msg = header + '\n Either file is missing or is not readable user1 \n\n'
        smtpserver.sendmail(gmail_user, to, msg)
        print('done!')			
		
else:
    print("Doesn't exist") 	
