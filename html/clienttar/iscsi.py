
import commands
commands.getoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.98 --discover')
commands.getoutput('iscsiadm --mode node --targetname navjot --portal 192.168.43.98:3260 --login')