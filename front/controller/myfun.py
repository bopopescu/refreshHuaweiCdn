from front.models import Cloud
import platform
from subprocess import  PIPE, Popen

def get_clound_type(domain):
    cloud = Cloud.objects.exclude(name="未知云").all()
    rule_dict = {}
    for v in cloud:
        rule_dict[v.name] = v.domain_rule.strip().split(",")
    print(rule_dict)
    if platform.system() == "Linux":
        p = Popen("host {}".format(domain), stdout=PIPE, stderr=PIPE, shell=True)
        out = p.stdout.read().decode("utf-8")
        cname = out.strip().split("\n")[0].split()[-1]
    elif platform.system()== "Windows":
        p = Popen("nslookup {}".format(domain), stdout=PIPE, stderr=PIPE, shell=True)
        out = p.stdout.read().decode("utf-8")
        cname = out.strip().split()[-1]
    for i in rule_dict.items():
        for rule in i[1]:
            print("-"*30)
            print(rule)
            print("-" * 30)
            if platform.system() == "Linux":
                domain_rule = domain + rule.replace("domain", "") + "."
            elif platform.system() == "Windows":
                domain_rule = domain + rule.replace("domain", "")
            print(domain_rule)
            if domain_rule == cname:
                return i[0]
    return "未知云"