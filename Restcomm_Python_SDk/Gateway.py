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

class CreateGateway(object):

    def __init__(self,FriendlyName,UserName,Password,Proxy,client):

        self.FriendlyName=FriendlyName
        self.UserName=UserName
        self.Password=Password
        self.Proxy=Proxy
        self.Sid=client.Sid
        self.AuthToken=client.AuthToken
        self.BaseUrl = client.BaseUrl

    def Create(self):

        Url= self.BaseUrl+'/Accounts/'+self.Sid+'/Management/Gateways.json'
        data={'FriendlyName':self.FriendlyName,'UserName':self.UserName,'Password':self.Password,'Proxy':self.Proxy,'Register':'true','TTL':'3600'}
        r1 = requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        content = json.loads(r1.text)
        return content

class GetlistGateway(object):

    def __init__(self,client):

        self.Sid=client.Sid
        self.AuthToken=client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Management/Gateways.json'
        r2 = requests.get(Url,auth=(self.Sid,self.AuthToken))

        content = json.loads(r2.text)
        return content

class UpdateGateway(object):

    def __init__(self,GatewaySid,FriendlyName,UserName,client):

        self.Sid=client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.GatewaySid=GatewaySid
        self.FriendlyName=FriendlyName
        self.UserName=UserName

    def Update(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Management/Gateways.json/'+self.GatewaySid
        data = {'FriendlyName':self.FriendlyName,'UserName':self.UserName}
        r3 = requests.post(Url,data=data,auth=(self.Sid,self.AuthToken))

        content = json.loads(r3.text)
        return content

class DeleteGateway(object):

    def __init__(self,GatewaySid,client):

        self.Sid=client.Sid
        self.AuthToken=client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.GatewaySid=GatewaySid

    def Delete(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Management/Gateways.json/'+self.GatewaySid
        r4 = requests.delete(Url, auth=(self.Sid,self.AuthToken))
        content = json.loads(r4.text)
        return content