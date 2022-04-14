import random
import os
import shutil

contacts = {}
x = int(input("Berapa banyak nomor yang Anda inginkan? "))
y = input("Berapa awalan nomor yang Anda inginkan? ")
z = int(input("Berapa banyak digit yang akan dirandom? "))

class Contact():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def generate_numbers(self):
        value = [0] * self.z
        number = set()
    
        for i in range(self.x):
            for j in range(self.z):
                value[j] = random.randint(0, 9)
            str_value = [str(i) for i in value]
            new_value = "".join(str_value)
            number.add(self.y + new_value)
        
        numbers = list(number)
        return numbers
    
    def generate_names(self):
        name = input("Masukan nama: ")
        for i in range(len(self.numbers)):
            contacts["{}{}".format(name, i + 1)] = self.numbers[i]
        print(contacts)
       
    def make_vcf(self):
        Q = input("Apakah Anda ingin save nomor ini? (Y/N) ")
        if Q.lower() == "y":
            make_dir = input("Masukan nama folder: ")
            if os.path.exists(make_dir):
                pass
            else:
                os.mkdir(make_dir)
            for i, j in contacts.items():
                with open(make_dir + "/" + i + ".vcf", "w") as f:
                    f.write("BEGIN:VCARD\n")
                    f.write("VERSION:3.0\n")
                    f.write("N:{}\n".format(i))
                    f.write("TEL;CELL:{}\n".format(j))
                    f.write("END:VCARD\n")
            print("File telah disave di folder " + make_dir)
        else: 
            exit()
      
    def main(self):
        self.numbers = self.generate_numbers()
        self.generate_names()
        self.make_vcf()
        
Contact(x, y, z).main()