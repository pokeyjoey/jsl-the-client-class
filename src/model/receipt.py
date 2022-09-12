class Receipt:
    columns = ['total', 'address', 'end_date', 'restaurant_name']

    def __init__(self, **kwargs):
        # verify that keyword arguments exist in columns
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')

        # set class attributes from the keyword arguments
        for k, v in kwargs.items():
            if k in self.columns:
                setattr(self, k, v)

