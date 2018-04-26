class Student(object):
    """description of class"""
    name = "Praktikan DKP"
    id = "211201171X00XX"
    address = "GKB"
    gpa = 0.0

    def __init__(self): #default constructor
        print("Mahasiswa telah dibuat")
    
    def __init__ (self, name, id, address): #constructor berparameter
        print("Mahasiswa Telah dibuat")
        self.name = name
        self.id = id
        self.address = address

    def intro(self): #method
        print("Nama saya: " + self.name + " / NIM saya: " + self.id)

    def tellGPA(self, gpa): #method
     if gpa >= 3.0:
        print("IPK saya: " + str(gpa))
     else:
        print("IPK saya tidak boleh diberitahu orang lain")

    def tellAddress(self): #method
        print("Alamat saya di" + self.address)


