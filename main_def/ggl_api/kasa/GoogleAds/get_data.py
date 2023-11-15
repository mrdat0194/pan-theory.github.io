import sys
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

client = GoogleAdsClient.load_from_storage("google-ads.yaml")

def get_data(client, customer_id):
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          campaign.name,
          campaign.status,
          segments.device,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.average_cpc,
          metrics.cost_micros
        FROM campaign
        WHERE segments.date DURING LAST_30_DAYS
        """

    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id, query=query)

    try:
        for batch in response:
            for row in batch.results:
                print(
                    row
                )
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)


    if __name__ == "__main__":
        get_data(client, '5938713786')
