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
 
 This code was generated by :
 Name: Md Sharique
 Email : nukles1.07@gmail.com
 '''

import requests
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class UssdPush(object):

    def __init__(self, From, To, AppName, client):

        self.From = From
        self.To = To
        self.AppName = AppName
        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def Push(self):

        try:

            PushUrl = 'https://cloud.restcomm.com/restcomm-rvd/services/apps/'+self.AppName+'controller'
            Url = self.BaseUrl+'/Accounts/'+self.Sid+'UssdPush'
            data = {'From':self.From, 'To':self.To, 'Url':PushUrl}

            r = requests.post(Url, data=data, auth=(self.Sid,self.AuthToken))

            if r.status_code == 401:
                print("Authentication Error! Please Enter Valid Account Sid and Authentication Token")
            elif r.status_code == 404:
                return "Base Url is Incorrect! Please verify and try again"
            elif r.status_code == 400:
                return "Invalid option"
            else:
                content = json.loads(r.text)
                return content

        except requests.HTTPError:
            return ("HTTP ERROR")
        except requests.ConnectionError:
            return ("CONNECTION ERROR! Please check and try again")
        except requests.Timeout:
            return ("TIMEOUT ERROR")
        except requests.RequestException:
            return ("Invalid Url! Please check and try again")