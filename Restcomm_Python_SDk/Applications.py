'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2016, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 '''

import requests
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class CreateApplication(object):

    def __init__(self, FriendlyName, kind, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.FriendlyName = FriendlyName
        self.kind = kind

    def Create(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Applications.json'
        RcmUrl = 'cloud.restcomm.com/restcomm-rvd/services/apps/foobar/controller'
        data = {'FriendlyName': self.FriendlyName, 'ApiVersion': '2012-04-24', 'HasVoiceCallerIdLookup': 'false',
                'RcmUrl': RcmUrl, 'Kind': self.kind}
        r1 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r1.text)
        return content

class DeleteApplication(object):

    def __init__(self, AppSid, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.AppSid = AppSid

    def Delete(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Applications.json/'+self.AppSid
        r2 = requests.delete(Url, auth=(self.Sid, self.AuthToken))

        content = json.loads(r2.text)
        return content

class UpdateApplication(object):

    def __init__(self, AppSid, FriendlyName, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.AppSid = AppSid
        self.FriendlyName = FriendlyName

    def Update(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Applications.json/' + self.AppSid
        data = {'FriendlyName': self.FriendlyName}
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content

class GetApplicationList(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Applications.json/'
        r4 = requests.get(Url, auth = (self.Sid, self.AuthToken))

        content = json.loads(r4.text)
        return content