from unittest import TestLoader, TestSuite, TextTestRunner
from WebAutomation.Test.Scripts.test_Create_new_course_and_edit_module import assignment3Search
from WebAutomation.Test.Scripts.test_enroll_subject_Shamrose import Elearning
#from WebAutomation.Test.Scripts.test_Edit_Course_Create_Account import blog_Elearning
from WebAutomation.Test.Scripts.test_Forgot_Password import Royalon
from WebAutomation.Test.Scripts.test_KDuong_Adding_Item_Cart import Item_Cart
from WebAutomation.Test.Scripts.test_KDuong_Coupon import Coupon
from WebAutomation.Test.Scripts.test_KDuong_Payment import KDuong_Payment
from WebAutomation.Test.Scripts.test_KDuong_Updating_Item_Cart import KDuong_Updating_Item_Cart
from WebAutomation.Test.Scripts.test_Login_Royalon import Login_Royalon
from WebAutomation.Test.Scripts.test_Remove_product_Shamrose import Remove_product_Shamrose


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite ((
        loader.loadTestsFromTestCase(assignment3Search),
        loader.loadTestsFromTestCase(Elearning),
#        loader.loadTestsFromTestCase(blog_Elearning),
        loader.loadTestsFromTestCase(Royalon),
        loader.loadTestsFromTestCase(Item_Cart),
        loader.loadTestsFromTestCase(Coupon),
        loader.loadTestsFromTestCase(KDuong_Payment),
        loader.loadTestsFromTestCase(KDuong_Updating_Item_Cart),
        loader.loadTestsFromTestCase(Login_Royalon),
        loader.loadTestsFromTestCase(Remove_product_Shamrose),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

