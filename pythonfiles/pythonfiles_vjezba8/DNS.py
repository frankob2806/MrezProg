import dns.resolver

example = "www.aspira.hr"


def get_records(domain):
    ids = [
        'A',
        'PTR',
        'MX',
    ]

    for a in ids:
        try:
            answers = dns.revolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())

        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_records(example)

#py desktop/pythonfiles/pythonfiles_vjezba8/