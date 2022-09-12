from .receipt import Receipt

class ReceiptBuilder:
    mapping = {'location_name': 'restaurant_name', 
               'location_address': 'address',
               'obligation_end_date_yyyymmdd': 'end_date',
               'total_receipts': 'total'}
    api_field_names = mapping.keys()
    columns = ['total', 'address', 'end_date', 'restaurant_name']

    @classmethod
    def receipt(self, **kwargs):
        # set class attributes from the keyword arguments
        receipt = Receipt()
        for k, v in kwargs.items():
            if k in self.api_field_names:
                setattr(receipt, self.mapping.get(k), v)

        return receipt

    @classmethod
    def receipts(self, receipt_records):
        receipts = []

        for receipt in receipt_records:
            receipts.append(self.receipt(**receipt))

        return receipts


