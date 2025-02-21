from manage_customer import ManageCustomer, CasualCustomer, LoyalCustomer


def main():
    manager = ManageCustomer()

    while True:
        print("\nQuản lý khách hàng")
        print("1. Thêm khách hàng")
        print("2. Chỉnh sửa hoặc cập nhật khách hàng")
        print("3. Xóa khách hàng")
        print("4. Tìm kiếm khách hàng")
        print("5. Danh sách khách hàng")
        print("6. Tổng doanh thu")
        print("7. Trung bình giá trị mua hàng")
        print("8. Top 3 khách hàng mua nhiều nhất")
        print("9. Top 10 khách hàng thân thiết")
        print("10. Thoát")

        choice = input("Nhập lựa chọn: ").strip()

        if choice == "1":
            id = input("Nhập mã khách hàng: ").strip()
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
            id = input("Nhập mã khách hàng muốn sửa: ").strip()
            name = input("Tên mới (bỏ trống nếu không đổi): ").strip()
            phone = input("Số điện thoại mới (bỏ trống nếu không đổi): ").strip()
            email = input("Email mới (bỏ trống nếu không đổi): ").strip()
            while True:
                print("1. Khách vãng lai")
                print("2. Khách thân thiết")
                print("3. Trở lại")
                luachontrong2 = input("\nNhập lựa chọn:")
                if luachontrong2 == "1":
                    solanmuahang = int(input("Nhập số lần mua hàng muốn sửa: "))
                    tonggiatrimuahang = int(input("Nhập tổng giá trị mua hàng muốn sửa:"))
                    manager.edit_customer(CasualCustomer(id, name, phone, email, solanmuahang, tonggiatrimuahang))
                    break
                elif luachontrong2 == "2":
                    diemtichluy = int(input("Nhập điểm tích lũy muốn sửa: "))
                    tonggiatrimuahang = int(input("Nhập tôgnr giá trị mua hàng muốn sửa: "))
                    manager.edit_customer(LoyalCustomer(id, name, phone, email, diemtichluy, tonggiatrimuahang))
                    break
                elif luachontrong2 == "3":
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        elif choice == "3":
            id = input("Nhập mã khách hàng muốn xóa: ").strip()
            manager.delete_customer(id)

        elif choice == "4":
            keyword = input("Nhập mã khách hàng, tên hoặc số điện thoại để tìm kiếm: ").strip()
            manager.search_customer(keyword)

        elif choice == "5":
            print("\nDanh sách khách hàng")
            print("1. Tất cả khách hàng")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")
            customers = []
            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
               customers = manager.list_customers()
            elif luachon == "2":
               customers = manager.list_customers(CasualCustomer)
            elif luachon == "3":
               customers = manager.list_customers(LoyalCustomer)
            elif luachon == "4":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            if customers:
                print("\nDanh sách khách hàng:")
                for customer in customers:
                    print(customer)
            else:
                print("\nKhông có khách hàng nào!")

        elif choice == "6":
            print("\nTổng doanh thu")
            print("1. Toàn bộ")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")

            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
                manager.tong_doanh_thu()
            elif luachon == "2":
                manager.tong_doanh_thu(CasualCustomer)
            elif luachon == "3":
                manager.tong_doanh_thu(LoyalCustomer)

        elif choice == "7":
            print("\nTrung bình giá trị mua hàng")
            print("1. Tất cả khách hàng")
            print("2. Khách hàng vãng lai")
            print("3. Khách hàng thân thiết")
            print("4. Trở lại")

            luachon = input("Nhập lựa chọn: ").strip()
            if luachon == "1":
                manager.trung_binh_gia_tri_mua_hang()
            elif luachon == "2":
                manager.trung_binh_gia_tri_mua_hang(CasualCustomer)
            elif luachon == "3":
                manager.trung_binh_gia_tri_mua_hang(LoyalCustomer)

        elif choice == "8":
            print("\nTop 3 khách hàng mua nhiều nhất")
            manager.top_3()

        elif choice == "9":
            print("\nTop 10 khách hàng thân thiết")
            manager.top_10()

        elif choice == "10":
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
