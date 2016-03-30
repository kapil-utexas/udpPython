from subprocess import call
import subprocess
import sys

mycmd="socat"
myarg=" - UDP-DATAGRAM:10.145.127.21:11111,broadcast,sp=s11111"
cmd2 = "python -m sbp.client.examples.simple"
#for num in range(0,100):
echo = subprocess.Popen((cmd2).split(), stdout=subprocess.PIPE)		
    #echo = subprocess.Popen(('echo linux_'+str(num)).split(), stdout=subprocess.PIPE)
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
