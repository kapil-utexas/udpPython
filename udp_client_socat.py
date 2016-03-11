from subprocess import call
import subprocess
import sys

mycmd="socat"
myarg=" - UDP-DATAGRAM:10.145.70.36:11111,broadcast,sp=s11111"

for num in range(0,10):
    echo = subprocess.Popen(('echo linux_'+str(num)).split(), stdout=subprocess.PIPE)
    socat = subprocess.Popen((mycmd+myarg).split(), stdin=echo.stdout,stdout=subprocess.PIPE)
    echo.stdout.close()
    output = socat.communicate()[0]
    echo.wait()

#call(mycmd + myarg,shell = True)

#for num in range(0, 100):
#    print(num)
#subprocess.call(["ls", "-l"])
#    try:
#        retcode = call(mycmd + myarg + strx), shell = True)
#        if retcode < 0:
#            print >>sys.stderr, "Child was terminated by signal", -retcode
#        else:i
#            print >>sys.stderr, "Child returned", retcode
#    except OSError as e:
#        print >>sys.stderr, "Execution Failed!!!", e
