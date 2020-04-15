# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darodrig <darodrig@42madrid.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/15 22:12:50 by darodrig          #+#    #+#              #
#    Updated: 2020/04/15 22:12:50 by darodrig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import functools
from string import capwords
import getpass
import datetime

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        exectime = time.time() - start
        if int(exectime) > 0:
            units = "s"
        else:
            exectime = exectime * 1000
            units = "ms"
        f = open("machine.log", "a")
        f.write("({})Running: {}    [ exec-time = {} {} ]\n".format(
            getpass.getuser(),
            capwords(func.__name__.replace('_', ' ')),
            round(exectime, 3),
            units))
        f.close()
        return ret
    return wrapper
