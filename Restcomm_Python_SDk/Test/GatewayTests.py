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

from Restcomm_Python_SDk import Gateway
import unittest
import vcr

class TestCreateGateway(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:

                file = open("GatewayData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                FriendlyName = file.readline()
                UserName = file.readline()
                Password = file.readline()
                Proxy = file.readline()

                data = Gateway.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Gateway.CreateGateway(FriendlyName.strip(), UserName.strip(), Password.strip(), Proxy.strip(), data).Create()

                self.assertIsNotNone(content)
                file.close()

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestGetListGateway(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_GetList(self):

        try:

                file = open("GatewayData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()

                data = Gateway.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Gateway.GetlistGateway(data).GetList()

                self.assertIsNotNone(content)
                file.close()

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestUpdateGateway(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Update(self):

        try:

                file = open("GatewayData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                FriendlyName = file.readline()
                UserName = file.readline()
                file.readline()
                file.readline()
                GatewaySid = file.readline()

                data = Gateway.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Gateway.UpdateGateway(GatewaySid.strip(), FriendlyName.strip(), UserName.strip(), data)

                self.assertIsNotNone(content)
                file.close()

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestDeleteGateway(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Delete(self):

        try:

                file = open("GatewayData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                GatewaySid = file.readline()

                data = Gateway.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Gateway.DeleteGateway(GatewaySid.strip(), data).Delete()

                self.assertIsNotNone(content)
                file.close()

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

if __name__ == '__main__':
    unittest.main()