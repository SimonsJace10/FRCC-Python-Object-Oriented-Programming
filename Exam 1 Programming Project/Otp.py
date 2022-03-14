# unbreakable_encryption.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from secrets import token_bytes
from typing import Tuple


class Otp(object):
    def __init__(self, m):
        self.msg = m

    @staticmethod
    def random_key(length):
        # generate length random bytes
        tb = token_bytes(length)
        # convert those bytes into a bit string and return it
        return int.from_bytes(tb, "big")

    # the encrypt method can't be static and needs self as an argument because it needs to access the member method of
    # random_key in order to generate a dummy key
    def encrypt(self):
        original_bytes = self.msg.encode()
        dummy = self.random_key(len(original_bytes))
        original_key = int.from_bytes(original_bytes, "big")
        encrypted = original_key ^ dummy  # XOR
        return dummy, encrypted

    # the static decrypt method provides a decryption using the passed in keys, which are returned by the encrypt()
    # method above
    @staticmethod
    def decrypt(key1, key2):
        decrypted = key1 ^ key2  # XOR
        temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
        return temp.decode()
       

if __name__ == "__main__":
    secretMsg = Otp("One Time Pad!")
    # print the passed in string to confirm that it revealed the correct message
    print(secretMsg.msg)
    # create a tuple that stores the two returned keys from the encrypt() method
    returned_keys = (secretMsg.encrypt())
    # print the decrypted string, by calling the decrypt method and passing in the keys stored in the tuple
    print("secret message is: " + secretMsg.decrypt(returned_keys[0], returned_keys[1]))
