import os
import pickle
from .BitSrunCore.core import Core

class Cmd(object):

    def __init__(self):
        self._conf_file = os.environ['HOME']+'/.srun-py-config.pkl'

    def login(self):
        userinfo = self._load_config()
        if userinfo:
            Core.login(*userinfo)


    def logout(self):
        userinfo = self._load_config()
        if userinfo:
            username, _ =userinfo
            Core.logout(username)

    def info(self):
        Core.info()

    def config(self):
        username = input("输入校园网用户名:")
        password = input("输入校园网密码:")
        userinfo = (username,password)
        with open(self._conf_file, 'wb') as f:
            pickle.dump(userinfo, f)

    def _load_config(self):
        if os.path.isfile(self._conf_file):
            with open(self._conf_file, 'rb') as f:
                user_info = pickle.load(f)
            return user_info
        else:
            print("请先配置用户名密码")
            return None

cmd = Cmd()

if __name__ == '__main__':
    cmd.config()
    cmd._load_config()