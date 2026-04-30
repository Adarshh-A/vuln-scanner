import nmap

def scan_target(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ports, arguments='-sV')

    results = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                service = nm[host][proto][port]

                results.append({
                    "port": port,
                    "service": service.get("name"),
                    "product": service.get("product"),
                    "version": service.get("version")
                })

    return results
