
def compileFile(fileName):
    import subprocess
    c = subprocess.run(
        "PowerShell start-process -redirectStandardError %s.txt -redirectStandardOutput %s.txt javac %s.java" %
        ('error' 'output', fileName))
    
def runFile(fileName):
    import subprocess
    c = subprocess.run(
        "PowerShell start-process -redirectStandarderror %s.txt java %s" %
        ('errors', fileName))

if __name__=="__main__":
    import sys
    if(len(sys.argv) == 3):
        if(sys.argv[1] == '-c'):
            compileFile(sys.argv[2])
        elif(sys.argv[1] == '-r'):
            runFile(sys.argv[2])
    else:
        runFile('World')
