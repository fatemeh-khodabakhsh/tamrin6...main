n = int(input())
domains = set()
for _ in range(n):
    email = input()
    if "@" in email:
        username,domain = email.split("@",1)
        domains.add(domain)
sorted_domains = sorted(domains)
for domain in sorted_domains:
    print(domain)
