
servers = ["Server1", "192.168.2.10", "db-server"]

# write a script that loops through a list of servers
for server in servers:
# and loops through a range of common ports (80-84)
    for port in range(80, 85):
        print(f"Scanning {server} on port {port}")

#output to look like the following:
# Scanning {server} on port x