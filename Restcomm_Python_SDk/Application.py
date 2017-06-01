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

class RestcommApplication(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def CreateApplication(self):

        Url=self.Uri+self.Sid+'/Applications'
        FriendlyName=input("Enter the Friendly Name")
        RcmUrl='cloud.restcomm.com/restcomm-rvd/services/apps/foobar/controller'
        kind=input("Enter your choice of application")
        data={'FriendlyName':FriendlyName,'ApiVersion':'2012-04-24','HasVoiceCallerIdLookup':'false','RcmUrl':RcmUrl,'Kind':kind}
        r1=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        print(r1.content)

    def DeleteApplication(self):

        RequiredSid=input("enter the SID of the Application to be deleted")
        Url=self.Uri+self.Sid+'/Applications/'+RequiredSid
        r2=requests.delete(Url,auth=(self.Sid,self.AuthToken))

        print(r2.content)

    def UpdateApplication(self):

        RequiredSid = input("enter the SID of the Application to be deleted")
        Url = self.Uri + self.Sid + '/Applications/' + RequiredSid
        FriendlyName=input("enter new friendly name")
        data={'FriendlyName':FriendlyName}
        r3=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        print(r3.content)

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommApplication(AccountSid,Token,Ur)
    details.CreateApplication()
    details.DeleteApplication()

if __name__=="__main__":
    main()