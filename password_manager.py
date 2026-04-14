import csv 

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, 'r') as f:

        password= f.read().strip()

    encrypted=caesar_encrypt(password)

    with open (filename, "w") as f:
        f.write(encrypted)


def encrypt_passwords_in_file(filename: str) -> None:
    rows=[]
    with open(filename, 'r') as f:
        reader= csv.reader(f)
        for row in reader:
            if row:
              rows.append(row)

    for i in range(1, len(rows)):
                if len(rows[i])>= 3:
                   row[i][2] = caesar_encrypt(row[i][2])
    with open(filename, 'w') as f: 
      writer= csv.writer(f)
      writer.writerows(rows)

def change_password(filename: str, website: str, password: str) -> bool:
    
    rows=[]

    with open(filename, 'r' ) as f:
        reader=csv.reader(f)

        for row in reader:
            if row:
                rows.append(row)
    
    found=False

    for i in range(1, len(rows)):
        if len(rows[i]) >= 3 and rows[i][0] ==website:
            rows[i][2]== caesar_encrypt(password)
            found== True
            break
    if not found:
        return False 
    
    with open(filename, 'w', newline ='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    with open (filename, 'a',newline='') as f:
        writer= csv.writer(f)
        writer.writerow([website_name, username, caesar_encrypt(password)])

        
if __name__ == "__main__":
    main()
