#!/usr/bin/env python3


import paramiko
import re


def check_stat_vm(hv_ip, vm_id, hv_username):
    vm_name = ""
    vm_status = False
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hv_ip, username=hv_username)
    stdin, stdout, stderr = client.exec_command('qm list')
    out = bytes.decode(stdout.read(), encoding='utf-8')
    err = bytes.decode(stderr.read(), encoding='utf-8')
    if err != "":
        print(err)
        client.close()
        return vm_name, vm_status
    vm_data = re.search(r"( {} ).*".format(vm_id), out)
    if vm_data == None:
        print("There is no virtual machine with this id")
        vm_status = False
        return vm_name, vm_status
    vm_data = vm_data.group(0)
    vm_name = re.search(r"(?<=( {} ))\S*( )".format(vm_id), vm_data).group(0)
    vm_status = re.search(r"stopped", vm_data)
    if vm_status == None:
        print("The virtual machine is not in stopped status")
        vm_status = False
        client.close()
        return vm_name, vm_status
    vm_status = True
    client.close()
    return vm_name, vm_status