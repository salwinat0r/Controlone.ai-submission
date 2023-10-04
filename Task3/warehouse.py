import csv

class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    @staticmethod
    def save_and_display_parcel_details(parcels):
        # Create a dictionary to store parcels by category
        category_parcels = {
            'Filters': [],
            'Automobil_parts': [],
            'Cargo_containeer': [],
        }

        # Group parcels by category
        for parcel in parcels:
            category_parcels[parcel.parcel_category].append(parcel.parcel_number)

        # Write the parcel numbers to a CSV file
        with open('parcel_details.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Filters', 'Automobil_parts', 'Cargo_containeer'])
            for i in range(max(len(category_parcels['Filters']), len(category_parcels['Automobil_parts']), len(category_parcels['Cargo_containeer']))):
                writer.writerow([
                    category_parcels['Filters'][i] if i < len(category_parcels['Filters']) else '',
                    category_parcels['Automobil_parts'][i] if i < len(category_parcels['Automobil_parts']) else '',
                    category_parcels['Cargo_containeer'][i] if i < len(category_parcels['Cargo_containeer']) else '',
                ])

# Create a list of WarehouseParcelDetail objects
parcels = [
    WarehouseParcelDetail(23456, 66234, 'Filters'),
    WarehouseParcelDetail(66234, 86643, 'Automobil_parts'),
    WarehouseParcelDetail(98432, 64326, 'Cargo_containeer'),
    WarehouseParcelDetail(96355, 74328, 'Filters'),
    WarehouseParcelDetail(86643, 56382, 'Automobil_parts'),
    WarehouseParcelDetail(53463, 48923, 'Cargo_containeer'),
    WarehouseParcelDetail(83722, 48095, 'Filters'),
    WarehouseParcelDetail(64326, 70172, 'Automobil_parts'),
    WarehouseParcelDetail(87653, 78297, 'Cargo_containeer'),
]

# Save the parcels to the CSV file
WarehouseParcelDetail.save_and_display_parcel_details(parcels)
