from dingdinghelper import DingDingHelper
import requests
import ctypes
from multiprocessing import Process, freeze_support

def Mbox(title, text, style):
  return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def f():
  ding = DingDingHelper()
  ding.renew_cookie()
  r = requests.post("http://xxx/api/_/dingding/setCookie", json={ "cookie": ding.cookie })
  if r.status_code == 200:
    Mbox('提示', '上传成功！', 0)
  else:
    Mbox('提示', '上传失败！', 0)

if __name__ == "__main__":
  freeze_support()
  Process(target=f).start()