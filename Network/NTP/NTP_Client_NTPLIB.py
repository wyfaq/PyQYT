#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

import ntplib
from time import ctime
import sys

def ntp_client(NTP_SERVER):
	c = ntplib.NTPClient()
	response = c.request(NTP_SERVER, version=3)
	print(response)
	print('\t' + ctime(response.tx_time))
if __name__ == '__main__':
	ntp_server = sys.argv[1]
	ntp_client(ntp_server)
	#'0.uk.pool.ntp.org'





