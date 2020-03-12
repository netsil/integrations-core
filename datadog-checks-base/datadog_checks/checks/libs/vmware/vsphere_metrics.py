'''
Created on 11-Mar-2020

@author: atish.bhowmick
'''

CPU_METRICS = {
    'cpu.ready': {
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    'cpu.usage': {
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
}
MEM_METRICS = {
    'mem.usage': {
        's_type': 'absolute',
        'unit': 'percent',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Active
    'mem.active': {
        's_type': 'absolute',
        'unit': 'kiloBytes',
        'rollup': 'average',
        'entity': ['VirtualMachine']
    },
    # Balloon
    'mem.vmmemctl': {
        's_type': 'absolute',
        'unit': 'kiloBytes',
        'rollup': 'average',
        'entity': ['VirtualMachine']
    },
    # Consumed
    'mem.consumed': {
        's_type': 'absolute',
        'unit': 'kiloBytes',
        'rollup': 'average',
        'entity': ['VirtualMachine']
    },
    # Shared
    'mem.shared': {
        's_type': 'absolute',
        'unit': 'kiloBytes',
        'rollup': 'average',
        'entity': ['VirtualMachine']
    },
    # Swapped
    'mem.swapped': {
        's_type': 'absolute',
        'unit': 'kiloBytes',
        'rollup': 'average',
        'entity': ['VirtualMachine']
    },
}
DATASTORE_METRICS = {
    # Average read requests per second
    'datastore.numberReadAveraged': {
        's_type': 'rate',
        'unit': 'number',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Average write requests per second
    'datastore.numberWriteAveraged': {
        's_type': 'rate',
        'unit': 'number',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Read rate
    'datastore.read': {
        's_type': 'rate',
        'unit': 'kiloBytesPerSecond',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    #Write rate
    'datastore.write': {
        's_type': 'rate',
        'unit': 'kiloBytesPerSecond',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
}
DISK_METRICS = {
    # Usage
    'disk.usage': {
        's_type': 'rate',
        'unit': 'kiloBytesPerSecond',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Read requests
    'disk.numberRead': {
        's_type': 'delta',
        'unit': 'number',
        'rollup': 'summation',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Average read requests per second
    'disk.numberReadAveraged': {
        's_type': 'rate',
        'unit': 'number',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Write requests
    'disk.numberWrite': {
        's_type': 'delta',
        'unit': 'number',
        'rollup': 'summation',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Average write requests per second
    'disk.numberWriteAveraged': {
        's_type': 'rate',
        'unit': 'number',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Read rate
    'disk.read': {
        's_type': 'rate',
        'unit': 'kiloBytesPerSecond',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
    # Write rate
    'disk.write': {
        's_type': 'rate',
        'unit': 'kiloBytesPerSecond',
        'rollup': 'average',
        'entity': ['VirtualMachine', 'HostSystem']
    },
}