from winreg import *
e = SetValue(HKEY_CLASSES_ROOT,r'Directory\Background\shell\Start CodePad\command',
             REG_SZ,r'F:\Programming\5. Python\CodePad\dist\codePad\codePad.exe')

