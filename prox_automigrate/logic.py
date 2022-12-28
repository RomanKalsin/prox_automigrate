#!/usr/bin/env python3


from prox_automigrate.arg_parser import cli
from prox_automigrate.check_stat_vm import check_stat_vm
from prox_automigrate.list_storage import list_storage
from prox_automigrate.config_send import config_send
from prox_automigrate.snap_create import snap_create
from prox_automigrate.snap_send import snap_send
from prox_automigrate.config_edit import config_edit


def main():
    options = cli()
    hv_ip, vm_id, hv_username, dest, new_vm_id = options.hv_ip, options.vm_id, options.user ,options.dest, options.idvm
    vm_name, vm_status = check_stat_vm("localhost", new_vm_id, hv_username)
    if vm_name != "NO-EXISTS":
        print("A VM with this ID exists on the target hypervisor")
        return 1
    vm_name, vm_status = check_stat_vm(hv_ip, vm_id, hv_username)
    if vm_status != True:
        print("There is no virtual machine for migrate with this id")
        return 1
    dataset_list = list_storage(hv_ip, vm_id, hv_username)
    f_dt = snap_create(hv_ip, dataset_list, hv_username)
    snap_send(hv_ip, dataset_list, vm_name, vm_id, new_vm_id, dest, f_dt, hv_username)
    config_send(hv_ip, vm_id, vm_name, new_vm_id, hv_username)
    config_edit(vm_id, new_vm_id)