import os
import string
import logging
import platform
from cryptography.fernet import Fernet


class Cript:
    """
    A class used for the encryption and decryption of data, which uses Fernet
    symmetric encryption.

    :Example:

        >>> cript = Cript()
        >>> encrypted_data = cript.cripto_data("some sensitive data")
        >>> original_data = cript.decripto_data(encrypted_data)

    """

    def __init__(self):
        """
        Constructor method.
        Initializes the Cript object with None as the key.
        """
        self.key = None

    @staticmethod
    def create_folder(path):
        """
        Creates a folder at the specified path.

        :param path: Path to the folder to be created.
        :type path: str
        :return: Absolute path to the folder.
        :rtype: str
        """
        path = os.path.abspath(path)
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def create_path_to_save():
        """
        Creates a path for storing the key file.

        :return: Path to the key file.
        :rtype: str
        """
        system = platform.system()

        if system == 'Windows':
            # Path for AppData in Windows
            current_user = os.getenv('LOCAL_PATH')
            path_store_key = os.path.abspath(current_user + '/AppData/Local/bgui')
        elif system == 'Linux':
            home_dir = os.path.expanduser('~')  # Gets the home directory
            path_store_key = os.path.join(home_dir, '.bgui')  # Creates a path within the home directory
            os.makedirs(path_store_key, exist_ok=True)
        else:
            logging.error(f"Unsupported operating system: {system}")
            return
        os.makedirs(path_store_key, exist_ok=True)
        return path_store_key

    def generate_secret_key(self):
        """
        Generates a Fernet key and saves it into a file.

        :return: None
        """
        key = Fernet.generate_key()
        path_store_key = os.path.abspath(self.create_path_to_save())
        if not os.path.exists(f"{path_store_key}/h.b"):
            with open(f"{path_store_key}/h.b", "wb") as key_file:
                key_file.write(key)

    def load_key(self):
        """
        Loads the Fernet key from a file.

        :return: None
        """
        path_store_key = os.path.abspath(self.create_path_to_save())
        with open(f"{path_store_key}/h.b", "rb") as key_file:
            self.key = key_file.read()

    def salting(self, dados):
        """
        Salts the input data by interspersing it with ASCII characters.

        :param dados: Data to be salted.
        :type dados: str
        :return: Salted data.
        :rtype: str
        """
        salted = ''
        salt = string.ascii_uppercase + string.ascii_lowercase
        for i, c in enumerate(dados[::-1]):
            index = salt.find(c)
            salted += c + salt[i] if index == -1 else salt[index - 7] + salt[i]
        return salted

    def d_salt(self, salted):
        """
        Removes the salt from the input data.

        :param salted: Salted data.
        :type salted: str
        :return: Original unsalted data.
        :rtype: str
        """
        original_dados = ''
        salt = string.ascii_uppercase + string.ascii_lowercase
        for i, c in enumerate(salted[::-1]):
            index = salt.find(c)
            index_char_alt_range = salt[-7:].find(c)
            d_salted = salt[index + 7] if index_char_alt_range == -1 else salt[index_char_alt_range]
            if i % 2 != 0:
                original_dados += c if index == -1 else d_salted
        return original_dados

    def cripto_data(self, dados):
        """
        Encrypts and salts the input data.

        :param dados: Data to be encrypted.
        :type dados: str
        :return: Encrypted data.
        :rtype: str
        """
        self.generate_secret_key()
        if self.key is None:
            self.load_key()

        salted = self.salting(dados)
        salted = salted.encode()
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(salted)
        dado_text = str(cipher_text.decode())
        return dado_text

    def decripto_data(self, dado_text):
        """
        Decrypts the input data and removes the salt.

        :param dado_text: Data to be decrypted.
        :type dado_text: str
        :return: Decrypted data.
        :rtype: str
        """
        if self.key is None:
            self.load_key()
        cipher_suite = Fernet(self.key)
        plain_text = cipher_suite.decrypt(dado_text.encode())
        salted = str(plain_text.decode())
        original_dado = self.d_salt(salted)
        return original_dado
