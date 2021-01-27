import json
import mysql.connector
from functools import reduce
from main_def import config_sql

def extract_json(table, Json_field, method_number):
    config_file = config_sql
    with open(config_file) as json_data_file:
        config = json.load(json_data_file)

    if config.get('mysql', False):
        mysql_config = config['mysql']
        mydb = mysql.connector.connect(
            host=mysql_config['host'],
            user=mysql_config['user'],
            password=mysql_config['password'],
            database=mysql_config['database'],
            port=mysql_config['port']
        )

    mycursor = mydb.cursor()
    if method_number == 1:
        Select_distinct_name = f"SELECT id, JSON_KEYS({Json_field}) from {table} WHERE {Json_field} is not NULL AND valid = 1 GROUP BY JSON_KEYS({Json_field});"
        mycursor.execute(Select_distinct_name)
        result = mycursor.fetchall()
        return result
    else:
        Select_distinct_name = f"""select distinct(json_extract(json_keys({Json_field}),'$[0]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[1]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[2]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[3]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[4]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[5]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[6]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[7]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[8]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[9]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[10]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[11]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[12]')) from {table}
               union
               select distinct(json_extract(json_keys({Json_field}),'$[13]')) from {table};"""
        mycursor.execute(Select_distinct_name)
        result = mycursor.fetchall()
        # result trả về list of tuples:
        old_strings = reduce(lambda x, y: x + y, result)
        new_strings = []

        for string in old_strings:
            if string is not None:
                new_string = string.replace('"', "")
                new_strings.append(new_string)
        return new_strings



if __name__ == "__main__":
    # result = extract_json("crawlingtasks","TaskDetail",1)
    #
    # result = extract_json("datasources", "Ext", 1)
    # # ['static_video', 'resize_images', 'faststart', 'original_datasource', 'hls_files', 'Title', 'n_favorites', 'justin',
    # #  'is_title_updated', 'source', 'artist', 'video_type', 'background_360_video', 'bg_360_file_name',
    # #  'resize_images_source', 'can_convert_background_video', 'is_artist_updated', 'hls_supported', 'can_faststart',
    # #  'trackid_remove', 'artist_name', 'on_create_note', 'background_720_video', 'bg_720_file_name', 'cdn_domain',
    # #  'in_top100', 'video_source', 'sub_genres', 'bg_1080_file_name', 'background_1080_video', 'faststart_migrated',
    # #  'is_background_360_video_cropped', 'source_title', 'screen_shot_interval', 'published_at',
    # #  'is_background_720_video_cropped', 'loudness_detection_note', 'loudness_detection_output', 'sub_genre_ids',
    # #  'video_source2', 'featured_by_samV']

    # result = extract_json("artists" ,"Ext" ,2)
    # ['short_id', 'n_playlists', 'square_image', 'itune_artist_id', 'external_id', 'image_verification',
    #  'itunes_artist_id', 'resize_images', 'n_playlists_created_time', 'is_raw_info_crawled', 'external_artist_ids']
    result = extract_json("artists", "Info", 2)
    # ['allmusic', 'wiki', 'iTunes', 'iTunes_url', 'allmusic_url', 'wiki_url', 'info_url', 'social_urls',
    #  'contributed_user', 'fixed_genres', 'background_preview_url']

    print(result)
