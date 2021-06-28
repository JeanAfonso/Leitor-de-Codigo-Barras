import logging

from enums import Region, ProductType
from package import Package


logger = logging.getLogger(__name__)

barcode_list = [
    '888555555123888',
    '333333555584333',
    '222333555124000',
    '000111555874555',
    '111888555654777',
    '111333555123333',
    '555555555123888',
    '888333555584333',
    '111333555124000',
    '333888555584333',
    '555888555123000',
    '111888555123555',
    '888000555845333',
    '000111555874000',
    '111333555123555'
]

def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

PACKAGES_BY_COMPANIES = {}
PACKAGES_BY_REGION = {}
PACKAGES_BY_DESTINATION = {}
PACKAGES_BY_TYPE = {}

for barcode in barcode_list:
    package = Package(barcode)
    if package.validate_barcode():
        add_element(PACKAGES_BY_COMPANIES, package.company_id, barcode)
        add_element(PACKAGES_BY_REGION, package.origin, barcode)
        add_element(PACKAGES_BY_DESTINATION, package._destination, barcode)
        add_element(PACKAGES_BY_TYPE, package._product_type, barcode)

# Packages by companies
for company, packages in PACKAGES_BY_COMPANIES.items():
    print(f'Company Id: {company} - packages number: {len(packages)}')

# Packages by Region of origin
for region, packages in PACKAGES_BY_REGION.items():
    print(f'Region: {Region(region).name} - packages: {packages}')

# Packages by Type
for type, packages in PACKAGES_BY_TYPE.items():
    print(f'Type: {ProductType(type).name} - packages: {packages}')

# Packages by Destination
for destination, packages in PACKAGES_BY_DESTINATION.items():
    print(f'Destination: {Region(destination).name} - packages: {packages}')

# South packages with Toys
south_packages = PACKAGES_BY_REGION.get(Region.SOUTH.value, [])
for barcode in south_packages:
    package = Package(barcode)
    if package.product_type == ProductType.TOY.value:
        print(f'The SOUTH packages contains toys Barcode: {package.barcode}')
