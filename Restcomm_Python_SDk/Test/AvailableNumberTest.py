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

from Restcomm_Python_SDk import AvailableNumber
import unittest
import requests
from unittest.mock import Mock, patch

class TestAvailableNumber(unittest.TestCase):

    def test_Availability(self):

        try:

            with patch.object(requests, 'get')as get_mock:

                file2 = open('index.html', 'w')

                message = """<AvailableNumbers>
                <AvailableNumber>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <FriendlyName>+919840274356</FriendlyName>
                <PhoneNumber>+919840274356</PhoneNumber
                </AvailableNumber>
                </AvailableNumbers>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("AvailableNumberData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                AreaCode = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = AvailableNumber.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AvailableNumber.NumberAvailablity(AreaCode, data).Availability()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

if __name__=="__main__":
    unittest.main()