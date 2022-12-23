#!/usr/bin/env python3


from prox_automigrate.arg_parser import cli
from prox_automigrate.check_source import check_stat_vm
from prox_automigrate.list_storage import list_storage
from prox_automigrate.config_send import config_send
from prox_automigrate.snap_create import snap_create
from prox_automigrate.snap_send import snap_send


def main():
    options = cli()
    hv_ip, vm_id, hv_username, dest = options.hv_ip, options.vm_id, options.user ,options.dest
    vm_name, vm_status = check_stat_vm(hv_ip, vm_id, hv_username)
    if vm_status != True:
        return 1
    dataset_list = list_storage(hv_ip, vm_id, hv_username)
    f_dt = snap_create(hv_ip, dataset_list, hv_username)
    snap_send(hv_ip, dataset_list, vm_name, vm_id, dest, f_dt, hv_username)
    config_send(hv_ip, vm_id, vm_name, hv_username)