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

class NumberAvailablity(object):

    def __init__(self, AreaCode, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.AreaCode = AreaCode

    def Availability(self):

        try:

            Url = self.BaseUrl+'/Accounts/'+self.Sid+'/AvailablePhoneNumbers/US/Local.json'
            param = {'AreaCode':self.AreaCode}
            r1 = requests.get(Url, params=param, auth=(self.Sid, self.AuthToken))

            if r1.status_code == 401:
                print("Authentication Error! Please Enter Valid Account Sid and Authentication Token")
            else:
                content = json.loads(r1.text)
                return content

        except requests.HTTPError:
            print("HTTP ERROR")
        except requests.ConnectionError:
            print("CONNECTION ERROR! Please check and try again")
        except requests.Timeout:
            print("TIMEOUT ERROR")
        except requests.RequestException:
            print("Invalid Url! Please check and try again")
