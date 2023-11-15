from __future__ import print_function

from googleapiclient.errors import HttpError

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def create_image(presentation_id):
  """
  Creates images the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  # If modifying these scopes, delete the file token.pickle.
  SCOPES = ['https://www.googleapis.com/auth/presentations.readonly', 'https://www.googleapis.com/auth/presentations']

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
        service.presentations().get(presentationId=PRESENTATION_ID).execute()
    )


    IMAGE_URL = (
        "https://www.google.com/images/branding/"
        "googlelogo/2x/googlelogo_color_272x92dp.png"
    )
    slides = presentation.get("slides")
    imagePaths = sorted(list(paths.list_images("images/")))

    for i, slide in enumerate(slides):

        print(slide)
        # pylint: disable=invalid-name
        requests = []
        image_id = "MyImage_" + str(i)
        emu4M = {"magnitude": 4000000, "unit": "EMU"}
        print(i)
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
            .batchUpdate(presentationId=presentation_id, body=body)
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

  PRESENTATION_ID = "1G8CSwm5UhjXpwqBmr5SdfMtME_5KvZ4bT6_BbMaanPY"

  create_image(PRESENTATION_ID)