#!/usr/bin/env python3


import subprocess
import re


# Отправка снапшотов
def snap_send(hv_ip, dataset_list, vm_name, vm_id, dest, f_dt, hv_username):
    for i in dataset_list:
        snap_name = '{}@am{}'.format(i, f_dt)
# Поумолчанию путь к датасету назначения равен пути датасету источника
        disk_path = i
# Если датасет назначения указан
        if dest != False:
            disk_name = re.split(r"/", i)[-1]
            disk_path = "{}/{}".format(dest, disk_name)
            print("Needed edit config file vm id:{} disk path:{} ".format(vm_id, disk_path))
        size_human = subprocess.run(["ssh", "{}@{}".format(hv_username, hv_ip), "zfs", "send", "{}".format(snap_name), "-nv"], stdout=subprocess.PIPE)
        size_human = bytes.decode(size_human.stdout, encoding='utf-8')
        size_human = re.search(r'(?<=(total estimated size is )).*', size_human).group(0)
        size_machine = subprocess.run(["ssh", "{}@{}".format(hv_username, hv_ip), "zfs", "send", "{}".format(snap_name), "-nP"], stdout=subprocess.PIPE)
        size_machine = bytes.decode(size_machine.stdout, encoding='utf-8')
        size_machine = re.search(r'(?<=(size)).*', size_machine).group(0)
        size_machine = re.search(r'\d+', size_machine).group(0)
        file = open('./{}.sh'.format(vm_name), 'w')
        file.write("#!/bin/bash\n")
        file.write("ssh {}@{} 'zfs send -R {} | lz4c -z' | lz4c -d | pv --size {} --name '{} {}' | zfs receive {}".format(hv_username, hv_ip, snap_name, size_machine, vm_name, size_human, disk_path))
        file.close()
        subprocess.run(['chmod', '+x', './{}.sh'.format(vm_name)])
        subprocess.run(['./{}.sh'.format(vm_name)])
        subprocess.run(['rm', './{}.sh'.format(vm_name)])