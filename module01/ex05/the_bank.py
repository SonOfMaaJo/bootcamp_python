class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def check_valid(self, new_account):
        """ Check if an account is valid or not
        """
        if not isinstance(new_account, Account):
            return False
        if len(new_account.__dict__) % 2 == 0:
            return False
        findzip = 0
        findaddr = 0
        for attribut in new_account.__dict__:
            if attribut[0] == 'b':
                return False
            if attribut.find('zip') == 0:
                findzip = 1
            if attribut.find('zip'):
                findaddr = 1
        if (findzip == 0 or findaddr == 0):
            return False
        if not hasattr(new_account, 'name') or not hasattr(new_account, 'id') \
                or not hasattr(new_account, 'value'):
            return False
        if not isinstance(new_account.name, str) or not \
                isinstance(new_account.id, int):
            return False
        if not isinstance(new_account.value, int) and not \
                isinstance(new_account.value, float):
            return False
        return True

    def find_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def add(self, new_account):
        """Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not self.check_valid(new_account):
            return False
        if new_account not in self.accounts:
            self.accounts.append(new_account)
            return True
        else:
            return False

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the firs account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return: True if success, False if an error occured
        """
        if amount < 0 or not isinstance(origin, str) or not isinstance(dest,
                                                                       str):
            return False
        origin_a = self.find_account(origin)
        dest_a = self.find_account(dest)
        if not self.check_valid(origin_a) or not self.check_valid(dest_a):
            return False
        if origin_a.value < amount:
            return False
        dest_a.value = amount
        origin_a.value = origin_a.value - amount
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = self.find_account(name)
        if account is None:
            return False
        if self.check_valid(account):
            return True
        attributs = []
        findzip = 0
        findaddr = 0
        for attribut in account.__dict__:
            if attribut[0] == 'b':
                attributs.append(attribut)
            if attribut.find('zip') == 0:
                findzip = 1
            if attribut.find('addr') == 0:
                findaddr = 1
        for attr in attributs:
            del account.__dict__[attr]
        if (findzip == 0):
            account.__dict__.update({'zip': ''})
        if (findaddr == 0):
            account.__dict__.update({'addr': ''})
        if not hasattr(account, 'id'):
            account.__dict__.update({'id': Account.ID_COUNT})
            Account.ID_COUNT += 1
        if not hasattr(account, 'value'):
            account.__dict__.update({'value': 0})
        return True
