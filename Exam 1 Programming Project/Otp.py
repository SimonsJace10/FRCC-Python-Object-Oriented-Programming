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
    def __random_key(length):
        # generate length random bytes
        tb = token_bytes(length)
        # convert those bytes into a bit string and return it
        return int.from_bytes(tb, "big")
       

if __name__ == "__main__":
    secretMsg = Otp("One Time Pad!")
    secretMsg.encrypt()
    print (secretMsg.decrypt())
    
    print(secretMsg)
