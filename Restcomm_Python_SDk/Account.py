'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2017, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This program is free software: you can redistribute it and/or modify
 * under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation; either version 3 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 '''


import requests
import xml.etree.ElementTree as ET

class RestcommAccount(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def AccountDetails(self):

        Url=self.Uri+self.Sid
        r1=requests.get(Url,auth=(self.Sid,self.AuthToken))
        root = ET.fromstring(r1.content)
        for details in root.findall('Account'):
            FriendlyName = details.find('FriendlyName').text
            Status = details.find('Status').text
            DateCreated = details.find('DateCreated').text
            DateUpdated = details.find('DateUpdated').text

    def ChangePassword(self):

        Password = input("Enter the new Password")
        Url=self.Uri+self.Sid
        data={'AccountSid':self.Sid,'Password':Password}
        r2=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

    def CreateSubAccount(self):

        FriendlyName=input("Enter the friendly Name")
        EmailAddress=input("Enter the email address")
        Password=input("Enter the Password")
        data = {'FriendlyName': FriendlyName, 'EmailAddress': EmailAddress, 'Password': Password}
        r3=requests.post(self.Uri,data=data,auth=(self.Sid,self.AuthToken))
        root = ET.fromstring(r3.content)
        for details in root.findall('Account'):
            FriendlyName = details.find('FriendlyName').text
            Status = details.find('Status').text
            DateCreated = details.find('DateCreated').text
            DateUpdated = details.find('DateUpdated').text
            Role=details.find('Role').text

    def CloseSubAccount(self):

        SubSid=input("Enter the SubAccount SID")
        Url=self.Uri+SubSid
        data = {'Status':'closed'}
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommAccount(AccountSid,Token,Ur)
    details.AccountDetails()
    details.ChangePassword()
    details.CreateSubAccount()
    details.CloseSubAccount()

if __name__=="__main__":
    main()