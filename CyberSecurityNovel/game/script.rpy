init:
    $ talked_with = list()
    $ endingType = "none"

# Определение персонажей игры.
define arseniy = Character('Арсений', color="#c8ffc8")
define lena = Character('Лена', color="#49a812", image="lena")
define zhenya = Character('Женя', color="#068c9e", image="zhenya")
define kirill = Character('Кирилл (0xDeAdBeEf)', color="#deadbeef", image="kirill")

image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

# ai generated
image room_bg = "bg/room.jpg"
image classroom_bg = "bg/classroom.png"
image school_bg = "bg/school.png"
image supermarket_bg = "bg/supermarket.png"
image cafe_bg = "bg/cafe.png"
image medical_university = "bg/medical_university.png"
# ai generated

# https://uploads.worldanvil.com/uploads/images/85148b6a1cd86a311695e1d837f39dc9.JPG
image investigation = "bg/investigation.png"

#https://upload.wikimedia.org/wikipedia/commons/0/02/%D0%98%D0%A0%D0%98%D0%A2-%D0%A0%D0%A2%D0%A4_%D0%A3%D1%80%D0%A4%D0%A3_%D0%B2_%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%D0%B5_%D0%B2%D0%B5%D1%87%D0%B5%D1%80%D0%BE%D0%BC_05.03.2023.jpg
image irit_rtf = "bg/irit_rtf.png"

# ai generated
image lena listening:
    "lena/lena_default.png"
image lena talking:
    "lena/lena_mouth_open.png"

image zhenya listening:
    "zhenya/zhenya_default2.png"
image zhenya talking:
    "zhenya/zhenya_mouth_open2.png"

image kirill listening:
    "kirill/kirill_default.png"
# ai generated

# Игра начинается здесь:
label start:
    $ talked_with = list()
    scene black
    scene room_bg with dissolve

    play sound "home_ambient.mp3" loop fadein 0.5 volume 0.75

    "*Арсений проснулся со странным ощущением паники*"
    "*Посмотрев на часы, он убедился, что не проспал уроки, но спокойнее от этого не стало*"

    menu sleep_or_continue_menu:
        "Что бы сделать"
        "Спать дальше":
            scene black with dissolve
            "Арсений лёг дальше спать, а вы так и не узнаете, что же его так тревожило"
            return
        "Понять причину его паники":
            jump main

label main:
    "*Дальше уснуть так и не удалось, да и не хотелось, потому что Арсения не отпускали мысли о собственном будущем*"

    arseniy "Угораздило же меня в пять утра проснуться..."
    arseniy "Мало того, теперь только и думаю о том, кем бы мне стать"
    arseniy "Я же одиннадцатый класс скоро закончу, а так и не придумал чем по жизни заниматься стану"

    arseniy "Даже не знаю что и выбрать.."
    arseniy "Родители меня вообще на медицинское думают отправить"
    arseniy "А я хочу пойти в айти сферу, но там такой выбор, да и ажиотаж огромный..."
    arseniy "Я ведь много чего умею.. наверное. Вот вроде всё, а вроде и ничего.. немного кодить на Python умею, всё таки мне ЕГЭ по информатике сдавать"
    arseniy "Фу, экзамены, ещё об этом сейчас не хватало думать"
    arseniy "Лучше всего конечно у меня получается видео всякие по компьютерной тематике смотреть.. и фильмы.. Да, точно!"

    stop sound fadeout 0.5
    scene black with dissolve

    # https://www.youtube.com/watch?v=U6A7Iv0RbdA
    play movie "hacker_screen.webm" loop
    show movie with dissolve:
        blur 8

    arseniy "Обожаю всякие фильмы про крутых хакеров"
    play sound "typing_sound.ogg" fadein 1.0 fadeout 1.0
    arseniy "Они такие клац клац и бам.."
    
    stop sound fadeout 1.0
    
    #https://www.shutterstock.com/shutterstock/videos/1070890183/thumb/1.jpg?ip=x480
    show image "other/access_granted.webp" at truecenter
    
    arseniy "Большими буквами на весь экран написано \"Access Granted\""

    hide image "other/access_granted.webp"
    stop movie
    hide movie with dissolve
    scene room_bg with dissolve
    "*Воображать можно бесконечно, но тут произошло неизбежное..*"

    #https://www.myinstants.com/media/sounds/alarm_clock.mp3
    play sound "alarm_clock.mp3" fadein 1.0 fadeout 1.0 volume 0.75
    
    "*Прозвенел будильник, а значит пора собираться в школу...*"
    stop sound fadeout 1.0
    scene black with dissolve

    scene classroom_bg with dissolve:
        blur 8
    #https://pixabay.com/
    play sound "classroom_ambient.mp3" loop fadein 1.0
    arseniy "Пустовато тут, хотя чему я удивляюсь"
    arseniy "Вечно все опаздывают"

    "*В класс зашла Лена, хорошая подруга Арсения*"

    show lena talking with dissolve
    lena talking "Приветик, Сеня!"
    lena talking "Чего такой задумчивый?"

    menu talk_with_lena_or_skip:
        "Что ответить"
        "Мысли о будущем не покидают меня":
            jump lena_route
        "Всё нормально, давай потом поговорим":
            show lena listening with dissolve
            arseniy "Всё нормально, не выспался просто, лучше потом поговорим"
            lena talking "Ну ладненько, если что приходи в кофейню ко мне, у меня смена сегодня"
            hide lena talking with dissolve
    
    jump after_school


label lena_route:
    $ talked_with.append("lena")
    
    if renpy.showing("room_bg"):
        arseniy "Схожу-ка я к Лене на работу, она как раз на смене"
        scene black with dissolve
        scene cafe_bg with dissolve:
            blur 8
        
        play sound "cafe_ambient.mp3" volume 0.5

        show lena talking with dissolve
        lena talking "Ой, Сеня, ты всё таки пришел! Рассказывай давай что случилось, ты прям сам не свой."
    
    show lena listening with dissolve
    
    arseniy "Никак не могу определиться с профессией"
    
    lena talking "Я тоже в последнее время часто об этом думаю"
    lena talking "Вроде и на дизайн хочу пойти, не зря же на художку столько лет потратила"
    lena talking "Но я уже почти год верстаю странички для сайтов и мне очень нравится идея на прикладную информатику пойти, потом веб дизайнером работать буду"
    lena talking "А ты из чего выбираешь?"

    show lena listening with dissolve

    if "zhenya" in talked_with:
        if "kirill" in talked_with:
            arseniy "Я поговорил с Женей и со знакомым хакером Кириллом"
            arseniy "Один предложил пойти на информационную безопасность, другой позвал к ним работать"
            arseniy "Выбираю так сказать между добром и злом ха-ха"
            arseniy "Учиться долго слишком, а у Кирилла сразу работа. Денег много можно поднимать"
            lena talking "А это не опасно? Когда нибудь же вас обязательно раскроют"
            show lena listening with dissolve
            if talked_with.index("zhenya") > talked_with.index("kirill"):
                arseniy "Кирилл мне рассказал как они остаются не пойманными, звучит вполне убедительно, должно работать"
                lena talking "Мне конечно эта затея не очень нравится, но тебе наверное виднее"
            else:
                arseniy "Женя рассказал мне про несколько случаев, когда хакеров ловили, после этого я призадумался, но большие доходы перебивают страх"
            hide lena with dissolve
            "*Ещё немного мило побеседовав с Леной, герой отправился обратно домой*"
        else:
            arseniy "Я поговорил с Женей"
            arseniy "Он предложил пойти на информационную безопасность"
            lena talking "Звучит интересно! Так ещё и специальность очень востребованная!"
            lena talking "Будешь сайтики мои на уязвимости проверять хи-хи"
            show lena listening with dissolve
            arseniy "Обязательно!"
            $ endingType = "good"
    elif "kirill" in talked_with:
        arseniy "Я поговорил со знакомым хакером Кириллом"
        arseniy "Он позвал меня к ним работать"
        arseniy "Учиться даже не надо, сразу работа считай. Денег много можно поднимать"
        lena talking "А это не опасно? Когда нибудь же вас обязательно раскроют"
        show lena listening with dissolve
        arseniy "Нет конечно, поймают только если быть неосторожным"
        lena talking "Мне это не кажется хорошей идеей... но как знаешь"
        show lena listening with dissolve
        $ endingType = "bad"
    else:
        arseniy "Да вот даже не знаю, технических направлений слишком много"
        lena talking "Может тогда на прикладную информатику поступишь? Вместе учиться будем, круто же"
        lena talking "Там всего понемногу, во время учебы и определишься"
        show lena listening with dissolve
        arseniy "Может ты и права, но я пожалуй ещё подумаю"
        $ endingType = "neutral"
    hide lena with dissolve
    if renpy.showing("cafe_bg"):
        "*Ещё немного мило побеседовав с Леной, герой отправился обратно домой*"
        jump home_after_school
    else: 
        jump after_school

label after_school:
    "*Вот так прошел урок за уроком*"

    stop sound fadeout 0.5

    scene black with dissolve
    scene school_bg with dissolve:
        blur 8

    #https://pixabay.com/
    play sound "street_ambient.mp3" fadein 0.5 volume 0.5
    "*Арсений пошел домой*"
    
    scene supermarket_bg with dissolve:
        blur 8
    arseniy "Женяяяя!!!"
    show zhenya listening with dissolve
    "*Из супермаркета выходил Женя, ребенок из семьи, с которой хорошо общались родители нашего героя*"
    "*Женя уже год как закончил школу, Арсений относится к нему как к старшему брату*"

    zhenya talking "Ого, какие люди!"
    zhenya talking "Ну и давненько же мы не виделись, как дела, как сам? Рассказывай"

    show zhenya listening with dissolve

    menu talk_with_zhenya_or_skip:
        "Что сказать?"
        "Быстро ответить и пойти домой":
            arseniy "Да всё как обычно, со школы вот иду, хочу поскорее домой"
            zhenya talking "А, хорошо, в таком случае не буду задерживать, обязательно потом пообщаемся! До скорого!"
            jump home_after_school
        "Спросить совета":
            jump zhenya_route

label zhenya_route:
    $ talked_with.append("zhenya")
    show zhenya listening with dissolve
    arseniy "Я всё никак не могу выбрать куда поступать"
    zhenya talking "А чего сложного то? Я увидел направление с искусственным интеллектом, почти ничего не знал, но думаю перспективное направление, туда и поступил."
    zhenya talking "Сначала ничего не понимал, а сейчас уже проекты вот делаю, деньги неплохие зарабатываю."

    show zhenya listening with dissolve
    if "lena" in talked_with:
        if "kirill" in talked_with:
            arseniy "А я вот с Леной и Кириллом поговорил, она предложила на прикладную поступить, а Кирилл к себе меня позвал, предложил бросить идею учиться"
            arseniy "Притом аргументы у него железные, денег много, от родителей съеду, как давно уже хочу"
            zhenya talking "Вот недавно только наши спецы большую операцию устроили, отловили пару хакерских группировок, а там такие же школьники как ты"
            zhenya talking "Бросай лучше эту идею, доберутся органы до тебя быстро и всё, видеться только через стекло будем, а общаться по телефону"
            show zhenya listening with dissolve
            arseniy "А что предложишь тогда?"
            zhenya talking "Иди на информационную безопасность, будешь такими же взломами заниматься, только легально, по заказу компаний"
            zhenya talking "У меня пара знакомых там учатся, один работает уже"
            zhenya talking "Такой же гик как ты, и доволен как слон, работы много, но она интересная. Сидит там сети на признаки необычной активности мониторит, иногда на выезды катается, проверяет сети филиалов на уязвимости."
            zhenya talking "Не заскучаешь там короче"
            show zhenya listening with dissolve
            arseniy "Спасибо тебе за предложение, мне нравится, пойду родителям расскажу!"
            $ endingType = "good"
        else:
            arseniy "С Леной поговорил, она предложила на прикладную поступить"
            zhenya talking "Ну вот, хорошая же идея"
            show zhenya listening with dissolve
            arseniy "Вообще-то да, но чего то определенного хочется.. а прикладная информатика это как то расплывчато"
            zhenya talking "Ты же по хакерам фанатеешь?"
            show zhenya listening with dissolve
            arseniy "Нуууу... да.."
            zhenya talking "Может тогда на информационную безопасность пойдешь? У меня пара знакомых там учатся, один работает уже"
            zhenya talking "Такой же гик как ты, и доволен как слон, работы много, но она интересная. Сидит там сети на признаки необычной активности мониторит, иногда на выезды катается, проверяет сети филиалов на уязвимости."
            zhenya talking "Не заскучаешь там короче"
            show zhenya listening with dissolve
            arseniy "Спасибо тебе за предложение, это определенно лучше прикладной информатики, пойду родителям расскажу!"
            $ endingType = "good"
    elif "kirill" in talked_with:
            arseniy "А я вот с Кириллом поговорил, он к себе меня позвал, сказал бросать идею учиться"
            arseniy "Притом аргументы у него железные, денег много, от родителей съеду, как давно уже хочу"
            zhenya talking "Бросай лучше эту идею, доберутся органы до тебя быстро и всё, видеться только через стекло будем, а общаться по телефону"
            show zhenya listening with dissolve
            arseniy "А что предложишь тогда?"
            zhenya talking "Иди на информационную безопасность, будешь против хакеров работать."
            zhenya talking "У меня пара знакомых там учатся, а один работает уже"
            zhenya talking "Такой же гик как ты, и доволен как слон, работы много, но она интересная. Сидит там сети на признаки необычной активности мониторит, иногда на выезды катается, проверяет сети филиалов на уязвимости."
            zhenya talking "Не заскучаешь там короче"
            show zhenya listening with dissolve
            arseniy "Спасибо тебе за предложение, мне нравится, пойду родителям расскажу!"
            $ endingType = "good"
    else:
        arseniy "К тебе первому вот обращаюсь, может чего предложишь"
        zhenya talking "Приходи ко мне на ИИ-шное направление, может понравится"
        show zhenya listening with dissolve
        arseniy "Нет уж, спасибо. Этот искусственный интеллект это один большой пузырь, который скоро лопнет."
        zhenya talking "Круто ты конечно о моем выборе отозвался.. Ну допустим, чего там тебе нравится то вообще?"
        zhenya talking "Ты же по хакерам фанатеешь?"
        show zhenya listening with dissolve
        arseniy "Нуууу... да.."
        zhenya talking "Может тогда на информационную безопасность пойдешь? У меня пара знакомых там учатся, один работает уже"
        zhenya talking "Такой же гик как ты, и доволен как слон, работы много, но она интересная. Сидит там сети на признаки необычной активности мониторит, иногда на выезды катается, проверяет сети филиалов на уязвимости."
        zhenya talking "Не заскучаешь там короче"
        show zhenya listening with dissolve
        arseniy "Хорошее предложение, но мне надо бы ещё подумать.."
    
    hide zhenya with dissolve
    jump home_after_school

label kirill_route:
    $ talked_with.append("kirill")
    "*Кирилл очень переживает за свою анонимность и общается только через защищённный мессенджер*"

    show kirill listening

    #https://www.myinstants.com/media/sounds/message-sent.mp3
    play sound "message_sent.mp3"
    arseniy "Я всё никак не могу определиться с тем, что бы мне после школы делать"

    if "lena" in talked_with:
        if "zhenya" in talked_with:
            arseniy "Но поговорил с друзьями, теперь думаю на информационную безопасность пойти учиться"
            #https://www.myinstants.com/media/sounds/telegram-notification.mp3
            play sound "notification.mp3"
            kirill "Странный ты, умный ведь, шаришь за компы, приходи к нам! Зачем тебе этот университет, четыре года жизни минимум потеряешь, так еще и против нас бороться будешь"
            kirill "А ведь команда у нас отличная, все свои, всё безопасно"
            play sound "message_sent.mp3"
            arseniy "Заманчивое предложение, но вот опасаюсь что поймают нас рано или поздно"
            arseniy "Ещё и перспектива остаться без образования мне как то не нравится"
            play sound "notification.mp3"
            kirill "Какой ты неженка! Надоумили тебе друзья это образование.. бред это всё"
            kirill "Подставки под чай лучше диплома не придумал? У тебя и так аттестат есть, скоро второй появится"
            play sound "message_sent.mp3"
            arseniy "Какой то ты агрессивный сегодня, ладно, спишемся еще"
        else:
            pass
    elif "zhenya" in talked_with:
            arseniy "Но поговорил с другом, он предложил на информационную безопасность пойти учиться"
            arseniy "Интересная работа оказывается"
            play sound "notification.mp3"
            kirill "Странный ты, умный ведь, шаришь за компы, приходи к нам! Зачем тебе этот университет, четыре года жизни минимум потеряешь, так еще и против нас бороться будешь"
            kirill "А ведь команда у нас отличная, все свои, всё безопасно"
            play sound "message_sent.mp3"
            arseniy "Заманчивое предложение, но вот опасаюсь что поймают нас рано или поздно"
            arseniy "Ещё и перспектива остаться без образования мне как то не нравится"
            play sound "notification.mp3"
            kirill "Какой ты неженка! Надоумил тебе этот идиот про образование.. бред это всё"
            kirill "Подставки под чай лучше диплома не придумал? У тебя и так аттестат есть, скоро второй появится"
            play sound "message_sent.mp3"
            arseniy "Какой то ты агрессивный сегодня, ладно, спишемся еще"
    else:
        play sound "notification.mp3"
        kirill "Да чего тут думать, ты же умный, шаришь за компы, приходи к нам! Зачем тебе этот университет, четыре года жизни минимум потеряешь"
        kirill "Команда у нас хорошая, все свои, всё безопасно"
        play sound "message_sent.mp3"
        arseniy "Заманчивое предложение, но вот опасаюсь что поймают нас рано или поздно"
        arseniy "Ещё и перспектива остаться без образования мне как то не нравится"
        play sound "notification.mp3"
        kirill "Нормально всё будет, мы через туннели сидим, шифрование повсюду, не поймают если сам себя не выдашь"
        kirill "А диплом зачем тебе, подставки под чай лучше не придумал?"
        play sound "notification.mp3"
        kirill "Сейчас столько возможностей, прогресс идет, а люди так и не поняли, что доверять всем не стоит"
        kirill "Зарабатываем самые большие деньги за всё время работы, накопишь столько, что до старости хватит."
        kirill "Да и от предков съедешь наконец, круто же."
        play sound "message_sent.mp3"
        arseniy "Круто конечно, я обдумаю и напишу потом"
        $ endingType = "bad"
    jump home_after_school

label home_after_school:
    stop sound fadeout 0.5

    #https://pixabay.com/
    play sound "home_ambient.mp3" loop fadein 0.5 volume 0.75

    if len(talked_with) == 3:
        jump ending

    scene black with dissolve
    scene room_bg with dissolve

    if not renpy.showing("room_bg"):
        "*Вернувшись домой героя так и не отпускала тревога*"

    menu talk_with_someone:
        "С кем поговорить?"
        "С Женей" if (not "zhenya" in talked_with):
            "*Арсений позвонил Жене и пригласил его в гости, пообщаться*"
            jump zhenya_route
        "С Кириллом" if (not "kirill" in talked_with):
            jump kirill_route
        "С Леной" if (not "lena" in talked_with):
            jump lena_route
        "Определиться уже с выбором" if len(talked_with) > 0:
            jump ending

label ending:
    stop sound fadeout 0.5
    scene black with dissolve

    if endingType == "bad":
        stop music fadeout 0.5
        play music "bad_ending.mp3" fadein 0.5 loop volume 0.75
        "Переместимся на пару лет вперед..."
        
        play movie "hacker_bg.webm" loop
        show movie with dissolve:
            blur 32
        "Арсений повёлся на обещания Кирилла и стал работать на хакерскую группировку"
        "Но ни к чему хорошему это, конечно, не привело"
        stop movie
        hide movie with dissolve
        scene investigation with dissolve:
            blur 8
        "Как и все преступники, киберпреступники рано или поздно окажутся за решеткой за противоправные деяния"
        "Наш Арсений - не исключение, его группировка взломала государственные серверы и продавала секретную информацию"
        "Нашему герою определенно нужно было услышать правильный совет от человека, на которого он ровняется"
        "Теперь вряд ли мы увидим Сеню в ближайшие годы... Не повторяйте его ошибок!"
    elif endingType == "good":
        scene irit_rtf with dissolve:
            blur 32
        "Арсений послушал совет Жени и уже учится на направлении информационной безопасности в УрФУ"
        "Теперь его ждут четыре года интересного обучения!"
    elif endingType == "neutral":
        scene irit_rtf with dissolve:
            blur 32
        show lena listening with dissolve
        "Арсений решил, что было бы здорово пойти учиться вместе с Леной, они поступили на прикладную информатику"
        hide lena listening with dissolve
    else:
        scene supermarket_bg with dissolve:
            blur 16
        "Никакая концовка, родители отправили на врача"
    
    scene black with dissolve
    stop sound fadeout 0.5
    stop music fadeout 0.5
    "Спасибо за прохождение! Попробуйте ещё раз, чтобы получить разные диалоги"