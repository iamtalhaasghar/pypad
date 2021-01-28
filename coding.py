class Code(object):    

    def __init__(self):
        self.path = str()
        self.fileName = str()
        
    def runCmd(self):
        import os
        os.startfile('cmd')

    def compileCode(self):
        pass

    def runCode(self):
        pass
    
class TextFile(Code):
    
    def __init__(self, path):
        self.path = path
        import os
        self.fileName = os.path.split(path)[1]


class JavaFile(Code):
    
    def __init__(self, path):
        self.path = path
        import os
        self.fileName = os.path.split(path)[1]

    def compileCode(self):
        import subprocess
        c = subprocess.run('PowerShell start-process -wait javac %s -redirectstandarderror error.txt'
                           % self.fileName)
        f = open('error.txt')
        s = f.read()
        return s

    def runCode(self):
        
        import subprocess
        c = subprocess.run('PowerShell start-process java %s' %
                           self.fileName.split('.')[0])
            

