
# -*- coding:UTF-8 -*-
#设置nagios监控命令方式

script_dir = ""

service = {'host_name' : '192.168.6.6-nagios server',
'service_description' : 'check-host-alive',
'check_command' : 'check-host-alive',
'check_period' : '24x7',
'max_check_attempts' : '1',
'normal_check_interval': '1',
'retry_check_interval' : '1',
'contact_groups' : 'admins',
'notification_interval' : '10',
'notification_period' : '24x7',
'notification_options' : 'w,u,c,r'
}

command = {'command' : '/opt/nagios/nagios/'}