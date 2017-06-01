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

class RestcommCall(object):

    def __init__(self,Sid,AuthToken,Uri):
        self.Sid=Sid
        self.AuthToken=AuthToken
        self.Uri=Uri

    def MakeCalls(self):

        From=input("Enter the number to call from")
        To=input("Enter the client name to call")
        Url=self.Uri+self.Sid+'/Calls'
        Urls = 'cloud.restcomm.com/restcomm/demos/hello-Play.xml'
        data = {'From': From, 'To':To, 'Url': Urls}

        r1 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        root = ET.fromstring(r1.content)
        for details in root.findall('Call'):
            StartTime=details.find('StartTime').text
            EndTime=details.find('EndTime').text
            Duration=details.find('Duration').text
            Price=details.find('Price').text
            Direction=details.find('Direction').text
            AnsweredBy=details.find('AnsweredBy').text
            ApiVersion=details.find('ApiVersion').text
            ForwardedFrom=details.find('ForwardedFrom').text
            CallerName=details.find('CallerName').text
            Sid = details.find('Sid').text
            Status = details.find('Status').text
            DateCreated = details.find('DateCreated').text
            DateUpdated = details.find('DateUpdated').text


    def GetCallDetail(self):\

        Url = self.Uri + self.Sid + '/Calls'

        r2=requests.get(Url,auth=(self.Sid,self.AuthToken))
        print(r2.content)

    def RedirectCall(self):

        Sid2=''
        Url=self.Uri+self.Sid+'/Calls'+'/'+Sid2
        Url2='cloud.restcomm.com/restcomm/demos/dial­alice.xml'
        data={'Url':Url2}

        r3=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))
        print(r3.content)

    def ConferenceCall(self):

        Sid2 = ''
        Url = self.Uri + self.Sid + '/Calls' + '/' + Sid2
        Url3='cloud.restcomm.com/restcomm/demos/conference.xml'
        data={'Url':Url3,'MoveConnectedCallLeg':'true'}

        r4=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))
        print(r4.content)

    def MuteParticipant(self):

        ParticipantSid=input("Enter the Participant SID")
        ConferenceSid=input("Enter the Conference SID")
        Url = self.Uri + self.Sid +'/Conferences/'+ConferenceSid+'/Participants/'+ParticipantSid
        data={'Mute':'true'}

        r5=requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))
        print(r5.content)

    def UnMuteParticipant(self):
        ParticipantSid = input("Enter the Participant SID")
        ConferenceSid = input("Enter the Conference SID")
        Url = self.Uri + self.Sid + '/Conferences/' + ConferenceSid + '/Participants/' + ParticipantSid
        data = {'Mute': 'false'}

        r6 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        print(r6.content)

def main():

    AccountSid=input("Enter your AccountID")
    Token=input("Enter your Account Token")
    Ur='https://cloud.restcomm.com/restcomm/2012-04-24/Accounts/'
    details=RestcommCall(AccountSid,Token,Ur)
    details.MakeCalls()
    #details.GetCallDetail()
    #details.ConferenceCall()
    #details.MuteParticipant()
    #details.RedirectCall()
    #details.UnMuteParticipant()

if __name__=="__main__":
    main()