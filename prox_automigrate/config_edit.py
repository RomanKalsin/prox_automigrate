#!/usr/bin/env python3


def config_edit(vm_id, new_vm_id):
    if new_vm_id != False:
        with open ("/etc/pve/qemu-server/{}.conf".format(new_vm_id), "r") as f:
            data = f.read()
        new_data = data.replace("vm-{}-disk-".format(vm_id), "vm-{}-disk-".format(new_vm_id))
        with open ("/etc/pve/qemu-server/{}.conf".format(new_vm_id), "w") as f:
            print(new_data)
            f.write(new_data)