class House :

    def __init__(self,hous_no,hous_name):
        self.hous_no = hous_no
        self.hous_name = hous_name
    def show(self):
        print(f"{self.hous_name},{self.hous_no}")

house1=House(34,"amitya")

house1.show()

