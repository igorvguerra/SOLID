class Programmer:
    def make(self):
        print("Programmer is creating code")

class Seller:
    def make(self):
        print("Seller is selling the product")

class HR:
    def make(self):
        print("HR is hiring new devs")

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

programmer = Programmer()
seller = Seller()
hr = HR()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(hr)
