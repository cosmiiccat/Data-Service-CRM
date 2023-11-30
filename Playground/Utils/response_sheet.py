import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from . import MongoClient

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "11gRhITmQdhmPeyyCXSlKyQrd3rdDI0wE6Yfb5_zo3G4"
SAMPLE_RANGE_NAME = "A1"

def interact_sheet(form_id):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        values = list()
        queries = list(MongoClient.find({"type": "query", "form-id": form_id}))
        header = ["Customer-id"]; customer_ids = list()
        for query in queries:
            header.append(query["query"])
            # print(f'''Query - {query["id"]}''')
            responses = MongoClient.find({"type": "response", "query-id": query["id"]})
            for response in responses:
                # print(response["customer-id"])
                if response["customer-id"] not in customer_ids:
                    customer_ids.append(response["customer-id"])
        values.append(header)
        for customer_id in customer_ids:
            row = [str(customer_id)]
            for query in queries:
                responses = list(MongoClient.find({"type": "response", "customer-id": customer_id, "query-id": query["id"]}))
                if len(responses) > 0:
                    row.append(responses[0]["response"])
                else:
                    row.append("")
            values.append(row)

        # print(customer_ids)

        # ------------- READING SHEET ---------------- #

        # print(f"Attempting to fetch data from range: {SAMPLE_RANGE_NAME}")
        # result = (
        #     sheet.values()
        #     .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        #     .execute()
        # )
        # values = result.get("values", [])

        body = {
            "values": values
        }
        result = sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="RAW",
            body=body
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")

        if not values:
            print("No data found.")
            return
        
        print(values)

    except HttpError as err:
        print(err)


# interact_sheet(form_id="3abe191c-aedd-4b79-9378-e4fca037492b")
