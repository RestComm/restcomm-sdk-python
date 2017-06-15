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
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class AccountDetails(object):

    def __init__(self,client):
        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def Details(self):

        Url=self.BaseUrl+'/Accounts.json/'+self.Sid
        r1=requests.get(Url, auth=(self.Sid,self.AuthToken))
        content = json.loads(r1.text)

        return content

class ChangeAccountPassword(object):

    def __init__(self, Password, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.Password = Password

    def ChangePassword(self):

        Url = self.BaseUrl+'/Accounts.json/'+self.Sid
        data = {'AccountSid': self.Sid, 'Password': self.Password}
        r2 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        content = json.loads(r2.text)
        return content

class CreateSubAccount(object):

    def __init__(self, FriendlyName, EmailAddress, Password, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.Password = Password
        self.FriendlyName = FriendlyName
        self.EmailAddress = EmailAddress

    def Create(self):

        Url = self.BaseUrl+'/Accounts.json/'
        data = {'FriendlyName': self.FriendlyName, 'EmailAddress': self.EmailAddress, 'Password': self.Password}
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content

class CloseSubAccount(object):

    def __init__(self, SubSid, client):
        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.SubSid = SubSid

    def Close(self):

        Url = self.BaseUrl+'/Accounts.json/'+self.SubSid
        data = {'Status': 'closed'}
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content

class SubAccountDetails(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def Details(self):

        Url = self.BaseUrl+'/Accounts.json/'
        r4 = requests.get(Url, auth=(self.Sid, self.AuthToken))
        content = json.loads(r4.text)
        return content