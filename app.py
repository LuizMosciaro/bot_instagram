from instapy import InstaPy

session = InstaPy(username='*****', password='********',headless_browser=False)

#likes
session.set_do_like(enabled=True, percentage=100)
#likeconfigs
session.set_delimit_liking(enabled=True, max_likes=500, min_likes=75)
session.like_by_tags(['manaus','amazonas','manausamazonas','manauscity','amazonia',
                        'makeup','manausam','natureza'])

#naolikes
session.dont_like('homem','policial','man','men','homens','modamasculina','brasil','homem','boy' ,
            'boys' ,'beleza' ,'homensestilosos','homenslindos' ,'barba' ,'a' ,'masculino' ,'homemmoderno' ,
            'instagood' ,'style' ,'estilomasculino' ,'fitness' ,'saopaulo','macho','alfa','instaboy','likesforlikes',
            'top','fy','top','riodejaneiro','sex', 'nude', 'naked','hunt', 'gun', 'shoot', 'slaughter', 'pussy')


#comentarios
session.set_do_comment(enabled=True,percentage=35)
session.set_comments([u'Legal!','=)',u'😊','Uau legal',u'😊😊',u'Uau 😊', u'👏👏',u'💁🏽',u'🔥🔥🔥',u'✨✨✨',u'✨'])
session.set_delimit_commenting(enabled=True, max_comments=100, min_comments=10)
session.set_smart_location_hashtags(['213998268/manaus-brazil'],radius=50)

#supervisor
session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes_h","likes_d", "comments_d", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            notify_me=True,
                            peak_likes_hourly=57,
                            peak_likes_daily=600,
                            peak_comments_hourly=70,
                            peak_comments_daily=300,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)

#skips
session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100,
                       skip_business=False,
                       skip_non_business=False,
                       business_percentage=100)

#perfil do insta
session.set_relationship_bounds(enabled=True,
                                potency_ratio=1.5,
                                delimit_by_numbers=True,
                                max_followers=8000,
                                max_following=2000,
                                min_followers=500,
                                min_following=200,
                                min_posts=100)

