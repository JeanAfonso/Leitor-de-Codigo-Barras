import logging

from enums import ProductType, Region
from validations import is_product_type_valid
from exceptions import InvalidBarCode

BLOCKED_COMPANIES = ['584']
BLOCKED_PRODUCT_TYPE_BY_REGION = {
    Region.MIDWEST.value: [ProductType.JEWEL.value]
}

logger = logging.getLogger(__name__)


class Package:

    def __init__(self, barcode):
        self.barcode = barcode
        try:
            self.origin, self._destination, self._loggi_code, self.company_id, self._product_type = self._split_barcode()
        except IndexError as e:
            logger.exception(f'An unexpected error')
            raise InvalidBarCode(f'BarCode Invalid, error: {e}')

    def _validate_barcode_format(self):
        if isinstance(self.barcode, int):
            raise ValueError(
                'Invalid barcode type, inserts an string barcode'
            )

    def _validate_product_type(self):
        return is_product_type_valid(self._product_type)

    def _validate_allowed_product_type_by_region(self, region):
        try:
            _region = Region(region)
        except ValueError:
            return False

        return self._product_type not in BLOCKED_PRODUCT_TYPE_BY_REGION.get(
            _region.value, []
        )

    def _validate_allowed_company(self) -> bool:
        return self.company_id not in BLOCKED_COMPANIES

    def _split_barcode(self) -> list:
        return [
            self.barcode[index: index + 3]
            for index in range(0, len(self.barcode), 3)
        ]

    def get_package_destination_region(self):
        return Region(self._destination)

    def validate_barcode(self) -> tuple[bool, str]:
        if not self._validate_product_type():
            return False

        if not self._validate_allowed_product_type_by_region(self.origin):
            return False

        if not self._validate_allowed_company():
            return False

        return True

    @property
    def destination(self):
        return Region(self._destination).name

    @property
    def product_type(self):
        return self._product_type

