import string
import textwrap

BASE64_CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'


def encode_text(text, encoding='utf-8'):
    """Encodes text to base64 using the specified encoding when turning the input text to bytes"""
    return encode_bytes(text.encode(encoding))


def decode_text(base64_text, encoding='uft-8'):
    """Decodes text from base64 using the specified encoding when turning the output bytes to text"""
    return decode_bytes(base64_text).decode(encoding)


def encode_bytes(byte_sequence):
    """Takes a bytes object and turns it into a base64 string"""

    # Create a string of 0s and 1s from the input byte sequence
    binary_string = ''
    for byte in byte_sequence:
        binary_string += format(byte, '08b')

    # Add padding 0s so the number of bits is divisible by 6
    if len(binary_string) % 6 != 0:
        binary_string += (6 - len(binary_string) % 6) * '0'

    # Break up the whole string into a list of 6 bit segments
    six_bit_segments = textwrap.wrap(binary_string, 6)

    # Turn the 6 bit segments into base64 characters and concatenate them
    base64_text = ''
    for segment in six_bit_segments:
        base64_text += BASE64_CHARACTERS[int(segment, 2)]

    # Add padding so that the number of characters in the resulting text is divisible by 4
    if len(base64_text) % 4 != 0:
        base64_text += (4 - len(base64_text) % 4) * '='

    return base64_text


def decode_bytes(base64_text):
    """Takes a base64 string and turns it into a bytes object"""

    # Remove padding
    base64_text = base64_text.rstrip('=')

    # Turn base64 characters into a string of 0s and 1s
    binary_string = ''
    for base64_char in base64_text:
        binary_string += format(BASE64_CHARACTERS.find(base64_char), '06b')

    # Remove padding 0s so the number of bits is divisible by 8
    if len(binary_string) % 8 != 0:
        binary_string = binary_string[:-(len(binary_string) % 8)]

    # Break up the whole string to a list of 8 bit segments
    eight_bit_segments = textwrap.wrap(binary_string, 8)

    # Turn the 8 bit segments into bytes and return them
    ints = []
    for segment in eight_bit_segments:
        ints.append(int(segment, 2))
    return bytes(ints)
