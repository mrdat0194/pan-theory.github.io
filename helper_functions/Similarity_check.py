import re
from my_functions import timer

@timer
def strlist_not_in_list():
    exclusion_list = ["intro","outro","remix","dub","instrumental","karaoke","inst.","interlude","prelude","version","ver.","versión","skit","interview","edit","radio","live","en Vivo","ao Vivo","performance","session","original","cut","extended","short","acoustic","acústica","acústico","clean","explicit","piano","exclusive","medley","mono","commentary","demo","alternate","chopped","take ","outtake","part","pt.","pts.","act ","7''","12''","directo","concierto","reprise","retake","remake","rework","remastered","rmx","mix","re-recorded"]
    youtube_title = ["arty - perfect strangers (official lyric video)","alpha 9 - sleepwalker","in the dark","our origin","sundown","pearl (mixed)","ferry corsten & paul oakenfold - a slice of heaven (kaleidoscope)","patterns of the soul (mixed) (davey asprey remix)","running for peace (mixed)","see you again (mixed)","open my mind (mixed)","fireflies (mixed) (jorn van deynhoven remix)","you & i (mixed) (aly & fila club mix)","fall for you","d (don\'t go) (mixed)","zombie (mix cut)","northern star (mixed)","light the way (mixed) (bryan kearney remix)","missing (mixed) (jorn van deynhoven remix)","army of angels (mixed)","enough echo (mixed)","coming home (mixed) (standerwick remix)","popcorn","free","till the sunrise","i feel love (mixed) (omar sherif remix)","stadium arcadium (mixed)","be in the moment (mixed) (allen watts remix)","midnight","music rescues me (mixed)","rebirth (mixed) (ahmed romel remix)","seventh heaven (asot 895)","wherever you are (mixed) (solis & sean truby remix)","safe from harm (mixed) (giuseppe ottaviani remix)","just as you are (mixed)","for the one you love (mixed)","alone in the wilderness (mixed)","zubr (mixed)","the air i breathe (mixed)","activate (mixed)","lifting you higher (asot 900 anthem)","thirty three south","i\'ve been thinking about you (mixed)","take me there (mixed)","u","a world beyond (mixed)","disturbance (mixed)","the wolf (mixed)","the sound of e (mixed) (jorn van deynhoven remix)","ready to rave (mixed)","shock therapy (mixed) (rising altitude mix)","a state of trance year mix 2018 (mixed) (outro: the verdict)","a state of trance year mix 2018 (mixed) (outro: the verdict)","coming home (mix cut) (standerwick remix)","sex, love & water (drym extended remix)","live at tomorrowland belgium 2018 (highlights) (mix cut) (intro)","a state of trance (asot899) (intro)","drowning (avicii remix)","armin van buuren feat. james newman - therapy (sebastian davidson remix)","mowgli","the night sky","magus","i believe","ilan bluestone - noa","blue angel","till the sky falls down (live at asot 500 4am intro mix)","rogue","yalung","cyclone","i didn\'t know","bobina - something about you","nightfalls (original mix)","alpine","ram - rambulance","the space brothers - heaven will come (the noble six remix)","a state of trance (asot899) (outro)","live at sunburn festival india 2018 (mixed) (intro)","dimitri vegas & like mike x armin van buuren x w&w - repeat after me (live at tomorrowland 2018)","airborn, bogdan vix & keyplayer feat. alexandra badoi - runaway [#ultra2019]","armin van buuren - lifting you higher (asot 900 anthem) [blasterjaxx remix] [#ultra2019]","armin van buuren vs. w&w - ready to rave (live at ultra japan 2018)","live at sunburn festival india 2018 (mixed) (outro)","wild wild son (extended club mix)","zombie (mixed)","la résistance de l\'amour (mixed)","another you (mixed)","run away (mixed)","slipstream","in my control","not techno","alive","comet","flight of the buzzard","therapy (leo reyes extended remix)","protoculture & sue mclaren – secret weapon [#asot868]","rapid eye - stealing beauty (daxson remix)  [#asot868]","the sound of goodbye","lange & sarah howells - out of the sky (andres sanchez remix)","allen watts — polarize (daniel skyver remix)","ultimate - adam\'s peak","the air i breathe","just a dream","inferno","vini vici - where the heart is","orjan nilsen - that one night","orjan nilsen - in a thousand ways (feat. rykka)","ashley wallbridge feat. nash - gods","orjan nilsen - i see spots","what a rush","resistance","orjan nilsen feat. r-lend - without kontakt","chris brown, tyga - ayo (official audio)","avril lavigne - nobody\'s home (audio)","knockin\' on heaven\'s door (studio version)","error: this video is not available.","avril lavigne - what the hell","avril lavigne - push ft. evan taubenfeld (audio)","wish you were here","avril lavigne - smile (audio)","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","avril lavigne - alice (extended version) (official music album/full song)","error: this video is not available.","avril lavigne - goodbye (audio)","error: this video is not available.","error: this video is not available.","avril lavigne - wish you were here (acoustic version) (official music album/full song)","error: this video is not available.","what the hell (bimbo jones remix)","what the hell (instrumental) - avril lavigne [hq]","wish you were here (instrumental) - avril lavigne [hq]","error: this video is not available.","girlfriend","avril lavigne - girlfriend (the submarines\' time wrap \'66 mix)","error: this video is not available.","avril lavigne - girlfriend (french version) (audio)","girlfriend (french version - explicit)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - french) [explicit]","avril lavigne - girlfriend (spanish version) (audio)","girlfriend (spanish version - explicit)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - spanish) [explicit]","avril lavigne - girlfriend (german version) (audio)","girlfriend (german version - explicit)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - german) [explicit]","avril lavigne - girlfriend (italian version) (audio)","girlfriend (italian version - explicit)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - italian) [explicit]","avril lavigne - girlfriend (portuguese version) (audio)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - portuguese) [explicit]","avril lavigne - girlfriend (japanese version) (audio)","girlfriend (japanese version - explicit version)","avril lavigne - girlfriend (the submarines\' time warp \'66 mix - japanese) [explicit]","avril lavigne - girlfriend (mandarin version) (audio)","girlfriend (mandarin version - explicit)","avril lavigne -  girlfriend (the submarines\' time warp \'66 mix - mandarin) [explicit]","avril lavigne - losing grip (audio)","complicated","avril lavigne - sk8er boi (audio)","avril lavigne - i\'m with you (audio)","mobile","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","avril lavigne - tomorrow (audio)","avril lavigne - anything but ordinary","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","avril lavigne - nobody\'s fool - let go","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","avril lavigne - head above water (lyric video)","avril lavigne - birdie (lyrics) 🎵","avril lavigne- tell me it\'s over (lyrics) (new single 2018)","dumb blonde (feat. nicki minaj) (audio) - avril lavigne","avril lavigne - alice - audio","avril lavigne - my happy ending (audio)","avril lavigne - take it (audio)","avril lavigne - we are warriors (official audio)","avril lavigne \"rock n roll\" (official audio)","avril lavigne - here\'s to never growing up (audio)","error: this video is not available.","error: this video is not available.","avril lavigne - let me go ft. chad kroeger (official audio)","error: this video is not available.","avril lavigne - bad girl ft. marilyn manson (audio)","avril lavigne - hello kitty (audio)","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","avril lavigne - hush hush (audio)","rock n roll (acoustic)","avril lavigne - how you remind me (audio)","avril lavigne - smile (acoustic version) lyrics video","avril lavigne   losing grip - live (audio) hd/hq","avril lavigne - complicated (the matrix mix)","avril lavigne - girlfriend (dr. luke remix) ft. lil mama","avril lavigne - hot (wolfadelic remix)","avril lavigne - sk8er boi (live acoustic version) from essential mixes (2010) hq","my happy ending (live acoustic version)","take me away (live acoustic version)","avril lavigne - nobody\'s home [live acoustic] (bonus track)","avril lavigne - he wasn\'t (live acoustic)","when you\'re gone (acoustic) - avril lavigne","error: this video is not available.","i fell in love with the devil (radio edit)","avril lavigne - fuel (live)","head above water (feat. we the kings)","error: this video is not available.","error: this video is not available.","avril lavigne - the best damn thing (audio)","avril lavigne - when you\'re gone (audio)","avril lavigne - everything back but you (audio)","avril lavigne - hot (audio)","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","error: this video is not available.","avril lavigne - alone (audio)","avril lavigne - i will be (audio)","i can do better (acoustic version)","take me away","together","avril lavigne - don\'t tell me (audio)","avril lavigne - he wasn\'t (audio)","how does it feel","forgotten","who knows","fall to pieces","freak out","slipped away","i always get what i want","avril lavigne - fly (lyrics on screen)","21 savage & metro boomin - \"run up the racks\"","currensy - audio dope 5 (pilot talk 3)","error: no conn, hlsvp, hlsmanifesturl or url_encoded_fmt_stream_map information found in video info; please report this issue on https://yt-dl.org/bug . make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. be sure to call youtube-dl with the --verbose flag and include its complete output.","currensy - audio dope 5 (pilot talk 3)","french montana - no shopping ft. drake","a$ap rocky - f**kin\' problems (audio) ft. drake, 2 chainz, kendrick lamar","inner life - ain\'t no mountain high enough (whitenoize remix) (cover art)","the greatest showman cast - the greatest show (official audio)","p!nk - a million dreams (from the greatest showman: reimagined) [official audio]","willow sage hart - a million dreams (reprise) [official lyric video]","years & years and jess glynne - come alive (official lyric video)","max & ty dolla $ign - the other side (official lyric video)","kelly clarkson - never enough (from the greatest showman: reimagined) [official lyric video]","kesha - this is me (from the greatest showman soundtrack) [official audio]","rewrite the stars","sara bareilles - tightrope (official lyric video)","from now on","pentatonix - the greatest show (official lyric video)","craig david - come alive (official lyric video)","kesha - this is me (from the greatest showman soundtrack) [official audio]","the greatest showman cast - the greatest show (official audio)","the greatest showman cast - a million dreams (official audio)","a million dreams (reprise)","come alive","the greatest showman cast - the other side (official audio)","never enough","this is me","rewrite the stars","tightrope","the greatest showman cast - never enough (reprise) [official audio]","the greatest showman cast - from now on (official audio)","billie eilish - no time to die (audio)","billie eilish - copycat (sofi tukker remix/audio)","billie eilish - bored (audio)","billie eilish - bellyache (marian hill remix/audio)","billie eilish - everything i wanted (audio)","my future","billie eilish - bitches broken hearts (audio)","billie eilish - xanny (lyrics)","billie eilish - you should see me in a crown (audio)","billie eilish - wish you were gay (audio)","billie eilish - when the party\'s over (audio)","8","my strange addiction","bury a friend","billie eilish - ilomilo (lyrics)","i love you","billie eilish - myboi (troyboi remix/audio)","billie eilish - six feet under (blu j remix)","six feet under (gazzo remix)","billie eilish - six feet under (jerry folk remix)","billie eilish - six feet under (aire atlantica remix)","billie eilish - when i was older (music inspired by the film roma/audio)","six feet under","therefore i am","billie eilish - come out and play (audio)","billie eilish - copycat (audio)","billie eilish - idontwannabeyouanymore (audio)","billie eilish - my boy (audio)","billie eilish - watch (audio)","billie eilish - party favor (audio)","bellyache","ocean eyes","billie eilish - hostage (audio)","billie eilish, vince staples - &burn (audio)","billie eilish - ocean eyes (astronomyy remix)","ocean eyes (blackbear remix)","billie eilish - ocean eyes (goldhouse remix)","billie eilish - ocean eyes (cautious clay remix)","messin my head (mixed)","[full audio] blackpink - (불장난) playing with fire [2nd single album]","[full audio] blackpink - stay [2nd single album]","[full audio] blackpink - whistle (휘파람) (acoustic ver.) [2nd single album]","[full audio] blackpink (블랙핑크) - boombayah (붐바야) [1st single album]","how you like that","blackpink - as if it\'s your last (마지막처럼) [han|rom|eng color coded lyrics]","blackpink - kill this love (color coded lyrics eng/rom/han/가사)","blackpink - boombayah (japanese) [audio]","blackpink – whistle (japanese ver.) (audio)","blackpink - playing with fire [japanese ver.] mp3","blackpink – stay (japanese ver.) (audio)","blackpink - as if it\'s your last [japanese ver.] mp3","blackpink - ddu-du ddu-du  (japanese audio)","blackpink-forever young(japanese ver.) full","blackpink - really  (japanese audio)","blackpink- see u later (japanese ver.) full","error: video unavailable","blackpink - don\'t know what to do (color coded lyrics eng/rom/han/가사)","error: video unavailable","blackpink - 아니길 (hope not) fm/v","ddu-du ddu-du (remix)","blackpink - \'ddu-du ddu-du\' (japanese ver) 日本語/歌詞 (color coded lyrics eng/rom/kan)","error: video unavailable","forever young (live)","stay (remix version)","whistle (live)","you & i + only look at me (live)","solo (live)","really (reggae version)","see u later (live)","playing with fire (live)","boombayah (live)","as if it\'s your last (live)","whistle (remix version)","ddu ddu-du (remix version)","stay (live)","pretty savage","bet you wanna ft. cardi b","lovesick girls","crazy over you","love to hate me","you never know","blackpink - boombayah (japanese ver.) (color coded lyrics)","blackpink (블랙핑크) - whistle (japanese version) (color coded/kan/rom/eng)","blackpink - playing with fire「japanese  ver.」(lyric video)","blackpink (블랙핑크) - \'stay\' (japanese ver.) (color coded lyrics jap/rom/eng)","blackpink -  as if it\'s your last (japanese ver.) (color coded lyrics)","blackpink – whistle (acoustic ver.) (japanese ver.) (audio)","kill this love (japan version)","(1080p hd) blackpink (블랙핑크) - don\'t know what to do (japanese version)","(1080p hd) blackpink (블랙핑크) - kick it (japanese version)","(1080p hd) blackpink (블랙핑크) - hope not (japanese version)","ddu-du ddu-du (remix)","[full audio] blackpink - 뚜두뚜두 (ddu-du ddu-du)","[full audio] blackpink - forever young","really","see u later","kooky chords (mixed)","fall down (mk remix) (mixed)","ricky remedy - road rage (go stoopid) [feat. bok nero]","riot ten & throwdown - act a fool (feat. bok nero) | dim mak records","steve aoki - kolony anthem feat. ilovemakonnen & bok nero (cover art) [ultra music]","bok nero & shizz lo - fvcken greatest","yellow claw - loudest mf (feat. bok nero) [crisis era remix] [out now]","solid (feat. marilyn manson)","boys noize - starwin (official audio)","pegasus","jimmy edgar - shout","warehouse","go on girl","ghettocoder","femme litre","gingy & bordello - all day (robert hood remix)","for these times (original mix)","randomer - meat and dancing","kowton - tfb","anoid (demo version)","craze - selekta (valentino khan remix)","dog blood - chella ride [audio]","tric trac (original mix)","djedjotronic - kaiko","gesaffelstein - aufstand [hq]","luft","wall to wall","work this m.f.","motor","dave clarke - compass","tom rowlands - nothing but pleasure (boys noize pressure fix)","alesia - andrea","maje","boys noize - xtc (chemical brothers remix) (official audio)","spank rock - dtf dadt","space invaders are smoking grass","goldfisch","xtc","apparat - arcadia (boys noize reprise)","brett young — hell yeah damn right (ole miss tribute)","ticket to l.a - brett young (lyrics)","brett young - here tonight(8d audio)","catch","1, 2, 3 mississippi","brett young - let it be mine (audio)","brett young - where you want me (audio)","used to missin’ you","brett young - change your name (lyrics)","brett young ft. gavin degraw - chapters (audio)","brett young - the ship and the bottle (audio)","brett young - reason to stay (lyric video)","brett young - runnin\' away from home (audio)","brett young - don\'t wanna write this song (audio)","brett young - catch (the acoustic sessions)","brett young - chapters (the acoustic sessions) ft. gavin degraw","error: this video is not available.","brett young - sleep without you (official music video)","brett young — sleep without you (lyrics)","brett young - close enough (audio)","brett young - close enough","brett young - like i loved you (official music video)","like i loved you","brett young - in case you didn\'t know (official music video)","[8d audio] in case you didnt know - brett young","brett young - olivia mae","brett young - olivia mae (audio)","brett young - left side of leavin\' (acoustic)","brett young - left side of leaving","brett young - you ain\'t here to kiss me (acoustic)","brett young - you ain\'t here to kiss me (audio)","brett young - back on the wagon (audio)","brett young - back on the wagon","brett young - makin\' me say (audio)","brett young - makin\' me say","brett young - memory won\'t let me (audio)","brett young  - memory won\'t let me (lyrics)","brett young - beautiful believer (audio)","brett young- \"beautiful believer\" (original song)","brett young - mercy (audio)","mercy","brett young - hallelujah (official audio)","brett young - o holy night (static video)","brett young - lady (lyric video)","dear diary,","parasite eve","bring me the horizon - teardrops (official video)","obey","itch for the cure (when will we be free?)","kingslayer","1x1","bring me the horizon - ludens (lyric video)","one day the only butterflies left will be in your chest as you march towards your death","re: they have no reflections","who wants flowers when you\'re dead? nobody","rawwwrr!","drown (new)","steal something.","candy truck / you expected: lab your result: green","a devastating liberation","¿","like seeing spiders running riot on your lover\'s grave","dead dolphin sounds \'aid brain growth in unborn child\' virtual therapy / nature healing 2 hours","bring me the horizon - ±ªþ³§ (feat. yonaka)","anthem","fuck (feat. josh franceschi)","visions","blacklist","memorial","bring me the horizon - \"the fox and the wolf\" (full album stream)","happy song","the comedown","chelsea smile","it was written in blood","bring me the horizon - \"death breath\" (full album stream)","bring me the horizon - \"football season is over\" (full album stream)","sleep with one eye open","bring me the horizon - diamonds aren\'t forever (hq)","the sadness will never end (feat. sam carter)","no need for introductions, i\'ve read about girls like you on the backs of toilet doors","suicide season","no need for introductions, i\'ve read about girls like you on the backs of toilet doors...","pray for plagues","bring me the horizon - \"shadow moses\"","go to hell, for heaven\'s sake","can you feel my heart","sleepwalking","antivist","the house of wolves","empire (let them sing)","and the snakes start to sing","seen it all before","crooked young","hospital for souls","the fox and the wolf (feat. josh scogin)","doomed","throne","true friends"]
    mp3_title =("Perfect Strangers","Sleepwalker","In the Dark","Our Origin","Sundown","Pearl","A Slice of Heaven","Patterns of the Soul (Davey Asprey Remix)","Running for Peace","See You Again (feat. Michele C.)","Open My Mind","Fireflies (feat. Christina Novelli) [Jorn Van Deynhoven Remix]","You & I (Aly & Fila Club Mix)","Fall for You (feat. Lucy Pullin)","D (Don't Go)","Zombie","Northern Star","Light the Way (feat. Kat Marsh) [Bryan Kearney Remix]","Missing (Jorn Van Deynhoven Remix)","Army of Angels","Enough Echo","Coming Home (feat. Bo Bruce) [Standerwick Remix]","Popcorn","Free (feat. Enya Angel)","Till the Sunrise","I Feel Love (Omar Sherif Remix)","Stadium Arcadium","Be in the Moment (ASOT 850 Anthem) [Allen Watts Remix]","Midnight","Music Rescues Me (feat. Plumb)","Rebirth (Ahmed Romel Remix)","Seventh Heaven","Wherever You Are (feat. HALIENE) [Solis & Sean Truby Remix]","Safe from Harm (Giuseppe Ottaviani Remix)","Just as You Are (feat. Fiora)","For the One You Love (feat. Natalie Gioia)","Alone in the Wilderness","Zubr","The Air I Breathe","Activate","Lifting You Higher (ASOT 900 Anthem)","Thirty Three South","I've Been Thinking About You","Take Me There","U","A World Beyond (FSOE550 Anthem)","Disturbance","The Wolf","The Sound of E (Jorn Van Deynhoven Remix)","Ready to Rave","Shock Therapy (Rising Altitude Mix)","A State of Trance Year Mix 2018 (Outro: The Verdict)","A State of Trance Year Mix 2018 (DJ Mix)","Coming Home (feat. Bo Bruce) [Standerwick Remix] [Live]","Sex, Love & Water (feat. Conrad Sewell) [Drym Remix] [Live]","Live at Tomorrowland Belgium 2018 (Highlights) [Intro]","A State of Trance (Intro)","Drowning (feat. Laura V) [Avicii Remix]","Therapy","Mowgli","The Night Sky","Magus","I Believe (feat. Giuseppe De Luca)","Noa","Blue Angel","Till the Sky Falls Down","Rogue","Yalung","Cyclone","I Didn't Know","Something About You","Nightfalls","Alpine","Rambulance","Heaven Will Come (The Noble Six Remix)","A State of Trance (Outro)","Live at Sunburn Festival India 2018 (Intro)","Repeat After Me (Live)","Run Away (Live)","Lifting You Higher (ASOT 900 Anthem) [Live]","Ready to Rave (Live)","Live at Sunburn Festival India 2018 (Outro)","Wild Wild Son (Club Mix)","Zombie","La Résistance De L'Amour (Live) [Mixed]","Another You (feat. Mr. Probz) [Live] [Mixed]","Run Away (Live) [Mixed]","Slipstream","In My Control","Not Techno","Alive","Comet","Flight of the Buzzard","Therapy (feat. James Newman) [Leo Reyes Remix]","Secret Weapon (feat. Sue McLaren)","Stealing Beauty (Daxson Remix)","The Sound of Goodbye","Out of the Sky (feat. Sarah Howells) [Andres Sanchez Remix]","Polarize (Daniel Skyver Remix)","Adam’s Peak","The Air I Breathe","Just a Dream","Inferno","Where the Heart Is","That One Night","In a Thousand Ways (feat. Rykka)","Gods (feat. Nash)","I See Spots","What a Rush","Resistance","Without Kontakt (feat. R-Lend)","Ayo (Mixed)","Nobody's Home","Knockin' on Heaven's Door (Studio Version)","Black Star","What the Hell","Push","Wish You Were Here","Smile","Stop Standing There","I Love You","Everybody Hurts","Not Enough","4 Real","Darlin","Alice (Extended Version)","Remember When","Goodbye","What the Hell (Acoustic Version)","Push (Acoustic Version)","Wish You Were Here (Acoustic Version)","Bad Reputation","What the Hell (Bimbo Jones Remix)","What the Hell (Instrumental)","Wish You Were Here (Instrumental)","Girlfriend (Radio Edit)","Girlfriend","Girlfriend (The Submarines' Time Warp '66 Mix - English)","Girlfriend (Junkie XL Mix)","Girlfriend (French Version - Clean)","Girlfriend (French Version - Explicit)","Girlfriend (The Submarines' Time Warp '66 Mix - French)","Girlfriend (Spanish Version - Clean)","Girlfriend (Spanish Version - Explicit)","Girlfriend (The Submarines' Time Warp '66 Mix - Spanish)","Girlfriend (German Version - Clean)","Girlfriend (German Version - Explicit)","Girlfriend (The Submarines' Time Warp '66 Mix - German)","Girlfriend (Italian Version - Clean)","Girlfriend (Italian Version - Explicit)","Girlfriend (The Submarines' Time Warp '66 Mix - Italian)","Girlfriend (Portugese Version - Clean)","Girlfriend (The Submarines' Time Warp '66 Mix - Portugese)","Girlfriend (Japanese Version - Clean)","Girlfriend (Japanese Version - Explicit Version)","Girlfriend (The Submarines' Time Warp '66 Mix - Japanese)","Girlfriend (Mandarin Version - Clean)","Girlfriend (Mandarin Version - Explicit)","Girlfriend (The Submarines' Time Warp '66 Mix - Mandarin)","Losing Grip","Complicated","Sk8er Boi","I'm with You","Mobile","Unwanted","Tomorrow","Anything but Ordinary","Things I'll Never Say","My World","Nobody's Fool","Too Much to Ask","Naked","Head Above Water","Birdie","Tell Me It's Over","Dumb Blonde (feat. Nicki Minaj)","Alice","My Happy Ending","Take It","We Are Warriors","Rock N Roll","Here's To Never Growing Up","17","Bitchin' Summer","Let Me Go (feat. Chad Kroeger)","Give You What You Like","Bad Girl (feat. Marilyn Manson)","Hello Kitty","You Ain't Seen Nothin' Yet","Sippin' On Sunshine","Hello Heartache","Falling Fast","Hush Hush","Rock N Roll (Acoustic)","How You Remind Me","Smile (Acoustic Version)","Losing Grip (Live)","Complicated (The Matrix Mix)","Girlfriend (feat. Lil Mama) [Dr. Luke Mix]","Hot (Wolfadelic Remix)","Sk8er Boi (Live Acoustic Version)","My Happy Ending (Live Acoustic Version)","Take Me Away (Live Acoustic Version)","Nobody's Home (Live Acoustic Version)","He Wasn't (Live Acoustic Version)","When You're Gone (Acoustic Version)","Girlfriend (Junkie XL Extended Mix)","I Fell In Love With the Devil (Radio Edit)","Fuel (Live)","Head Above Water (feat. We the Kings)","I Can Do Better","Runaway","The Best Damn Thing","When You're Gone","Everything Back But You","Hot","Innocence","I Don't Have to Try","One of Those Girls","Contagious","Keep Holding On","Alone","i will be","I Can Do Better (Acoustic Version)","Take Me Away","Together","Don't Tell Me","he wasn't","How Does It Feel","Forgotten","Who Knows","Fall to Pieces","Freak Out","Slipped Away","I Always Get What I Want","Fly","Run Up the Racks (Mixed)","Audio Dope 5 (Mixed)","No Shopping (Mixed)","Audio Dope 5 (Mix Version)","No Shopping (Mix Version)","F**kin' Problems (Mixed)","Ain't No Mountain High Enough (WhiteNoize Remix) [Mixed]","The Greatest Show","A Million Dreams","A Million Dreams (Reprise)","Come Alive","The Other Side","Never Enough","This Is Me (The Reimagined Remix)","Rewrite the Stars","Tightrope","From Now On","The Greatest Show (Bonus Track)","Come Alive (Bonus Track)","This Is Me","The Greatest Show","A Million Dreams","A Million Dreams (Reprise)","Come Alive","The Other Side","Never Enough","This Is Me","Rewrite the Stars","Tightrope","Never Enough (Reprise)","From Now On","No Time To Die","Copycat (Sofi Tukker Remix)","Bored","Bellyache (Marian Hill Remix)","Everything I Wanted","my future","bitches broken hearts","xanny","you should see me in a crown","wish you were gay","when the party's over","8","my strange addiction","bury a friend","ilomilo","i love you","MyBoi (TroyBoi Remix)","Six Feet Under (BLU J Remix)","Six Feet Under (Gazzo Remix)","Six Feet Under (Jerry Folk Remix)","Six Feet Under (Aire Atlantica Remix)","WHEN I WAS OLDER (Music Inspired by the Film \"ROMA\")","Six Feet Under","Therefore I Am","come out and play","COPYCAT","idontwannabeyouanymore","my boy","watch","party favor","bellyache","ocean eyes","hostage","&burn","Ocean Eyes (Astronomyy Remix)","Ocean Eyes (Blackbear Remix)","Ocean Eyes (GOLDHOUSE Remix)","Ocean Eyes (Cautious Clay Remix)","Messin My Head (Mixed)","PLAYING WITH FIRE","STAY","WHISTLE (Acoustic Ver.)","BOOMBAYAH","How You Like That","As If It's Your Last","Kill This Love","BOOMBAYAH -JP Ver.-","WHISTLE -JP Ver.-","PLAYING WITH FIRE -JP Ver.-","STAY -JP Ver.-","AS IF IT'S YOUR LAST -JP Ver.-","DDU-DU DDU-DU -JP Ver.-","FOREVER YOUNG -JP Ver.-","REALLY -JP Ver.-","SEE U LATER -JP Ver.-","DDU-DU DDU-DU -JP Ver.- (BLACKPINK ARENA TOUR 2018 \"SPECIAL FINAL IN KYOCERA DOME OSAKA\")","Don't Know What To Do","Kick It","Hope Not","DDU-DU DDU-DU (Remix)","DDU-DU DDU-DU (JP Ver.)","DDU-DU DDU-DU (Live)","Forever Young (Live)","STAY (Remix Version) [Live]","WHISTLE (Live)","YOU & I + ONLY LOOK AT ME (Live)","SOLO (Live)","Really (Reggae Version) [Live]","See U Later (Live)","PLAYING WITH FIRE (Live)","BOOMBAYAH (Live)","As If It's Your Last (Live)","WHISTLE (Remix Version) [Live]","DU DDU-DU (Remix Version) [Live]","STAY (Live)","Pretty Savage","Bet You Wanna (feat. Cardi B)","Lovesick Girls","Crazy Over You","Love To Hate Me","You Never Know","BOOMBAYAH (Japanese Version)","WHISTLE (Japanese Version)","PLAYING WITH FIRE (Japanese Version)","STAY (Japanese Version)","As If It's Your Last (Japanese Version)","Whistle (Acoustic Ver.) [Japanese Version]","Kill This Love (Japan Version)","Don't Know What to Do (Japan Version)","Kick It (Japan Version)","Hope Not (Japan Version)","DDU-DU DDU-DU (Remix / Japan Version)","DDU-DU DDU-DU","Forever Young","Really","See U Later","The Return (Mixed)","Fall Down (MK Remix) [Mixed]","Road Rage (Go Stoopid) [feat. Bok Nero] [Mixed]","Act a Fool (feat. Bok Nero) [Mixed]","Kolony Anthem (feat. iLoveMakonnen & Bok Nero) [Mixed]","Fvcken Greatest (Mixed)","Loudest MF (feat. Bok Nero) [Mixed]","Solid (feat. Marilyn Manson)","Starwin","Pegasus","Shout","Warehouse","Go On Girl","Ghettocoder","Femme Litre","All Day (Robert Hood Remix)","For These Times","Meat & Dancing","TFB","Anoid (Demo Version)","Selekta (Valentino Khan Remix)","Chella Ride","Tric Trac","Kaiko","Aufstand","Luft","Wall To Wall","Work This MF","Motor","The Compass","Nothing But Pleasure (Boys Noize Pressure Fix)","Andrea","Maje","XTC (The Chemical Brothers Remix)","DTF DADT (Acapella)","Space Invaders Are Smoking Grass","Goldfisch","XTC (Acapella)","Arcadia (Boys Noize Reprise)","Hell Yeah Damn Right (Ole Miss Tribute)","Ticket to L.A.","Here Tonight","Catch","1, 2, 3 Mississippi","Let It Be Mine","Where You Want Me","Used to Missin’ You","Change Your Name","Chapters (feat. Gavin DeGraw)","The Ship and the Bottle","Reason to Stay","Runnin’ Away from Home","Don’t Wanna Write This Song","Catch (The Acoustic Sessions)","Chapters (feat. Gavin DeGraw) [The Acoustic Sessions]","Ain't Too Proud To Beg","Sleep Without You (Commentary)","Sleep Without You","Close Enough (Commentary)","Close Enough","Like I Loved You (Commentary)","Like I Loved You","In Case You Didn’t Know (Commentary)","In Case You Didn't Know","Olivia Mae (Commentary)","Olivia Mae","Left Side Of Leavin’ (Commentary)","Left Side of Leavin'","You Ain’t Here To Kiss Me (Commentary)","You Ain't Here To Kiss Me","Back On The Wagon (Commentary)","Back On the Wagon","Makin’ Me Say (Commentary)","Makin' Me Say","Memory Won’t Let Me (Commentary)","Memory Won't Let Me","Beautiful Believer (Commentary)","Beautiful Believer","Mercy (Commentary)","Mercy","Hallelujah","O Holy Night","Lady","Dear Diary,","Parasite Eve","Teardrops","Obey (with YUNGBLUD)","Itch for the Cure (When Will We Be Free?)","Kingslayer (feat. BABYMETAL)","1x1 (feat. Nova Twins)","Ludens","One Day the Only Butterflies Left Will Be In Your Chest As You March Towards Your Death (feat. Amy Lee)","Re: They Have No Reflections","Who Wants Flowers When You're Dead? Nobody","Rawwwrr!","Drown","Steal Something.","Candy Truck / You Expected: LAB Your Result: Green","A Devastating Liberation","¿ (feat. Halsey)","\"like seeing spiders running riot on your lover's grave\"","Dead Dolphin Sounds 'aid brain growth in unborn child' Virtual Therapy / Nature Healing 2 Hours (feat. Toriel)","±ªþ³§ (feat. Yonaka)","Anthem","F**k","Visions","Blacklist","Memorial","The  Fox and the Wolf","Happy Song","The Comedown","Chelsea Smile","It Was Written in Blood","Death Breath","Football Season Is Over","Sleep with One Eye Open","Diamonds Aren't Forever","The Sadness Will Never End","No Need for Introductions, I've Read About Girls Like You on the Backs of Toilet Doors","Suicide Season","No Need for Introductions (Benjamin Weinman Remix)","Pray for Plagues","Shadow Moses","Go to Hell, for Heaven's Sake","Can You Feel My Heart","Sleepwalking","Antivist","The House of Wolves","Empire (Let Them Sing)","And the Snakes Start to Sing","Seen It All Before","Crooked Young","Hospital for Souls","The Fox and the Wolf","Doomed","Throne","True Friends")
    for nub,i in enumerate(youtube_title):
        for t in exclusion_list:
            result = re.findall(t, i)
            if result != []:
                print(nub, 0)
                break
            else:
                print(nub, 1)
                break

if __name__ == "__main__":
    strlist_not_in_list()
