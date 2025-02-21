class Customer():
    def __init__(self,id,name,phone,email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"Mã khách hàng: {self.id}, Tên: {self.name}, Số điện thoại: {self.phone}, Email: {self.email} "

class LoyalCustomer(Customer):
    def __init__(self, id, name, phone, email, diemtichluy = 0, tonggiatrimuahang = 0):
        super().__init__(id, name, phone, email)
        self.diemtichluy = diemtichluy
        self.tonggiatrimuahang = tonggiatrimuahang
    def __str__(self):
        return super().__str__() + f"Điểm tích lũy: {self.diemtichluy}, Tổng giá trị mua hàng: {self.tonggiatrimuahang} "

class CasualCustomer(Customer):
    def __init__(self, id, name, phone, email, solanmuahang = 0, tonggiatrimuahang = 0):
        super().__init__(id, name, phone, email)
        self.solanmuahang = solanmuahang
        self.tonggiatrimuahang = tonggiatrimuahang
    def __str__(self):
        return super().__str__() + f"Số lần mua hàng: {self.solanmuahang}, Tổng giá trị mua : {self.tonggiatrimuahang} "
