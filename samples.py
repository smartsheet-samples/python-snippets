# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet
import logging

# TODO: Set your API access token here, or leave as None and set as environment variable "SMARTSHEET_ACCESS_TOKEN"
access_token = None

# Download an image in a cell
def download_cell_image(client, sheet_id, row_id, column_id, default_filename):
    # Get desired row
    row = client.Sheets.get_row(sheet_id, row_id)
    cell = row.get_column(column_id)
    image = cell.image

    filename = getattr(image, 'alt_text', default_filename)

    # Obtain a temporary image URL
    imageUrl = ss_client.models.ImageUrl( { "imageId": image.id } ) 
    response = ss_client.Images.get_image_urls([imageUrl])
    url = response.image_urls[0].url

   # Download the image
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

# Set column definition to a list of contacts
def add_column_contacts(ss_client, sheet_id, column_id, emails):
    column = ss_client.models.Column()
    column.type = 'CONTACT_LIST'

    contacts = []

    for email in emails:
        contact_option = ss_client.models.contact_option.ContactOption()
        contact_option.email = email
        contacts.append(contact_option)

    column.contact_options = contacts
    ss_client.Sheets.update_column(sheet_id, column_id, column)
    return None

# Set sheet link
# Value from source will be visible in dest
def set_sheet_link(ss_client, source_sheet_id, source_row_id, source_column_id, dest_sheet_id, dest_row_id, dest_column_id):
    cell_link = ss_client.models.CellLink()
    cell_link.sheet_id = source_sheet_id
    cell_link.row_id = source_row_id
    cell_link.column_id = source_column_id

    cell = ss_client.models.Cell()
    cell.column_id = dest_column_id
    cell.value = None
    cell.link_in_from_cell = cell_link

    row = ss_client.models.Row()
    row.id = dest_row_id
    row.cells.append(cell)

    rows = []
    rows.append(row)

    ss_client.Sheets.update_rows(dest_sheet_id, rows)
    return None

print('Starting ...')

# Initialize client
ss_client = smartsheet.Smartsheet(access_token)
# Make sure we don't miss any error
ss_client.errors_as_exceptions(True)

# setup logging
logging.basicConfig(filename='samples.log', level=logging.DEBUG)

# Add your test calls here
sheet_id = 5370997298751364
row_id = 6483985534609284
column_id = 2009176927954820

sheet_id2 = 6903887367038852
row_id2 = 6144655761926020
column_id2 = 7262773366286212

download_cell_image(ss_client, sheet_id, row_id, column_id, "save.jpg")

# add_column_contacts(ss_client, sheet_id, column_id, ['foo@bar.com'])

# set_sheet_link(ss_client, sheet_id2, row_id2, column_id2, sheet_id, row_id, column_id)

print('Done')
