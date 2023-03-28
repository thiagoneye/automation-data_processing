"""
Email Sending

This class enables sending emails through Microsoft Outlook, using the pywin32 package. It can be used to automate the process of composing and sending emails, providing a simpler and more efficient way to interact with Outlook. Please note that the class requires Outlook to be installed on the machine in order to work properly.
"""

# Imports

import win32com.client


# Classes

class Email:
    def __init__(self, to, subject, body, cc=''):
        self.outlook = win32com.client.Dispatch('outlook.application')
        self.mail = self.outlook.CreateItem(0)
        
        self.mail.To = to
        self.mail.Subject = subject
        self.mail.Body = body
        
        if cc != '':
            self.mail.CC = ''
    
    def addAttachments(self, file_path):
        self.mail.Attachments.Add(file_path)
    
    def sendMail(self):
        self.mail.Send()
