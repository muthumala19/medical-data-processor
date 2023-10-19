import hashlib
import base64
def hash_password(user_password):
    # Create a new MD5 hash object
    hashed_password = hashlib.md5(user_password.encode("utf-8"))

    # Return the hexadecimal digest of the hash
    return hashed_password.hexdigest()

def encode(encode_text):
    # Encode the text using Base64
    base64_bytes = base64.b64encode(encode_text.encode('ascii'))

    # Convert the bytes to a UTF-8 encoded string
    base64_message = base64_bytes.decode('ascii')

    return base64_message

def decode(decode_text):
    # Decode the Base64 encoded text
    message_bytes = base64.b64decode(decode_text.encode('ascii'))

    # Convert the bytes to a UTF-8 encoded string
    message = message_bytes.decode('ascii')

    return message
