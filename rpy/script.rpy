define college_girl = Character("女大")

init:
    image background = im.Scale("background.png", config.screen_width, config.screen_height)
    

default girl_affection = 0

init python:
    style.create("affection_text", "default")
    style.affection_text.font = "a.ttf" 
    style.affection_text.size = 30
    style.affection_text.color = "#ffffff"
    style.affection_text.outlines = [(2, "#FFC0CB", 0, 0)]


screen affection_display():
    text "女大好感度: [girl_affection]" style "affection_text" align (0.01, 0.01)

# label start:
#     show screen affection_display
#     $ renpy.movie_cutscene("videos/1-1.webm")
#     show screen affection_display

#     $ renpy.movie_cutscene("videos/1-2.webm")
#     show screen affection_display

#     $ renpy.movie_cutscene("videos/1-3.webm")
#     show screen affection_display

#     menu:
#         "开门":
#             $ renpy.movie_cutscene("videos/1-3-1.webm")
#             show screen affection_display

#         "询问":
#             $ renpy.movie_cutscene("videos/1-3-2.webm")
#             show screen affection_display

#     $ renpy.movie_cutscene("videos/1-4.webm")
#     show screen affection_display

#     return

label splashscreen:
    show logo at truecenter with Dissolve(2.0)
    $ renpy.pause(0.5, hard=True)
    pause 1.0
    hide logo with Dissolve(2.0)
    $ renpy.pause(0.5, hard=True)
    return

label before_main_menu:
    $ renpy.movie_cutscene("videos/0.webm")
    $ renpy.pause(0.5, hard=True)
    return

# label main_menu:
#     return


label start:

    show screen affection_display
    $ renpy.call_in_new_context("play_movie", "videos/1-1.webm")

    show screen affection_display
    $ renpy.call_in_new_context("play_movie", "videos/1-2.webm")

    show screen affection_display
    $ renpy.call_in_new_context("play_movie", "videos/1-3.webm")

    menu:
        "开门":
            show screen affection_display
            $ renpy.call_in_new_context("play_movie", "videos/1-3-1.webm")

        "询问":
            show screen affection_display
            $ renpy.call_in_new_context("play_movie", "videos/1-3-2.webm")

    show screen affection_display
    $ renpy.call_in_new_context("play_movie", "videos/1-4.webm")

    return

label play_movie(movie):
    $ renpy.movie_cutscene(movie)
    return

