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

class RestcommSms(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def SendSms(self):

        Url=self.Uri+self.Sid+'/SMS/Messages'
        To = '%2B'+input("Enter the Mobile Number of Receiver")
        From = '%2B'+input("Enter the Mobile Number of Sender")
        Body = input("Enter the message")
        data = {'To':To,'From':From,'Body':Body}
        r1=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        print(r1.text)

    def SmsList(self):

        Url=self.Uri+self.Sid+'/SMS/Messages'
        r2=requests.get(Url,auth=(self.Sid,self.AuthToken))

        print(r2.text)

    def FilterSmsList(self):
        Url = self.Uri + self.Sid + '/SMS/Messages?'
        FilterNumber=input("Enter the number to get data")
        params={'From':FilterNumber}
        r3 = requests.get(Url,params=params, auth=(self.Sid, self.AuthToken))

        print(r3.text)

    def PagingInformation(self):

        Url=self.Uri+self.Sid+'/SMS/Messages?'
        PageSize=input("Enter the size of the page")
        params={'PageSize':PageSize}

        r4=requests.get(Url,params=params,auth=(self.Sid,self.AuthToken))

        print(r4.text)

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommSms(AccountSid,Token,Ur)
    details.SendSms()
    details.SmsList()
    details.FilterSmsList()
    details.PagingInformation()

if __name__=="__main__":
    main()