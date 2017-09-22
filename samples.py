# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet
import logging

# TODO: Set your API access token here, or leave as None and set as environment variable "SMARTSHEET_ACCESS_TOKEN"
access_token = None


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
logging.basicConfig(filename='samples.log', level=logging.INFO)

# Add your test calls here
# set_sheet_link(ss_client, 6903887367038852, 6144655761926020, 7262773366286212, 5670346721388420, 3626203910301572, 5759377954105220)

print('Done')