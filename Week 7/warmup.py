
servers = ["Server1", "192.168.2.10", "db-server"]
ports = [20,21,22,23,25,53,67,68,69,80,110,111,\
         123,135,137,138,139,143,161,162,443,445,\
            500,514,520,631,993,995,1434,1723,1900,\
                3306,3389,4500,5900,8080,49152]
# write a script that loops through a list of servers
for server in servers:
# and loops through a range of common ports (80-84)
    for port in ports:
        #output to look like the following:
        # Scanning {server} on port x
        print("Scanning", server, "on port", port)
