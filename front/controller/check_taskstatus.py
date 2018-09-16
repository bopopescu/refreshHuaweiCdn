from subprocess import PIPE,Popen
import sys
import os
sys.path.append('/data/apache/www/huaweicloud/refreshHuaweiCdn')
os.environ['DJANGO_SETTINGS_MODULE'] = 'refreshHuaweiCdn.settings'
import django
django.setup()
from front.models import FreshLog,FreshStatus
import time


def check_status():
	success_status = FreshStatus.objects.filter(name="刷新成功").first()
	failed_status = FreshStatus.objects.filter(name="刷新失败").first()
	log = FreshLog.objects.filter(state=2).all()
	for v in log:
		task_id = v.task_id
		print(task_id)
		p = Popen("python2.7 /data/apache/www/huaweicloud/refreshHuaweiCdn/front/controller/pythonsdk_projects/query_cdn.py {}".format(task_id), stdout=PIPE, stderr=PIPE, shell=True)
		out = p.stdout.read().decode("utf-8")
		print(out.split())
		out_list = out.split()
		processing_num = out_list[0]
		failed_num = out_list[1]
		succeed_num = out_list[2]
		create_time = out_list[3]
		if int(succeed_num) == 1:
			v.state=success_status
			v.save()
		elif int(failed_num) == 1:
			v.state=failed_status
			v.save()
		elif int(time.time()) - int(create_time) > 60*10:
			v.state=failed_status
			v.save()
			
		

if __name__ == "__main__":
	check_status()
