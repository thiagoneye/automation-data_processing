"""
Connection with SAP

This class allows you to make a Python connection with the SAP GUI Scripting API for transaction
automation.

- Documentation:
https://help.sap.com/docs/sap_gui_for_windows/b47d018c3b9b45e897faf66a6c0885a8/babdf65f4d0a4bd8b40f5ff132cb12fa.html?locale=en-US&version=760.01
"""

# Imports

import time
import subprocess
import sys
import win32com.client


# Classes

class SAPGui:
    """
    SAP GUI Scripting API
    """

    def __init__(self, connection_name):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

        subprocess.Popen(self.path)

        self.sap_gui_auto = win32com.client.GetObject("SAPGUI")
        self.application = self.sap_gui_auto.GetScriptingEngine
        self.connection = self.application.OpenConnection(connection_name, True)

        time.sleep(3)

        self.session = self.connection.Children(0)

    def sap_login(self, mandante, username, password):
        """
        Function for performing user login.
        """
        try:
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = mandante
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
            self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "PT"
            self.session.findById("wnd[0]").sendVKey(0)
        except:
            print(sys.exc_info()[0])

    def end_transaction(self):
        """
        Function for finalizing the transaction.
        """
        self.session.EndTransaction()

    def close_connection(self):
        """
        Function to end connection.
        """
        self.connection.CloseConnection()
