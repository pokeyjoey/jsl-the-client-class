from src.model.receipt import Receipt
from src.model.receipt_builder import ReceiptBuilder

import pytest
import requests

@pytest.fixture()
def receipt():
    receipt_data = [('taxpayer_number', '12727298569'), ('taxpayer_name', 'MWD AUSTIN DOWNTOWN, LLC'), ('taxpayer_address', '1000 N POST OAK RD STE 220'), ('taxpayer_city', 'HOUSTON'), ('taxpayer_state', 'TX'), ('taxpayer_zip', '77055'), ('taxpayer_county', '101'), ('location_number', '1'), ('location_name', "MAX'S WINE DIVE"), ('location_address', '207 SAN JACINTO BLVD STE 200'), ('location_city', 'AUSTIN'), ('location_state', 'TX'), ('location_zip', '78701'), ('location_county', '227'), ('inside_outside_city_limits_code_y_n', 'Y'), ('tabc_permit_number', 'MB944126'), ('responsibility_begin_date_yyyymmdd', '2016-05-13T00:00:00.000'), ('responsibility_end_date_yyyymmdd', '2020-11-20T00:00:00.000'), ('obligation_end_date_yyyymmdd', '2017-10-31T00:00:00.000'), ('liquor_receipts', '23957'), ('wine_receipts', '59644'), ('beer_receipts', '10021'), ('cover_charge_receipts', '0'), ('total_receipts', '93622')]


    # set the class atrributes
    receipt_builder = ReceiptBuilder()
    receipt = ReceiptBuilder.receipt(**dict(receipt_data))

    yield receipt

@pytest.fixture()
def bad_receipt_data():
    bad_receipt_data = [('bogus_key', 'bogus_value'), ('taxpayer_number', '12727298569'), ('taxpayer_name', 'MWD AUSTIN DOWNTOWN, LLC'), ('taxpayer_address', '1000 N POST OAK RD STE 220'), ('taxpayer_city', 'HOUSTON'), ('taxpayer_state', 'TX'), ('taxpayer_zip', '77055'), ('taxpayer_county', '101'), ('location_number', '1'), ('location_name', "MAX'S WINE DIVE"), ('location_address', '207 SAN JACINTO BLVD STE 200'), ('location_city', 'AUSTIN'), ('location_state', 'TX'), ('location_zip', '78701'), ('location_county', '227'), ('inside_outside_city_limits_code_y_n', 'Y'), ('tabc_permit_number', 'MB944126'), ('responsibility_begin_date_yyyymmdd', '2016-05-13T00:00:00.000'), ('responsibility_end_date_yyyymmdd', '2020-11-20T00:00:00.000'), ('obligation_end_date_yyyymmdd', '2017-10-31T00:00:00.000'), ('liquor_receipts', '23957'), ('wine_receipts', '59644'), ('beer_receipts', '10021'), ('cover_charge_receipts', '0'), ('total_receipts', '93622')]

    yield bad_receipt_data

@pytest.fixture()
def receipts():
    # get the restaurant receipt data from the api
    response = requests.get("https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE")
    restaurant_receipts = response.json()

    # create a list of receipt objects
    receipts = ReceiptBuilder.receipts(restaurant_receipts)

    yield receipts

def test_receipt(receipt):
    assert type(receipt) == Receipt

def test_receipt_has_total(receipt):
    assert receipt.total == '93622'

def test_receipt_has_address(receipt):
    assert receipt.address == '207 SAN JACINTO BLVD STE 200'

def test_receipt_has_end_date(receipt):
    assert receipt.end_date == '2017-10-31T00:00:00.000'

def test_receipt_has_restaurant_name(receipt):
    assert receipt.restaurant_name == "MAX'S WINE DIVE"

def test_receipts_has_address(receipts):
    for receipt in receipts:
        assert hasattr(receipt, 'address')

def test_receipts_has_total(receipts):
    for receipt in receipts:
        assert hasattr(receipt, 'total')

def test_receipts_has_end_date(receipts):
    for receipt in receipts:
        assert hasattr(receipt, 'end_date')

def test_receipts_has_restaurant_name(receipts):
    for receipt in receipts:
        assert hasattr(receipt, 'restaurant_name')

