import imaplib
import re as regex
 
def getGmailUnread(bhuifarz, mtchcxwpawpgwfcd):
 
  gmail = imaplib.IMAP4_SSL('imap.gmail.com','993')
  gmail.login(bhuifarz,mtchcxwpawpgwfcd)
  gmail.select()
 
  unreadCount = regex.search("UNSEEN (/d+)", gmail.status("INBOX", "(UNSEEN)")[1][0]).group(1)
 
  unreadCount = int(unreadCount)
   
  return unreadCount
   
if __name__ == '__main__':
   
  unreadCount = getGmailUnread('bhuifarz@gmail.com','mtchcxwpawpgwfcd')
 
  if unreadCount == 0:
      print ('no new mail')
  elif unreadCount == 1:
      print ('1 new mail')
  else:
      print (str(unreadCount) + ' new mails')