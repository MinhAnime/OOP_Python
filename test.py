import unittest
from manage_customer import ManageCustomer, CasualCustomer, LoyalCustomer

class TestManageCustomer(unittest.TestCase):

    def setUp(self):
        self.manager = ManageCustomer()
        self.loyal_customer = LoyalCustomer("1", "Alice", "123456789", "alice@example.com", 100, 5000)
        self.casual_customer = CasualCustomer("2", "Bob", "987654321", "bob@example.com", 5, 1500)
        self.manager.add_customer(self.loyal_customer)
        self.manager.add_customer(self.casual_customer)

    def test_add_loyal_customer(self):
        customer = LoyalCustomer("3", "Charlie", "111111111", "charlie@example.com", 200, 7000)
        self.manager.add_customer(customer)
        self.assertIn(customer, self.manager.customers)

    def test_add_casual_customer(self):
        customer = CasualCustomer("4", "David", "222222222", "david@example.com", 10, 3000)
        self.manager.add_customer(customer)
        self.assertIn(customer, self.manager.customers)

    def test_edit_loyal_customer(self):
        self.manager.edit_customer(id="1", name="Alice Smith", phone="111111111", email="alice.smith@example.com", diemtichluy=200, tonggiatrimuahang=6000)
        customer = self.manager.customers[0]
        self.assertEqual(customer.name, "Alice Smith")
        self.assertEqual(customer.phone, "111111111")
        self.assertEqual(customer.email, "alice.smith@example.com")
        self.assertEqual(customer.diemtichluy, 200)
        self.assertEqual(customer.tonggiatrimuahang, 6000)

    def test_edit_casual_customer(self):
        self.manager.edit_customer(id="2", name="Bob Johnson", phone="222222222", email="bob.johnson@example.com", solanmuahang=10, tonggiatrimuahang=2500)
        customer = self.manager.customers[1]
        self.assertEqual(customer.name, "Bob Johnson")
        self.assertEqual(customer.phone, "222222222")
        self.assertEqual(customer.email, "bob.johnson@example.com")
        self.assertEqual(customer.solanmuahang, 10)
        self.assertEqual(customer.tonggiatrimuahang, 2500)

    def test_upgrade_casual_to_loyal(self):
        self.manager.edit_customer(id="2", tonggiatrimuahang=3000000)
        customer = self.manager.customers[1]
        self.assertIsInstance(customer, LoyalCustomer)
        self.assertEqual(customer.id, "2")
        self.assertEqual(customer.name, "Bob")
        self.assertEqual(customer.phone, "987654321")
        self.assertEqual(customer.email, "bob@example.com")
        self.assertEqual(customer.diemtichluy, 0)
        self.assertEqual(customer.tonggiatrimuahang, 3000000)

    def test_delete_customer(self):
        self.manager.delete_customer(id="1")
        self.assertNotIn(self.loyal_customer, self.manager.customers)

    def test_search_customer_by_id(self):
        results = self.manager.search_customer("1")
        self.assertIn(self.loyal_customer, results)

    def test_search_customer_by_name(self):
        results = self.manager.search_customer("Alice")
        self.assertIn(self.loyal_customer, results)

    def test_search_customer_by_phone(self):
        results = self.manager.search_customer("123456789")
        self.assertIn(self.loyal_customer, results)

    def test_list_all_customers(self):
        customers = self.manager.list_customers()
        self.assertIn(self.loyal_customer, customers)
        self.assertIn(self.casual_customer, customers)

    def test_list_loyal_customers(self):
        customers = self.manager.list_customers(LoyalCustomer)
        self.assertIn(self.loyal_customer, customers)
        self.assertNotIn(self.casual_customer, customers)

    def test_list_casual_customers(self):
        customers = self.manager.list_customers(CasualCustomer)
        self.assertIn(self.casual_customer, customers)
        self.assertNotIn(self.loyal_customer, customers)

    def test_total_revenue_all_customers(self):
        total_revenue = self.manager.tong_doanh_thu()
        self.assertEqual(total_revenue, 6500)

    def test_total_revenue_loyal_customers(self):
        total_revenue = self.manager.tong_doanh_thu(LoyalCustomer)
        self.assertEqual(total_revenue, 5000)

    def test_total_revenue_casual_customers(self):
        total_revenue = self.manager.tong_doanh_thu(CasualCustomer)
        self.assertEqual(total_revenue, 1500)

    def test_average_purchase_value_all_customers(self):
        average_value = self.manager.trung_binh_gia_tri_mua_hang()
        self.assertEqual(average_value, 3250)

    def test_average_purchase_value_loyal_customers(self):
        average_value = self.manager.trung_binh_gia_tri_mua_hang(LoyalCustomer)
        self.assertEqual(average_value, 5000)

    def test_average_purchase_value_casual_customers(self):
        average_value = self.manager.trung_binh_gia_tri_mua_hang(CasualCustomer)
        self.assertEqual(average_value, 1500)

    def test_top_3_customers(self):
        top_customers = self.manager.top_3()
        self.assertIn(self.loyal_customer, top_customers)
        self.assertIn(self.casual_customer, top_customers)


    def test_add_duplicate_customer_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_customer(LoyalCustomer("1", "Duplicate", "000000000", "duplicate@example.com", 0, 0))

    def test_edit_nonexistent_customer(self):
        with self.assertRaises(ValueError):
            self.manager.edit_customer(id="999", name="Nonexistent")

    def test_delete_nonexistent_customer(self):
        with self.assertRaises(ValueError):
            self.manager.delete_customer(id="999")

    def test_upgrade_nonexistent_customer(self):
        with self.assertRaises(ValueError):
            self.manager.upgrade_customer(id="999")

    def test_search_nonexistent_customer(self):
        results = self.manager.search_customer("Nonexistent")
        self.assertEqual(len(results), 0)

    def test_list_customers_empty(self):
        empty_manager = ManageCustomer()
        customers = empty_manager.list_customers()
        self.assertEqual(len(customers), 0)

    def test_total_revenue_empty(self):
        empty_manager = ManageCustomer()
        total_revenue = empty_manager.tong_doanh_thu()
        self.assertEqual(total_revenue, 0)

    def test_average_purchase_value_empty(self):
        empty_manager = ManageCustomer()
        average_value = empty_manager.trung_binh_gia_tri_mua_hang()
        self.assertEqual(average_value, 0)

    def test_top_3_customers_empty(self):
        empty_manager = ManageCustomer()
        top_customers = empty_manager.top_3()
        self.assertEqual(len(top_customers), 0)

    def test_top_10_loyal_customers_empty(self):
        empty_manager = ManageCustomer()
        top_customers = empty_manager.top_10()
        self.assertEqual(len(top_customers), 0)

if __name__ == "__main__":
    unittest.main()