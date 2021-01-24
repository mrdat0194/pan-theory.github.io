#!pip install pydot
# !brew install gprof2dot
import pydot

from IPython.display import Image, display


def view_pydot(pdot):
    plt = Image(pdot.create_png())
    display(plt)


# this time, in graph_type we specify we want a DIrected GRAPH
graph = pydot.Dot(graph_type='digraph')

# in the last example, we did no explicitly create nodes, we just created the edges and
# they automatically placed nodes on the graph. Unfortunately, this way we cannot specify
# custom styles for the nodes (although you CAN set a default style for all objects on
# the graph...), so let's create the nodes manually.

# creating nodes is as simple as creating edges!
node_a_1 = pydot.Node("tracks", style="filled", fillcolor="red", shape='box')
node_a_2 = pydot.Node("artists", style="filled", fillcolor="violet", shape='box')
node_a_3 = pydot.Node("albums", style="filled", fillcolor="violet", shape='box')
node_a_4 = pydot.Node("collections", style="filled", fillcolor="violet", shape='box')
# node_a_5 = pydot.Node("External", style="filled", fillcolor="yellow", shape='box')

# track info
# ['wiki', 'source', 'genius_url', 'fixed_genres', 'wiki_url', 'test', 'parent_genre', 'itunes_genres', 'allmusic_uuid', 'contributed_user', 'wiki_brief']

# but... what are all those extra stuff after "Node A"?
# well, these arguments define how the node is going to look on the graph,
# you can find a full reference here:
# http://www.graphviz.org/doc/info/attrs.html
# which in turn is part of the full docs in
# http://www.graphviz.org/Documentation.php

# neat, huh? Let us create the rest of the nodes!
node_a = pydot.Node("datasources", style="filled", fillcolor="red", shape='box')
node_b = pydot.Node("essential_playlist_datasource", style="filled", fillcolor="green", shape='box')
node_c = pydot.Node("crawlingtask", style="filled", fillcolor="green", shape='box')
node_d = pydot.Node("pointlog", style="filled", fillcolor="green", shape='box')

# Track
node_a_1_1 = pydot.Node("DurationMs")

# datasources
node_a__1 = pydot.Node("Id")
node_a__2 = pydot.Node("DataVerified")

# artists
node_a_2_1 = pydot.Node("UUID")
node_a_2_2 = pydot.Node("Name")

node_a_2_3 = pydot.Node("Info")
node_a_2_3_1 = pydot.Node(".wiki")
node_a_2_3_2 = pydot.Node(".wiki_url")
node_a_2_4 = pydot.Node("Ext")
node_a_2_4_1 = pydot.Node(".short_id")
node_a_2_4_2 = pydot.Node(".itune_artist_id")
node_a_2_4_3 = pydot.Node(".resize_images")

node_a_2_5 = pydot.Node("square_image_url")

# albums
node_a_3_1 = pydot.Node("UUID")
node_a_3_2 = pydot.Node("square_image_url")
node_a_3_3 = pydot.Node("Info")
node_a_3_3_1 = pydot.Node(".wiki")
node_a_3_3_1_1 = pydot.Node(".wiki.brief")

node_a_3_3_2 = pydot.Node(".wiki_url")
node_a_3_4 = pydot.Node("Ext")
node_a_3_4_1 = pydot.Node(".short_id")
node_a_3_4_2 = pydot.Node(".resize_images")

node_a_3_5 = pydot.Node("Artist")
node_a_3_6 = pydot.Node("iTuneUrl")
# collection
node_a_4_1 = pydot.Node("CollectionID")
# essential
node_b_1 = pydot.Node("essential_playlist", shape='box')
node_b_2 = pydot.Node("users", shape='box')
node_b_3 = pydot.Node("datasources")
node_b_4 = pydot.Node("tracks")
node_b_5 = pydot.Node("genres", style="filled", fillcolor="violet", shape='box')

#

# crawlingtask
node_c_1 = pydot.Node("itunes_album_tracks_release", shape='box')
node_c_2 = pydot.Node("tracks")

# pointlogs
node_d1 = pydot.Node("info")
node_d1_1 = pydot.Node(".email")
node_d1_2 = pydot.Node(".artist_name")
node_d1_3 = pydot.Node(".artist_info_url")
node_d1_4 = pydot.Node(".comment")
node_d2 = pydot.Node("ext")
node_d2_1 = pydot.Node(".crawler_id")
node_d3 = pydot.Node("UserId")
node_d4 = pydot.Node("ActionType")

# Contribution
node_d_1 = pydot.Node("users")
node_d_1_1 = pydot.Node("UUID")
node_d_2 = pydot.Node("crawlingtask")

node_d_2_1 = pydot.Node("ObjectId")
node_d_2_2 = pydot.Node("TaskDetail ->> '$.data_source_format_id'")
node_d_2_3 = pydot.Node("TaskDetail ->> '$.youtube_url'")

## Thumbnail
node_d_2_4 = pydot.Node("TaskDetail ->> '$.data_source_format_id'")
node_d_2_5 = pydot.Node("TaskDetail ->> '$.youtube_url'")

## C06
node_d_2_6 = pydot.Node("Ext ->> '$.itunes_track_task_id'")

# datasources
node_d_3 = pydot.Node("datasources")
node_d_3_1 = pydot.Node("TrackId")
node_d_3_2 = pydot.Node("FormatID")

node_d_3_3 = pydot.Node("Info")
node_d_3_3_1 = pydot.Node(".resize_images")
node_d_3_4 = pydot.Node("Ext")
node_d_3_4_1 = pydot.Node(".source")

node_d_3_5 = pydot.Node("SourceURI")
node_d_3_6 = pydot.Node("Valid")
node_d_3_7 = pydot.Node("youtubeid")
node_d_3_8 = pydot.Node("SourceName")
node_d_3_9 = pydot.Node("DurationMs")

node_d_4 = pydot.Node("collection_datasource", shape='box')
node_d_5 = pydot.Node("(pointlogs.CrawlerStatus or crawlingtasks.`Status` <> 'complete') and Date")

node_d_6 = pydot.Node("datasourceformatmaster", shape='box')
node_d_6_1 = pydot.Node("FormatID")

#
# thumbnail_second
# INSERT INTO crawlingtasks(Id,Priority,ActionID,ObjectId,Taskdetail) VALUES (uuid4(),499,'F91244676ACD47BD9A9048CF2BA3FFC1','5CDCBEBAA30F42E4BE56F31DD66856B3','{"PIC":"Minchan","when_exists":"keep both","use_track_image":true,"youtube_url":"https://www.youtube.com/watch?v=QpiZjTFU64o","data_source_format_id":"7F8B6CD82F28437888BD029EFDA1E57F"}');
# use_track_image
# INSERT INTO crawlingtasks(Id,Priority,ActionID,ObjectId,Taskdetail) VALUES (uuid4(),499,'F91244676ACD47BD9A9048CF2BA3FFC1','5CDCBEBAA30F42E4BE56F31DD66856B3','{"PIC":"Minchan","when_exists":"keep both","thumbnail_second":32,"youtube_url":"https://www.youtube.com/watch?v=QpiZjTFU64o","data_source_format_id":"7F8B6CD82F28437888BD029EFDA1E57F"}');
#

## itunes albums and Tracknum:
node_e = pydot.Node("itunes album_tracknum t1", style="filled", fillcolor="green", shape='box')

node_e1 = pydot.Node("TRIM(t1.ituneid)")

node_e2 = pydot.Node("TRIM(t1.tracknum)")

node_e_1 = pydot.Node("itunes_album_tracks_release")

node_e_1_1 = pydot.Node("ItuneAlbumId")

node_e_1_2 = pydot.Node("Seq")

node_e_1_3 = pydot.Node("Valid")

node_e_1_4 = pydot.Node("TrackName")

node_e_1_5 = pydot.Node("TrackArtist")

node_e_1_6 = pydot.Node("AlbumUUID")

node_e_2 = pydot.Node("tracks")

node_e_2_1 = pydot.Node("Title")

node_e_2_2 = pydot.Node("Artist")

node_e_2_3 = pydot.Node("Valid")

node_e_3 = pydot.Node("external_identity", style="filled", fillcolor="green", shape='box')

node_e_3_1 = pydot.Node("UUID")

node_e_3_2 = pydot.Node("ExternalId")

# trackcountlogs

## Crawler FC06, 0BD2, 0DE5, H348
node_f_1 = pydot.Node("ActionId_FC06", style="filled", fillcolor="yellow", shape='box')

node_f_2 = pydot.Node("ActionId_0DE5", style="filled", fillcolor="yellow", shape='box')

node_f_3 = pydot.Node("ActionId_0BD2", style="filled", fillcolor="yellow", shape='box')

# 2 cái này đều ảnh hưởng pointlog

## có mode replace
## tác động datasource
## Keep old_datasource_filename
node_f_4 = pydot.Node("ActionId_EDD9", style="filled", fillcolor="yellow", shape='box')

## không có mode replace
## Keep old_datasource_filename
node_f_5 = pydot.Node("ActionId_X2P0", style="filled", fillcolor="yellow", shape='box')

## autocrawler
node_f_6 = pydot.Node("ActionId_FCA0", style="filled", fillcolor="yellow", shape='box')

node_f_7 = pydot.Node("ActionId_2916", style="filled", fillcolor="yellow", shape='box')

node_f_8 = pydot.Node("ActionId_9B9E", style="filled", fillcolor="yellow", shape='box')

# tác động datasource
## có mode replace
## Keep old_datasource_filename
node_f_9 = pydot.Node("ActionId_FFC1", style="filled", fillcolor="yellow", shape='box')

## không có mode replace ,migrate
node_f_10 = pydot.Node("ActionId_8A83", style="filled", fillcolor="yellow", shape='box')

## missing artist
node_f_11 = pydot.Node("ActionId_BEAE", style="filled", fillcolor="yellow", shape='box')
node_f_12 = pydot.Node("ActionId_TG15", style="filled", fillcolor="yellow", shape='box')

#
node_f_1_1 = pydot.Node("albums", shape='box')
node_f_1_2 = pydot.Node("artist_albums", shape='box')
node_f_1_3 = pydot.Node("artists", shape='box')
node_f_1_4 = pydot.Node("external_identity", shape='box')

node_f_2_1 = pydot.Node("album_track", shape='box')
node_f_2_2 = pydot.Node("tracks", shape='box')
node_f_2_3 = pydot.Node("artist_track", shape='box')
node_f_2_4 = pydot.Node("external_identity", shape='box')
node_f_2_5 = pydot.Node("itune_album_track_release", shape='box')
node_f_2_6 = pydot.Node("Ext ->> '$.resize image/pip'")

#
node_g = pydot.Node("album_track", style="filled", fillcolor="violet", shape='box')
#
node_g_1 = pydot.Node("album_track", style="filled", fillcolor="violet", shape='box')
node_g_1_1 = pydot.Node("Videoid")

# urimapper

node_h = pydot.Node("urimapper", shape='box')

# # chart_video
#
node_i = pydot.Node("chart_video", shape='box')
#
node_i_1 = pydot.Node("Videoid")

# # collection_video
node_j = pydot.Node("collection_video", shape='box')

node_j_1 = pydot.Node("Videoid")

node_j_2 = pydot.Node("CollectionID")

# reportautocrawler
node_k_1 = pydot.Node("reportautocrawler_top100albums", shape='box')

node_k_1_1 = pydot.Node("DataSourcesExisted ->> '$.MP3_FULL'")

node_k_2 = pydot.Node("reportautocrawler_newclassic", shape='box')

node_k_2_1 = pydot.Node("DataSourcesExisted ->> '$.MP4_FULL'")

# usernarratives
node_l = pydot.Node("usernarratives", shape='box')

node_l_1 = pydot.Node("EntityUUID")

# genres
node_m = pydot.Node("genres", shape='box')

node_m_1 = pydot.Node("UUID")
node_m_2 = pydot.Node("title")
node_m_3 = pydot.Node("ParentId")

# genrematch.Genreid là 9 genre mẹ
# genres.title là tên genre mẹ
node_n = pydot.Node("genrematch", shape='box')

node_n_1 = pydot.Node("Genreid")
node_n_2 = pydot.Node("SubGenreid")

# ok, now we add the nodes to the graph
## node adding
graph.add_node(node_a_1)
graph.add_node(node_a_2)
graph.add_node(node_a_3)
graph.add_node(node_a_4)
# graph.add_node(node_a_5)
# graph.add_node(node_a_2_4_3)


graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)

graph.add_node(node_b_1)
graph.add_node(node_b_2)
graph.add_node(node_b_3)
graph.add_node(node_b_4)
graph.add_node(node_b_5)

graph.add_node(node_c_1)
graph.add_node(node_c_2)

graph.add_node(node_d_1)
graph.add_node(node_d_2)
graph.add_node(node_d_2_1)
graph.add_node(node_d_2_2)
graph.add_node(node_d_2_3)
graph.add_node(node_d_3)
graph.add_node(node_d_3_1)
graph.add_node(node_d_3_2)
graph.add_node(node_d_3_3)
graph.add_node(node_d_3_4)
graph.add_node(node_d_4)
graph.add_node(node_d_5)
graph.add_node(node_d_6)

graph.add_node(node_e)
graph.add_node(node_e_3)

# ActionId Crawlingtask
graph.add_node(node_f_1)

graph.add_node(node_f_1_1)
graph.add_node(node_f_1_2)
graph.add_node(node_f_1_3)
graph.add_node(node_f_1_4)

graph.add_node(node_f_2)

graph.add_node(node_f_2_1)
graph.add_node(node_f_2_2)
graph.add_node(node_f_2_3)
graph.add_node(node_f_2_4)
graph.add_node(node_f_2_5)

graph.add_node(node_f_3)
graph.add_node(node_f_4)
graph.add_node(node_f_5)

graph.add_node(node_f_6)
graph.add_node(node_f_7)
graph.add_node(node_f_8)
graph.add_node(node_f_9)
graph.add_node(node_f_10)
graph.add_node(node_f_11)
graph.add_node(node_f_12)

graph.add_node(node_g)

graph.add_node(node_g_1)

graph.add_node(node_h)

graph.add_node(node_i)

graph.add_node(node_j)

graph.add_node(node_k_1)
graph.add_node(node_k_2)

graph.add_node(node_l)

graph.add_node(node_m)

graph.add_node(node_n)

# and finally we create the edges
# to keep it short, I'll be adding the edge automatically to the graph instead
# of keeping a reference to it in a variable
graph.add_edge(pydot.Edge(node_a, node_a_1))
graph.add_edge(pydot.Edge(node_a_1, node_a_2))
graph.add_edge(pydot.Edge(node_a_1, node_a_3))
graph.add_edge(pydot.Edge(node_a_1, node_a_4))
# track
graph.add_edge(pydot.Edge(node_a_1, node_a_1_1))

# datasource
graph.add_edge(pydot.Edge(node_a, node_a__1))
graph.add_edge(pydot.Edge(node_a, node_a__2))

# graph.add_edge(pydot.Edge(node_a, node_a_5))

# a: artists
graph.add_edge(pydot.Edge(node_a_2, node_a_2_1, color='brown', label="get uuid"))
graph.add_edge(pydot.Edge(node_a_2, node_a_2_2, color='brown'))
graph.add_edge(pydot.Edge(node_a_2, node_a_2_3, color='brown'))
graph.add_edge(pydot.Edge(node_a_2_3, node_a_2_3_1, color='brown'))
graph.add_edge(pydot.Edge(node_a_2_3, node_a_2_3_2, color='brown'))
graph.add_edge(pydot.Edge(node_a_2, node_a_2_4, color='brown'))
graph.add_edge(pydot.Edge(node_a_2_4, node_a_2_4_1, color='brown'))
graph.add_edge(pydot.Edge(node_a_2_4, node_a_2_4_2, color='brown'))
graph.add_edge(pydot.Edge(node_a_2_4, node_a_2_4_3, color='brown', label="resize_image"))

graph.add_edge(pydot.Edge(node_a_2, node_a_2_5, color='brown'))

# a: albums
graph.add_edge(pydot.Edge(node_a_3, node_a_3_1, color='orange', label="get wiki"))
graph.add_edge(pydot.Edge(node_a_3, node_a_3_2, color='orange'))
graph.add_edge(pydot.Edge(node_a_3, node_a_3_3, color='orange'))
graph.add_edge(pydot.Edge(node_a_3_3, node_a_3_3_1, color='orange'))
graph.add_edge(pydot.Edge(node_a_3_3_1, node_a_3_3_1_1, color='orange'))
graph.add_edge(pydot.Edge(node_a_3_3, node_a_3_3_2, color='orange'))
graph.add_edge(pydot.Edge(node_a_3, node_a_3_4, color='orange'))
graph.add_edge(pydot.Edge(node_a_3_4, node_a_3_4_1, color='orange'))
graph.add_edge(pydot.Edge(node_a_3_4, node_a_3_4_2, color='orange', label="resize_image"))

graph.add_edge(pydot.Edge(node_a_3, node_a_3_5, color='orange'))
graph.add_edge(pydot.Edge(node_a_3, node_a_3_6, color='orange'))

# b: essential flow
graph.add_edge(pydot.Edge(node_b, node_b_1, color='blue', label="essential_flow"))
graph.add_edge(pydot.Edge(node_b_1, node_b_2, color='blue'))
graph.add_edge(pydot.Edge(node_b, node_b_3, color='blue'))
graph.add_edge(pydot.Edge(node_b_3, node_b_4, color='blue'))
graph.add_edge(pydot.Edge(node_b_1, node_b_5, color='blue'))

# c: checking crawl
graph.add_edge(pydot.Edge(node_c, node_c_1, color='green', label="checking crawling task ffc1"))
graph.add_edge(pydot.Edge(node_c_1, node_c_2, color='green'))
# graph.add_edge(pydot.Edge(node_c_2, node_b_3, color='green'))


# d: contributions
graph.add_edge(
    pydot.Edge(node_d, node_d_1, color='purple', label="checking contribution youtube, contribute but cannot show"))

graph.add_edge(pydot.Edge(node_d_1, node_d_2, color='purple'))

graph.add_edge(pydot.Edge(node_d_2, node_d_3, color='purple'))

graph.add_edge(pydot.Edge(node_d_2, node_d_2_1, color='purple'))
graph.add_edge(pydot.Edge(node_d_2, node_d_2_2, color='purple'))
graph.add_edge(pydot.Edge(node_d_2, node_d_2_3, color='purple'))
graph.add_edge(pydot.Edge(node_d_3, node_d_3_1, color='purple'))
graph.add_edge(pydot.Edge(node_d_3, node_d_3_2, color='purple'))
graph.add_edge(pydot.Edge(node_d_3, node_d_3_5, color='purple'))
graph.add_edge(pydot.Edge(node_d_3, node_d_3_6, color='purple'))
graph.add_edge(pydot.Edge(node_d_2_1, node_d_3_1, color='purple'))
graph.add_edge(pydot.Edge(node_d_2_2, node_d_3_2, color='purple'))
graph.add_edge(pydot.Edge(node_d_2_3, node_d_3_5, color='purple'))
graph.add_edge(pydot.Edge(node_d_3, node_d_4, color='purple'))
graph.add_edge(pydot.Edge(node_d_4, node_d_5, color='purple'))

# pointlog
graph.add_edge(pydot.Edge(node_d, node_d1))
graph.add_edge(pydot.Edge(node_d1, node_d1_1))
graph.add_edge(pydot.Edge(node_d1, node_d1_2))
graph.add_edge(pydot.Edge(node_d1, node_d1_3))
graph.add_edge(pydot.Edge(node_d1, node_d1_4))
graph.add_edge(pydot.Edge(node_d, node_d2))
graph.add_edge(pydot.Edge(node_d2, node_d2_1))
graph.add_edge(pydot.Edge(node_d, node_d3))
graph.add_edge(pydot.Edge(node_d3, node_d_1_1))
graph.add_edge(pydot.Edge(node_d, node_d4))
# user
graph.add_edge(pydot.Edge(node_d_1, node_d_1_1))

# datasources
graph.add_edge(pydot.Edge(node_d_3, node_d_3_3))
graph.add_edge(pydot.Edge(node_d_3, node_d_3_4))
graph.add_edge(pydot.Edge(node_d_3_3, node_d_3_3_1))
graph.add_edge(pydot.Edge(node_d_3_4, node_d_3_4_1))
#
graph.add_edge(pydot.Edge(node_d_3, node_d_3_8))

# datasourcesmaster
graph.add_edge(pydot.Edge(node_d_3, node_d_6))
graph.add_edge(pydot.Edge(node_d_6, node_d_6_1))
graph.add_edge(pydot.Edge(node_d_6_1, node_d_3_2))

# E: Album itunes track number
graph.add_edge(pydot.Edge(node_e_3, node_e_1, color='blue', label="Get trackID from newest update"))

graph.add_edge(pydot.Edge(node_e_3, node_e_3_1, color='blue'))

graph.add_edge(pydot.Edge(node_e_3, node_e_3_2, color='blue'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_6, color='blue'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_2, color='blue'))

graph.add_edge(pydot.Edge(node_e_3_1, node_e_1_6, color='blue'))

graph.add_edge(pydot.Edge(node_e, node_e_1, color='violet', label="Get trackID from track Seq and itune album"))

graph.add_edge(pydot.Edge(node_e_1, node_e_2, color='violet'))

graph.add_edge(pydot.Edge(node_e, node_e1, color='violet'))

graph.add_edge(pydot.Edge(node_e, node_e2, color='violet'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_1, color='violet'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_2, color='violet'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_3, color='violet'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_4, color='violet'))

graph.add_edge(pydot.Edge(node_e_1, node_e_1_5, color='violet'))

graph.add_edge(pydot.Edge(node_e_2, node_e_2_1, color='violet'))

graph.add_edge(pydot.Edge(node_e_2, node_e_2_2, color='violet'))

graph.add_edge(pydot.Edge(node_e_2, node_e_2_3, color='violet'))

graph.add_edge(pydot.Edge(node_e1, node_e_1_1, color='violet'))

graph.add_edge(pydot.Edge(node_e2, node_e_1_2, color='violet'))

graph.add_edge(pydot.Edge(node_e_2_1, node_e_1_4, color='violet'))

graph.add_edge(pydot.Edge(node_e_2_2, node_e_1_5, color='violet'))

# F: Crawling_actionId

graph.add_edge(pydot.Edge(node_f_1, node_f_1_1))
graph.add_edge(pydot.Edge(node_f_1, node_f_1_2))
graph.add_edge(pydot.Edge(node_f_1, node_f_1_3))
graph.add_edge(pydot.Edge(node_f_1, node_f_1_4))

graph.add_edge(pydot.Edge(node_f_2, node_f_2_1))
graph.add_edge(pydot.Edge(node_f_2, node_f_2_2))
graph.add_edge(pydot.Edge(node_f_2, node_f_2_3))
graph.add_edge(pydot.Edge(node_f_2, node_f_2_4))
graph.add_edge(pydot.Edge(node_f_2, node_f_2_5))
graph.add_edge(pydot.Edge(node_f_2, node_a))

graph.add_edge(pydot.Edge(node_a, node_f_2_6, label="E5"))

graph.add_edge(pydot.Edge(node_f_3, node_c_1))
# crawling impact on

graph.add_edge(pydot.Edge(node_f_4, node_g))
graph.add_edge(pydot.Edge(node_f_5, node_g))

graph.add_edge(pydot.Edge(node_f_6, node_f_1))
graph.add_edge(pydot.Edge(node_f_7, node_f_1))
graph.add_edge(pydot.Edge(node_f_8, node_f_1))

graph.add_edge(pydot.Edge(node_f_11, node_f_12))

# node_f_10

# H : urimapper

graph.add_edge(pydot.Edge(node_h, node_a_1))
graph.add_edge(pydot.Edge(node_h, node_a_2))
graph.add_edge(pydot.Edge(node_h, node_a_3))
graph.add_edge(pydot.Edge(node_h, node_b_1))

# i: videoid
graph.add_edge(pydot.Edge(node_g_1, node_i))
graph.add_edge(pydot.Edge(node_i, node_i_1))
graph.add_edge(pydot.Edge(node_g_1, node_g_1_1))
graph.add_edge(pydot.Edge(node_g_1_1, node_i_1))
graph.add_edge(pydot.Edge(node_g_1, node_j))
graph.add_edge(pydot.Edge(node_j, node_j_1))
graph.add_edge(pydot.Edge(node_g_1_1, node_j_1))
# j: collection_videos
graph.add_edge(pydot.Edge(node_j, node_j_2))
graph.add_edge(pydot.Edge(node_a_4, node_a_4_1))
graph.add_edge(pydot.Edge(node_a_4_1, node_j_2))

# K: reportauto
graph.add_edge(pydot.Edge(node_k_1, node_k_1_1))
graph.add_edge(pydot.Edge(node_k_2, node_k_2_1))
graph.add_edge(pydot.Edge(node_k_1_1, node_a__1))
graph.add_edge(pydot.Edge(node_k_2_1, node_a__1))

# L : narratives
graph.add_edge(pydot.Edge(node_l, node_l_1))

# M : genres
graph.add_edge(pydot.Edge(node_m, node_m_1))
graph.add_edge(pydot.Edge(node_m, node_m_2))
graph.add_edge(pydot.Edge(node_m, node_m_3))

# N : genresmatch : subgenre
graph.add_edge(pydot.Edge(node_n, node_n_1))
graph.add_edge(pydot.Edge(node_n, node_n_2))

# genres-subgenre
graph.add_edge(pydot.Edge(node_m, node_n))

graph.add_edge(pydot.Edge(node_m_1, node_n_1))
graph.add_edge(pydot.Edge(node_m_1, node_n_2))

# but, let's make this last edge special, yes?
# graph.add_edge(pydot.Edge(node_d, node_a, label="and back we go again", labelfontcolor="#009933", fontsize="10.0", color="blue"))

# and we are done
graph.write_png('example_graph.png')
view_pydot(graph)
import pandas as pd
print(graph.to_string())
# print(pd.DataFrame(graph.to_string()))

