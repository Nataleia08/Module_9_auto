import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline='') as fh:
        f_name = ["name", "email", "phone", "favorite"]
        s_wr = csv.DictWriter(fh, f_name)
        s_wr.writeheader()
        for i in contacts:
            s_wr.writerow(i)


def read_contacts_from_file(filename):
    with open(filename, "r", newline='') as fh:
        read = csv.DictReader(fh)
        print(read)
        new_contacts = []
        for row in read:
            contact = row
            if contact["favorite"] == 'False':
                contact["favorite"] = False
            else:
                contact["favorite"] = True
            new_contacts.append(contact)
        print(new_contacts)
        return new_contacts


write_contacts_to_file('eggs.csv', [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}])
read_contacts_from_file('eggs.csv')
