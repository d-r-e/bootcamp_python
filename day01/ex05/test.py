#!/usr/bin/env python3


from the_bank import Account, Bank


if __name__ == '__main__':

    pepe = Account('Pepe', zip=28032, value=0)
    papa = Account('Papa', addr="La mancha", value=0, b=3)
    pepe.value = 412
    del papa.value
    bankia = Bank()
    bankia.add(pepe)
    bankia.add(papa)
    bankia.fix_account(papa)
    bankia.transfer('Pepe', 'Papa', 400)
    print("Papa value after transfer:", papa.value)
