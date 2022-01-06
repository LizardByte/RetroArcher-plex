"""
ms_cv - Microsoft Correlation Vector, used for telemetry purposes by Microsoft Web APIs
Source: https://github.com/Microsoft/Telemetry-Client-for-Android/blob/master/AndroidCll/src/main/java/com/microsoft/cll/android/CorrelationVector.java
"""

__version__ = '0.1.1'
__author__ = 'OpenXbox <noreply@openxbox.org>'
__all__ = []


import re
import math
import random

class CorrelationVector(object):
    MAX_CORRELATION_VECTOR_LENGTH = 20
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    ID0_LENGTH = 16
    INT_MAX_VALUE = 2147483647

    def __init__(self):
        self.base_vector = self.seed_correlation_vector()
        self.current_vector = 1

    def can_extend(self):
        vector_size = math.floor(math.log10(self.current_vector) + 1)
        if len(self.base_vector) + 1 + vector_size + 1 + 1 > self.MAX_CORRELATION_VECTOR_LENGTH:
            return False
        else:
            return True

    def can_increment(self, new_vector):
        if new_vector - 1 == self.INT_MAX_VALUE:
            return False
        vector_size = math.floor(math.log10(new_vector) + 1)
        if len(self.base_vector) + vector_size + 1 > self.MAX_CORRELATION_VECTOR_LENGTH:
            return False
        else:
            return True

    def extend(self):
        if self.can_extend():
            self.base_vector = self.get_value()
            self.current_vector = 1
        return self.get_value()

    def get_value(self):
        return '%s.%s' % (self.base_vector, self.current_vector)

    def increment(self):
        new_vector = self.current_vector + 1
        if self.can_increment(new_vector):
            self.current_vector = new_vector
        return self.get_value()

    def is_valid(self, vector):
        if len(vector) > self.MAX_CORRELATION_VECTOR_LENGTH:
            return False
        validation_pattern = re.compile('^[' + self.CHARSET + ']{16}(.[0-9]+)+$')
        if not validation_pattern.match(vector):
            return False
        else:
            return True

    def seed_correlation_vector(self):
        return ''.join([random.choice(self.CHARSET) for i in range(self.ID0_LENGTH)])

    def set_value(self, vector):
        if self.is_valid(vector):
            base, current = vector.split('.')
            self.base_vector = base
            self.current_vector = int(current)
        else:
            raise Exception('Cannot set invalid correlation vector value')