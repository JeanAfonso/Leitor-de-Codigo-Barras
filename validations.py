from enums import ProductType


def is_product_type_valid(product_type):
    try:
        return bool(ProductType(product_type))
    except ValueError:
        return False
