#!/usr/bin/env python3


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def iscorrupted(self):
        ret = True
        if len(self.__dict__) % 2 == 1:
            return True
        for each in self.__dict__:
            if each.startswith('b'):
                return True
            if each.startswith('zip') or each.startswith('addr'):
                ret = False
        if 'name' not in self.__dict__:
            return True
        if 'id' not in self.__dict__:
            return True
        if 'value' not in self.__dict__:
            return True
        return ret

    def fix(self):
        if self.iscorrupted() is False:
            return True
        for each in self.__dict__:
            if each.startswith('b'):
                del self.__dict__[each]
                break
        if 'name' not in self.__dict__:
            self.__dict__.update(name="Default")
        if 'value' not in self.__dict__:
            self.__dict__.update(value=0)
        if 'id' not in self.__dict__:
            self.__dict__.update(id=self.ID_COUNT)
            self.ID_COUNT += 1
        if (self.iscorrupted()):
            return False
        return True


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the dest account
            @amount: float(amount) to transfer
            @return			True if success, False if an error ocurred
        """
        orig = None
        dst = None
        for each in self.account:
            if each.iscorrupted():
                if self.account[each].fix() is False:
                    print("Corrupted account")
                    return
            if origin == each.name or origin == each.id:
                orig = each
            if dest == each.name or dest == each.id:
                dst = each

        if orig is None or dst is None:
            print("Account does not exist.")
            return
        if orig.value < amount:
            print("Not enough money to make the transfer")
            return
        dst.value += amount
        orig.value -= amount
        print("Transfer succesful:\n"
              + "\tFrom {} to {}.".format(dst.name, orig.name))
        print("\t{}: current balance: {}".format(orig.name, orig.value))
        print("\t{}: current balance: {}".format(dst.name, dst.value))

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return			True if success, False if error
        """
        if type(account) is not Account:
            return False
        for acc in self.account:
            if acc == account:
                return acc.fix()
        return False
