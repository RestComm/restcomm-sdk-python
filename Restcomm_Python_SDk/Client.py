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

class RestcommClient(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def CreateClient(self):

        Url=self.Uri+self.Sid+'/Clients'
        Login=input("Enter the new client Username")
        Password=input("Enter the new client password")
        data={'Login':Login,'Password':Password}
        r1=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        root = ET.fromstring(r1.content)
        for details in root.findall('Client'):
            Sid = details.find('Sid').text
            Status = details.find('Status').text
            DateCreated = details.find('DateCreated').text
            DateUpdated = details.find('DateUpdated').text
            ApiVersion = details.find('ApiVersion').text

        print(r1.content)

    def DeleteClient(self):

        ClientSid=input("Enter the client Sid")
        Url = self.Uri + self.Sid + '/Clients/'+ClientSid
        r2=requests.delete(Url,auth=(self.Sid,self.AuthToken))

        print(r2.content)

    def ChangePassword(self):

        ClientSid = input("Enter the client Sid")
        Password = input("Enter the new client password")
        Url = self.Uri + self.Sid + '/Clients/' + ClientSid
        data = {'Password': Password}
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        print(r3.content)

    def ClientList(self):

        Url = self.Uri + self.Sid + '/Clients/'
        r4=requests.get(Url,auth=(self.Sid,self.AuthToken))

        print(r4.content)

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommClient(AccountSid,Token,Ur)
    details.CreateClient()
    details.ChangePassword()
    details.ClientList()
    details.DeleteClient()


if __name__=="__main__":
    main()