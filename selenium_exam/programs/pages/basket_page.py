from .locators import BasePageLocators


class BasketPage():

    def should_not_be_success_message(self):
            assert self.is_not_element_present(*BasePageLocators.WRITING_EMPTY_BASKET), \
           "Success message is presented, but should not be"

    def should_be_disappeare_element(self):
        assert self.is_disappeared(*BasePageLocators.WRITING_EMPTY_BASKET), \
           "Success message is presented, but should not be"