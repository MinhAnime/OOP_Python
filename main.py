from manage_customer import ManageCustomer, CasualCustomer, LoyalCustomer


def main():
    manager = ManageCustomer()

    while True:
        print("\nQuản lý khách hàng")
        print("1. Thêm khách hàng")
        print("2. Chỉnh sửa hoặc khách hàng")
        print("3. Nâng cấp khách hàng")
        print("4. Xóa khách hàng")
        print("5. Tìm kiếm khách hàng")
        print("6. Danh sách khách hàng")
        print("7. Tổng doanh thu")
        print("8. Trung bình giá trị mua hàng")
        print("9. Top 3 khách hàng mua nhiều nhất")
        print("10. Top 10 khách hàng thân thiết")
        print("11. Thoát")

        choice = input("Nhập lựa chọn: ").strip()

        if choice == "1":
            id = input("Nhập mã khách hàng: ").strip()
            if next((c for c in manager.customers if c.id == id), None):
                print("Mã khách hàng đã tồn tại, vui lòng nhập mã khác.")
                continue
            name = input("Nhập tên: ").strip()
            phone = input("Nhập số điện thoại: ").strip()
            email = input("Nhập Email: ").strip()

            while True:
                print("\nChọn loại khách hàng:")
                print("1. Khách hàng thân thiết")
                print("2. Khách hàng vãng lai")
                print("3. Trở lại")

                type_choice = input("Nhập lựa chọn: ").strip()

                if type_choice == "1":
                    diemtichluy = int(input("Nhập điểm tích lũy: "))
                    tonggiatrimuahang = int(input("Nhập tổng giá trị mua hàng: "))
                    manager.add_customer(LoyalCustomer(id, name, phone, email, diemtichluy, tonggiatrimuahang))
                    break
                elif type_choice == "2":
                    solanmuahang = int(input("Nhập số lần mua hàng: "))
                    tonggiatrimuahang = int(input("Nhập tổng giá trị mua hàng: "))
                    manager.add_customer(CasualCustomer(id, name, phone, email, solanmuahang, tonggiatrimuahang))
                    break
                elif type_choice == "3":
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        elif choice == "2":
            id = input("Nhập mã khách hàng muốn chỉnh sửa: ").strip()
            name = input("Nhập tên mới (bỏ trống nếu không thay đổi): ").strip() or None
            phone = input("Nhập số điện thoại mới (bỏ trống nếu không thay đổi): ").strip() or None
            email = input("Nhập Email mới (bỏ trống nếu không thay đổi): ").strip() or None

            customer = next((c for c in manager.customers if c.id == id), None)
            if customer:
                if isinstance(customer, LoyalCustomer):
                    diemtichluy = input("Nhập điểm tích lũy mới (bỏ trống nếu không thay đổi): ").strip()
                    diemtichluy = int(diemtichluy) if diemtichluy else None
                    tonggiatrimuahang = input("Nhập tổng giá trị mua hàng mới (bỏ trống nếu không thay đổi): ").strip()
                    tonggiatrimuahang = int(tonggiatrimuahang) if tonggiatrimuahang else None
                    manager.edit_customer(id, name, phone, email, diemtichluy, None, tonggiatrimuahang)
                elif isinstance(customer, CasualCustomer):
                    solanmuahang = input("Nhập số lần mua hàng mới (bỏ trống nếu không thay đổi): ").strip()
                    solanmuahang = int(solanmuahang) if solanmuahang else None
                    tonggiatrimuahang = input("Nhập tổng giá trị mua hàng mới (bỏ trống nếu không thay đổi): ").strip()
                    tonggiatrimuahang = int(tonggiatrimuahang) if tonggiatrimuahang else None
                    manager.edit_customer(id, name, phone, email, None, solanmuahang, tonggiatrimuahang)
            else:
                print("Không tìm thấy khách hàng với mã đã nhập.")

        elif choice == "3":
            id = input("Nhập mã khách hàng muốn nâng cấp: ").strip()
            manager.upgrade_customer(id)

        elif choice == "4":
            id = input("Nhập mã khách hàng muốn xóa: ").strip()
            manager.delete_customer(id)

        elif choice == "5":
            keyword = input("Nhập từ khóa tìm kiếm: ").strip()
            results = manager.search_customer(keyword)
            for i in results:
                print(i)

        elif choice == "6":
            print("\nDanh sách khách hàng")
            print("1. Tất cả khách hàng")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")

            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
                customer = manager.list_customers()
                for i in customer:
                    print(i)
            elif luachon == "2":
                customer = manager.list_customers(CasualCustomer)
                for i in customer:
                    print(i)
            elif luachon == "3":
                customer = manager.list_customers(LoyalCustomer)
                for i in customer:
                    print(i)
        elif choice == "7":
            print("\nTổng doanh thu")
            print("1. Tất cả khách hàng")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")

            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
                print(f"Tổng doanh thu: {manager.tong_doanh_thu()}")
            elif luachon == "2":
                print(f"Tổng doanh thu: {manager.tong_doanh_thu(CasualCustomer)}")
            elif luachon == "3":
                print(f"Tổng doanh thu: {manager.tong_doanh_thu(LoyalCustomer)}")

        elif choice == "8":
            print("\nTrung bình giá trị mua hàng")
            print("1. Tất cả khách hàng")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")

            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
                print(f"Trung bình giá trị mua hàng: {manager.trung_binh_gia_tri_mua_hang()}")
            elif luachon == "2":
                print(f"Trung bình giá trị mua hàng: {manager.trung_binh_gia_tri_mua_hang(CasualCustomer)}")
            elif luachon == "3":
                print(f"Trung bình giá trị mua hàng: {manager.trung_binh_gia_tri_mua_hang(LoyalCustomer)}")

        elif choice == "9":
            print("\nTop 3 khách hàng mua nhiều nhất")
            customer = manager.top_3()
            for i in customer:
                print(i)

        elif choice == "10":
            print("\nTop 10 khách hàng thân thiết")
            customer = manager.top_10()
            for i in customer:
                print(i)

        else:
            print("Kết thúc chương trình")
            break

if __name__ == "__main__":
    main()
