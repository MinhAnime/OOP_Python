from customer import LoyalCustomer, CasualCustomer


class ManageCustomer:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        if any(c.id == customer.id for c in self.customers):
            raise ValueError(f"Mã khách hàng {customer.id} đã tồn tại")
        self.customers.append(customer)
        print(f"Thêm khách hàng {customer.name} (ID {customer.id}) thành công")

    def edit_customer(self, id, name=None, phone=None, email=None, diemtichluy=None, solanmuahang=None, tonggiatrimuahang=None):
        for i, customer in enumerate(self.customers):
            if customer.id == id:
                print(f"Chỉnh sửa thông tin khách hàng: {customer}")
                customer.name = name if name else customer.name
                customer.phone = phone if phone else customer.phone
                customer.email = email if email else customer.email

                if isinstance(customer, LoyalCustomer):
                    customer.diemtichluy = diemtichluy if diemtichluy is not None else customer.diemtichluy
                    customer.tonggiatrimuahang = tonggiatrimuahang if tonggiatrimuahang is not None else customer.tonggiatrimuahang
                    print(f"Thông tin khách hàng đã được cập nhật: {customer}")
                elif isinstance(customer, CasualCustomer):
                    customer.solanmuahang = solanmuahang if solanmuahang is not None else customer.solanmuahang
                    customer.tonggiatrimuahang = tonggiatrimuahang if tonggiatrimuahang is not None else customer.tonggiatrimuahang
                    print(f"Thông tin khách hàng đã được cập nhật: {customer}")
                    break
        else:
            raise ValueError(f"Không tìm thấy khách hàng có ID {id}")

    def upgrade_customer(self, id):
        for customer in self.customers:
            if customer.id == id and isinstance(customer, CasualCustomer):
                if customer.tonggiatrimuahang > 2000000:
                    self.customers.remove(customer)
                    self.customers.append(
                        LoyalCustomer(customer.id, customer.name, customer.phone, customer.email, diemtichluy=0,
                                      tonggiatrimuahang=customer.tonggiatrimuahang))
                    print(f"Khách hàng {customer.name} (ID {customer.id}) đã nâng cấp thành công")
                    return
        else:
            raise ValueError(f"Không tìm thấy khách hàng có ID {id} hoặc khách hàng đã là khách hàng thân thiết")

    def delete_customer(self, id):
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)
                print(f"Khách hàng {customer.name} (ID {customer.id}) đã xóa thành công")
                return
        else:
            raise ValueError(f"Không tìm thấy khách hàng có ID {id}")

    def search_customer(self, keyword):
        ket_qua = [
            i for i in self.customers
            if keyword in i.id or keyword in i.name or keyword in i.phone
        ]
        if not ket_qua:
            print("Không tìm thấy khách hàng phù hợp.")
        return ket_qua

    def list_customers(self, loai_khach_hang=None):
        if loai_khach_hang is None:
            return self.customers
        return [i for i in self.customers if isinstance(i, loai_khach_hang)]

    def tong_doanh_thu(self, loai_khach_hang=None):
        danh_sach = self.list_customers(loai_khach_hang)
        return sum(i.tonggiatrimuahang for i in danh_sach) if danh_sach else 0

    def trung_binh_gia_tri_mua_hang(self, loai_khach_hang=None):
        danh_sach = self.list_customers(loai_khach_hang)
        return sum(i.tonggiatrimuahang for i in danh_sach) / len(danh_sach) if danh_sach else 0

    def top_3(self):
        return sorted(self.customers, key=lambda i: i.tonggiatrimuahang, reverse=True)[:3]

    def top_10(self):
        khach_hang_than_thiet = [i for i in self.customers if isinstance(i, LoyalCustomer) and i.diemtichluy > 500]
        return sorted(khach_hang_than_thiet, key=lambda i: i.diemtichluy, reverse=True)[:10]
