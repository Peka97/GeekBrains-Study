def detect_spammer(lst):
    spammer_dict = {'addr': 'val', 'count': 0}
    unique_addr = set(lst)
    for addr in unique_addr:
        if lst.count(addr) > spammer_dict['count']:
            spammer_dict['addr'] = addr
            spammer_dict['count'] = lst.count(addr)
    print(spammer_dict)


with open("nginx_logs.txt", "r", encoding='utf-8') as file:
    full_remote_addr = []
    for line in file:
        remote_addr = line.split()[0]
        request_type = line.split()[5].strip('"')
        requested_resource = line.split()[6]
        # print(tuple([remote_addr, request_type, requested_resource]))
        full_remote_addr += [remote_addr]
    detect_spammer(full_remote_addr)
