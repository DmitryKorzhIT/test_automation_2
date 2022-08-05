from functions_dir.register import Register


register = Register()

register.land_first_page()
register.password_auth()
register.burger_menu_item(nav_item_name='Register')
# register.header_icons_item(header_icons_item_name='Register')
register.click_on_product_image(product_number=3)
register.choose_product_size(size_number=0)
register.click_on_register_item_btn()
register.conditions_labels()
