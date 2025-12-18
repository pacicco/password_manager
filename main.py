from cryptography.fernet import Fernet, InvalidToken

class Password_Manager:
    
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def set_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password(self, path):
        if self.key is None:
            raise ValueError("Key not loaded. Call create_key() or load_key() first.")
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    site, encrypted = line.split(':', 1)
                    try:
                        self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
                    except InvalidToken:
                        # corrupted or wrong-key entry — skip and warn
                        print(f"Warning: could not decrypt entry for {site}; skipping.")
        except FileNotFoundError:
            raise

    def add_password(self, site, password):
        self.password_dict[site] = password

        # Only write to file if a password file path and key are set
        if self.password_file is not None and self.key is not None:
            with open(self.password_file, 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ':' + encrypted.decode() + '\n')

    def get_password(self, site):
        return self.password_dict.get(site)
    
def main():
    password = {
            'email': 'email@gmail.com',
            'github': 'ghp_1234567890abcdef',
            'bank': 'P@ssw0rd!'
        }

    pm = Password_Manager()

    print("What do you want to do?\n"
        "(1) Create Key\n"
        "(2) Load Key\n"
        "(3) Set Password File\n"
        "(4) Load Passwords\n"
        "(5) Add Password\n"
        "(6) Get Password\n"
        "(7) Quit"
    )
        
    done = False
    
    while not done:

            choice = input("Enter choice: ")
            if choice == '1':
                path = input("Enter key file path: ")
                pm.create_key(path)
                print("Key created and saved to", path)
            elif choice == '2':
                path = input("Enter key file path: ")
                pm.load_key(path)
                print("Key loaded from", path)
            elif choice == '3':
                path = input("Enter password file path: ")
                pm.set_password_file(path, password)
                print("Password file set to", path)
            elif choice == '4':
                path = input("Enter password file path: ")
                if pm.key is None:
                    print("No key loaded. Please load a key (option 2) before loading passwords.")
                else:
                    try:
                        pm.load_password(path)
                        print("Passwords loaded from", path)
                    except Exception as e:
                        print("Failed to load passwords:", e)
            elif choice == '5':
                site = input("Enter site name: ")
                password = input("Enter password: ")
                pm.add_password(site, password)
                print("Password added for", site)
            elif choice == '6':
                # Show available sites (prefer passwords already loaded into manager)
                sites = list(pm.password_dict.keys()) if pm.password_dict else list(password.keys())
                if not sites:
                    print("No sites available.")
                else:
                    print("Available sites:")
                    for i, s in enumerate(sites, start=1):
                        print("({}) {}".format(i, s))
                    sel = input("Enter site number or name: ").strip()
                    if sel.isdigit() and 1 <= int(sel) <= len(sites):
                        site = sites[int(sel) - 1]
                    else:
                        site = sel
                    pwd = pm.get_password(site)
                    # Fallback to the local `password` dict defined in main if manager doesn't have it
                    if pwd is None and site in password:
                        pwd = password[site]

                    if pwd is None:
                        print("No password found for", site)
                    else:
                        print("Password for {} is {}".format(site, pwd))
                
            elif choice == '7':
                done = True
                print("bye!")                       
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

