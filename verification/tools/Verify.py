import hashlib
import uuid


class Verification:

    @staticmethod
    def hash_id(id):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + id.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_id(hashed_id, entered_id):
        password, salt = hashed_id.split(':')
        return password == hashlib.sha256(salt.encode() + entered_id.encode()).hexdigest()
