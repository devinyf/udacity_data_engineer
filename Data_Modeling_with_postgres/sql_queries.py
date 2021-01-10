# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS t_songplays;"
user_table_drop = "DROP TABLE IF EXISTS t_users;"
song_table_drop = "DROP TABLE IF EXISTS t_songs;"
artist_table_drop = "DROP TABLE IF EXISTS t_artists;"
time_table_drop = "DROP TABLE IF EXISTS t_time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE "public"."t_songplays" (
  "sonplay_id" varchar NOT NULL DEFAULT '',
  "start_time" varchar NOT NULL DEFAULT '',
  "user_id" int8 NOT NULL DEFAULT 0,
  "level" varchar NOT NULL DEFAULT '',
  "song_id" varchar,
  "artist_id" varchar,
  "session_id" int8 NOT NULL DEFAULT 0,
  "location" varchar NOT NULL DEFAULT '',
  "user_agent" varchar NOT NULL DEFAULT '',
  CONSTRAINT "t_songplays_pkey" PRIMARY KEY ("sonplay_id")
)
;

""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS "t_users" (
  "user_id" int8 NOT NULL,
  "first_name" varchar NOT NULL DEFAULT '',
  "last_name" varchar NOT NULL DEFAULT '',
  "gender" varchar NOT NULL DEFAULT '',
  "level" varchar NOT NULL DEFAULT '',
  CONSTRAINT "t_users_pkey" PRIMARY KEY ("user_id")
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS "t_songs" (
  "song_id" varchar NOT NULL DEFAULT '',
  "title" varchar NOT NULL DEFAULT '',
  "artist_id" varchar NOT NULL DEFAULT '',
  "year" int4 NOT NULL DEFAULT 0,
  "duration" FLOAT NOT NULL DEFAULT 0,
  CONSTRAINT "t_songs_pkey" PRIMARY KEY ("song_id")
);
""")

artist_table_create = ("""
CREATE TABLE "public"."t_artists" (
  "artist_id" varchar NOT NULL DEFAULT '',
  "name" varchar NOT NULL DEFAULT '',
  "location" varchar NOT NULL DEFAULT '',
  "latitude" float8 NOT NULL DEFAULT 0,
  "longitude" float8 NOT NULL DEFAULT 0,
  CONSTRAINT "t_artists_pkey" PRIMARY KEY ("artist_id")
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS "t_time" (
  "start_time" varchar NOT NULL DEFAULT '',
  "hour" int2 NOT NULL DEFAULT 0,
  "day" int2 NOT NULL DEFAULT 0,
  "week" int2 NOT NULL DEFAULT 0,
  "month" int2 NOT NULL DEFAULT 0,
  "year" int4 NOT NULL DEFAULT 0,
  "weekday" varchar NOT NULL DEFAULT '',
  CONSTRAINT "t_time_pkey" PRIMARY KEY ("start_time")
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO t_songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)  ON CONFLICT(sonplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO t_users(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO NOTHING
""")

song_table_insert = ("""INSERT INTO t_songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO t_artists(artist_id, name, location, latitude, longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO t_time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
	SELECT song_id, s.artist_id FROM t_songs as s JOIN t_artists as a ON s.artist_id = a.artist_id
	WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]