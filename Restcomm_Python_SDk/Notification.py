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

        self.Sid=Sid
        self.AuthToken=AuthToken
        self.BaseUrl = BaseUrl

class NotificationList(object):

    def __init__(self,client):

        self.Sid=client.Sid
        self.AuthToken=client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/Notifications.json'
        r1=requests.get(Url,auth=(self.Sid,self.AuthToken))

        content = json.loads(r1.text)
        return content

class NotificationFilter(object):

    def __init__(self, ErrorCode, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.ErrorCode = ErrorCode

    def FilterErrorCode(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/Notifications.json?'
        params = {'ErrorCode': self.ErrorCode}
        r2 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r2.text)
        return content

    def FilterPage(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Notifications.json?'
        params = {'PageSize': self.ErrorCode}
        r3 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content