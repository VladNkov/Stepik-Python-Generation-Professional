import csv

with open('data.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))
mail_dict = {}

mail_list = [row['email'] for row in data]
for i in mail_list:
    nick_name, domain = i.split('@')[0], i.split('@')[1]
    mail_dict.setdefault(domain, []).append(nick_name)

domain_count = {
    domain: len(nick_name) for domain, nick_name in mail_dict.items()
}
sorted_domain = sorted(domain_count.items(), key=lambda x: (x[1], x[0]))

columns = ['domain', 'count']

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as write_file:
    writer = csv.writer(write_file, delimiter=',')
    writer.writerow(columns)
    writer.writerows(sorted_domain)