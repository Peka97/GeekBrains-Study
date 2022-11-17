with open("nginx_logs.txt", "r", encoding='utf-8') as file:
    full_remote_addr = []
    for line in file:
        remote_addr = line.split()[0]
        request_type = line.split()[5].strip('"')
        requested_resource = line.split()[6]
        print(tuple([remote_addr, request_type, requested_resource]))
