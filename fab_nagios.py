#/bin/env python        
#-*- coding:utf-8 -*-

from fabric.api import *
from fabric.contrib.console import confirm
from config import service

src_dir="/Users/gmsjy/nagios/"
nagi_dir="/opt/nagios/nagios"

env.user='nagios'
env.hosts=['114.215.184.138:10022','115.29.188.140:10022','115.29.194.125:10022']
env.password='mt5u#L9x'
#env.roledefs = {
#   'monitors':[]
#   'servers':[]
#}

@task
def nrpe_start():
    run("%s/bin/nrpe -c %s/etc/nrpe.cfg -d" % (nagi_dir,nagi_dir))
    
@task
def nrpe_stop():
    run("kill `pgrep nrpe`")
    
@task
def nrpe_restart():
    nrpe_stop()
    nrpe_start()
    
def writeService(serDict):
    """trans dict to string"""
    bufStr = "define service{\n"+\
    "host name "+serDict['host_name']+"\n"\
    "service_description "+serDict['service_description']+"\n"\
    "check_command "+serDict['check_command']+"\n"\
    "check_period "+serDict['check_period']+"\n"\
    "max_check_attempts "+serDict['max_check_attempts']+"\n"\
    "normal_check_interval "+serDict['normal_check_interval']+"\n"\
    "retry_check_interval "+serDict['retry_check_interval']+"\n"\
    "contact_groups "+serDict['contact_groups']+"\n"\
    "notification_interval "+serDict['notification_interval']+"\n"\
    "notification_period "+serDict['notification_period']+"\n"\
    "notification_options "+serDict['notification_options']+"\n"\
    "}"+"\n\n"
    return bufStr



def add_server(newServer,newCommand):
    """add servers to file"""
    with open('./config/servers', 'a') as f:
        f.write(newServer)
    with open('./config/nrpe.cfg','a') as f:
        f.write(newCommand)
    

if __name__ == "__main__":
    serString = writeService(service)
    serCommand = "command check /opt/nagios"
    print(serString)
    add_server(serString,serCommand)
