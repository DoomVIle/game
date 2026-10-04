image gradient = "gradient.jpg"
image gif = Movie(size=(1920, 1080), play=("images/ripple.webm")) 
default sheknows = False


label start:
    $ quick_menu = False
    scene gif with fade
    o "WELCOME…"
    o "I WAS HOPING TO SEE YOU HERE."
    o "YOUR PRESENCE IS VERY MUCH APPRECIATED."
    o "HERE IS A QUESTION FOR YOU:"
    o "DO YOU KNOW WHAT DAY IT IS?"
    menu:
        "i know":
            jump know
        "are we talking about the same thing?":
            jump unsure


label know:

    o "SPLENDID."
    o "ABSOLUTELY… SPLENDID."
    o "BUT MY MANNERS, WHERE ARE THEY…"
    o "CONGRATULATIONS ON YOUR MILESTONE."
    o "AND BY THAT I MEAN…"
    o "YOUR BIRTHDAY, RAMONA."
    o "BUT TODAY…"
    o "I WILL GRANT YOU MY GREATEST GIFT."
    o "JUST FOR TODAY…"
    o "YOU CAN NAME YOURSELF."

    menu:
        "i already did that ima tranny":
            jump damn


label damn:

    quicko "yeah ok girl but like bare with me won't you"
    quicko "i wanna be ominous and shit"
    quicko "whatever"
    quicko "just put spice then"
    quicko "or whatever i don't even gaf a dfuck"
    $ sheknows = True
    jump namingcheck


label unsure:

    o "BUT OF COURSE."
    o "NO MATTER WHAT DAY IT IS…"
    o "YOUR LIFE… IT IS TRULY SOMETHING TO CHERISH."
    o "LIFE… A FLEETING MOMENT ON EARTH."
    o "WE ALL RETURN TO DUST IN THE END."
    o "DON'T YOU AGREE, RAMONA?"
    menu:
        "what the fuck i'm so fuckibg scared right now":
            jump dw


label dw:

    o "THERE'S NO NEED TO BE."
    o "AFTER ALL…"
    o "WE ARE CELEBRATING."
    o "HAPPY BIRTHDAY, RAMONA."
    o "AND, OF COURSE."
    o "WHAT'S A BIRTHDAY WITHOUT A GIFT?"
    o "FOR YOUR BIRTHDAY, I WILL GRANT YOU A TRULY, TRULY PRECIOUS GIFT."
    o "THE GIFT OF AUTONOMY."
    o "GO AHEAD… AND NAME YOURSELF."

    jump namingcheck

label namingcheck: # Menacing name section
    $ quick_menu = True
    $ persistent.fake_menu = False
    $ povname =renpy.input("Input your name...", length=32)
    if povname.lower() in ["gaymore"]:
        gay "That's... not my name"
        jump namingcheck
    elif povname.lower() in ["epiphany"]:
        e "...........n.......No?!"
        jump namingcheck
    elif povname.lower() in ["gary"]:
        ga "He's more of a lil' bro to me, y'know.... Dont' tell him i said that."
        jump namingcheck
    elif povname.lower() in ["dante","mass"]:
        $ renpy.quit()
    elif povname.lower() in ["serene"]:
        s "Isn't he like, 12?"
        jump namingcheck
    elif povname.lower() in ["artie", "artemis"]:
        a "can he get me boba"
        jump namingcheck
    elif povname.lower() in["kernel ryan","ryan","ryder"]:
        r "i'm going to fucking kill you"
        jump namingcheck
    elif povname.lower() in["ramune","mune"]:
        m "it's too early for that"
        jump namingcheck
    elif povname.lower() in["vile"]:
        v "i don't enforce it but i prefer m-"
        "*gets sprayed with water*"
        v "hey."
        jump namingcheck
    elif povname.lower() in["batty"]:
        b "EWWWW A CHUD"
        jump namingcheck
    elif povname.lower() in["dee","loreraider","raider"]:
        d "*rubs hand together* my niche goonrods"
        jump namingcheck
    elif povname.lower() in["fio","fiorello"]:
        f "if i did that this game would be R rated"
        jump namingcheck
    elif povname.lower() in["underscores","april"]:
        u "i just can't do it, i'm married to the music"
        jump namingcheck
    elif povname.lower() in["ninajirachi","nina"]:
        n "my computer better"
        jump namingcheck
    elif povname.lower() in["pinkpantheress","pink"]:
        pp "haha yeah it's totally me you can be my american ah ah boy paypal me 5 dollars now"
        jump namingcheck
    elif povname.lower() in["porter","porter robinson"]:
        pr "i fucking HATE chileans"
        jump namingcheck
    elif povname.lower() in["madeon"]:
        ma "i fucking HATE porter robinson"
        jump namingcheck
    elif povname.lower() in["jamie","jamie paige"]:
        j "dude i really wish i could eat raw red meat rn"
        jump namingcheck
    elif povname.lower() in ["kasane teto", "teto", "kasane"]:
        k "https://youtu.be/F6q8MR1Iz6M?si=s_FWVINyfrl7iATi"
        jump namingcheck
    if sheknows:
        jump namechoose2 
    else:
        jump namechoose1
    
label namechoose1:

    o "[povname]"
    o "WHAT A WONDERFUL NAME."
    o "DON'T FORGET"
    o "…IT."
    o "AND BY IT, LET'S JUST SAY."
    o "uh"
    quicko "IDK"
    quicko "oh yea this is a dating sim btw"
    quicko "the guy SUCKS so good luck i guess BYE"

    jump datestart


label namechoose2:

    quicko "ok"
    quicko "yay"
    quicko "by the way this is a dating sim and the guy sucks so good luck i guess BYEEEE"
    jump datestart


label datestart:

    scene bg door with fade
    show gianni normal at left with dissolve
    g "Oh!"
    g "Hi! What's up?"
    g "You were getting me real worried"
    "You frown."
    povname "guh... i took the wrong fucking bus that's why"
    g "Ah shit, don't sweat it"
    povname "no wait uh"
    povname "i then took the right one"
    g "Mhm?"
    povname "I SWEAR it was the right one"
    povname "but"
    povname "for some reason it just took a completely different route"
    povname "i thought there was a roadblock or some shit"
    povname "but it just"
    povname "kept fucking going"
    povname "had to walk all the way anyway"
    povname "fuck my stupid tranny life"
    g "wOAH-"
    povname "I CAN SAY IT I CAN SAY IT I CAN SAY IT"
    g "Oh thank god"
    " "
    g "No shit I obviously figured"
    povname "ERM???"
    g "BY THAT I MEAN,"
    g "You don't seem like the type of girl to be saying slurs she shouldn't"
    g "....And for no reason"
    g "Nothing more or less"
    povname "yeah nice save loser"
    povname "did your MOM give it to you"
    " "
    povname "I am so sorry."
    g "I... I........"
    g "Aha nah it's chill"
    g "Never met her"
    g "But hey! Now we're equally offended"
    g "Care to come in?"
    povname "hmmm"
    povname "idk man what you said was pretty fucked up y'know"
    povname "you BASICALLY told me i don't pass"
    g "WHAT-"
    povname "AND that you want me to die."
    g "oh my god bruh"
    povname "AND that i'm too fat"
    g "Okay. Okay. You know what"
    g "I see you"
    g "You're... hurt."
    g "But at least come in so I can..."
    g "Keep The Peace with you?"
    povname " "
    povname "um"
    g "was that not an underscores song"
    povname "yeah"
    povname "i fucking LOVE that song"
    g "Phew"
    povname "why :eyes: :eyes: did you listen to her :eyes: :eyes: :eyes:"
    g "Ahem"
    g "I don't play about white girl pop"
    g "........................I don't play about getting cold either. Can you come in?"
    povname "IDK"
    g ":pleading_face:"
    povname "ugh i GUESS i'll come in then"
    g "yaaayyyy ^-^"
    povname "grownass man btw"

