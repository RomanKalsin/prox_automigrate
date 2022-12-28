#!/usr/bin/env python3


import subprocess


# Отправка конфига
def config_send(hv_ip, vm_id, vm_name, new_vm_id, hv_username):
    if new_vm_id == False:
        new_vm_id = vm_id
    status = subprocess.run(["scp", "{}@{}:/etc/pve/qemu-server/{}.conf".format(hv_username, hv_ip, vm_id), "/etc/pve/qemu-server/{}.conf".format(new_vm_id)], stdout=subprocess.PIPE)
    if status.returncode != 0:
        print("Config vm {} {} not send".format(new_vm_id, vm_name))
    print("Config vm {} {} sended".format(new_vm_id, vm_name))