from __future__ import print_function

from googleapiclient.errors import HttpError

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from main_def import credentials, tokens

def copy_presentation(drive_service,presentation_id, copy_title):
    """
    Creates the copy Presentation the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    try:
        body = {"name": copy_title}
        drive_response = (
            drive_service.files().copy(fileId=presentation_id, body=body).execute()
        )
        presentation_copy_id = drive_response.get("id")

    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Presentations  not copied")
        return error

    return presentation_copy_id

def create_slide(service,presentation_id, slide_id, page_id):
    """
    Creates the Presentation the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.\n
    """

    try:
        # Add a slide at index 1 using the predefined
        # 'TITLE_AND_TWO_COLUMNS' layout and the ID page_id.
        duplicate_object_request = {
            "objectId": slide_id
        }

        batch_update_request = {
            "requests": [{
                "duplicateObject": duplicate_object_request
            }]
        }

        response = (
            service.presentations()
            .batchUpdate(presentationId=presentation_id, body=batch_update_request)
            .execute()
        )

        # create_slide_response = response.get("replies")[0].get("duplicateObjectId")
        # print(f"Created slide with ID:{(create_slide_response.get('duplicateObjectId'))}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Slides not created")
        return error



def drive_get_file(presentation_id, target_folder_id, new_slide):
    SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.appdata','https://www.googleapis.com/auth/drive.file' ]
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(tokens):
        with open(tokens, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tokens, 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(q="'" + target_folder_id + "' in parents", fields="nextPageToken, files(id, name)").execute()

    PRESENTATION_ID = copy_presentation(service, presentation_id, new_slide)

    permission = {
        'type': 'anyone',
        'role': 'writer',
    }

    request = service.permissions().create(fileId=PRESENTATION_ID, body=permission)
    request.execute()

    print(PRESENTATION_ID)

    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            service.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=item['id']).execute()
            print(u'{0} ({1})'.format(item['name'], item['id']))

    return PRESENTATION_ID, items

def create_image(presentation_id, new_slide, target_folder_id):
  """
  Creates images the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  # If modifying these scopes, delete the file token.pickle.
  SCOPES = ['https://www.googleapis.com/auth/presentations.readonly', 'https://www.googleapis.com/auth/presentations' ]

  # The ID of a sample presentation.

  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  try:
    service = build("slides", "v1", credentials=creds)

    presentation = (
        service.presentations().get(presentationId=presentation_id).execute()
    )

    PRESENTATION_ID, items = drive_get_file(presentation_id, target_folder_id, new_slide)

    for i in range(len(items)-1):
        slides = presentation.get("slides")

        image_id = "MyImage_" + str(i)
        create_slide(service, PRESENTATION_ID, slides[0]['objectId'] ,image_id)

    presentation = (
        service.presentations().get(presentationId=PRESENTATION_ID).execute()
    )

    slides = presentation.get("slides")

    for i, slide in enumerate(slides):
        fileid = items[1]
        # print(fileid)
        # pylint: disable=invalid-name
        requests = []
        image_id = "MyImage_" + str(i)

        emu4M = {"magnitude": 4000000, "unit": "EMU"}
        IMAGE_URL = "https://drive.google.com/uc?export=download&id=" + fileid['id']

        # IMAGE_URL =  "https://drive.google.com/uc?export=download&id=1G9NSkfTPsJTuffXtcjtZ9P1oyfxUmq4p"

        print(IMAGE_URL)

        requests.append(
            {
                "createImage": {
                    "objectId": image_id,
                    "url": IMAGE_URL,
                    "elementProperties": {
                        "pageObjectId": slide['objectId'],
                        "size": {"height": emu4M, "width": emu4M},
                        "transform": {
                            "scaleX": 1,
                            "scaleY": 1,
                            "translateX": 100000,
                            "translateY": 100000,
                            "unit": "EMU",
                        },
                    },
                }
            }
        )

        # Execute the request.
        body = {"requests": requests}

        response = (
            service.presentations()
            .batchUpdate(presentationId=PRESENTATION_ID, body=body)
            .execute()
        )

        create_image_response = response.get("replies")[0].get("createImage")
        print(f"Created image with ID: {(create_image_response.get('objectId'))}")

  except HttpError as error:
    print(f"An error occurred: {error}")
    print("Images not created")
    return error


if __name__ == "__main__":
  # Put the presentation_id, Page_id of slides whose list needs
  # to be submitted.

  FIX_SLIDE_ID = "1G8CSwm5UhjXpwqBmr5SdfMtME_5KvZ4bT6_BbMaanPY"
  new_slide = "New presentation"
  target_folder_id = '1TTpwAAzmBTLKDOtPjETKFOQAyzHAN_wW'
  create_image(FIX_SLIDE_ID,new_slide, target_folder_id )
