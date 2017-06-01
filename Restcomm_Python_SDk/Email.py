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

class RestcommEmail(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def SendEmail(self):

        Url=self.Uri+self.Sid+'/Email/Messages'
        To = input("Enter the Email ID of Receiver")
        From = input("Enter the Email ID of Sender")
        Subject = input("Enter the Subject of an Email")
        Body = input("Enter the message")
        data = {'To':To,'From':From,'Body':Body,'Subject':Subject}
        r1=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        print(r1.text)

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommEmail(AccountSid,Token,Ur)
    details.SendEmail()

if __name__=="__main__":
    main()