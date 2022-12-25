from transitions.extensions import GraphMachine

from utils import send_flex_message, send_text_message
import api
import json

cur_movie = {}

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_now_playing(self, event):
        text = event.message.text
        return text.lower() == "now playing"

    def is_going_to_popular(self, event):
        text = event.message.text
        return text.lower() == "popular"

    def is_going_to_top_rated(self, event):
        text = event.message.text
        return text.lower() == "top rated"

    def is_going_to_upcoming(self, event):
        text = event.message.text
        return text.lower() == "upcoming"

    def is_going_to_overview(self, event):
        text = event.message.text
        cur_movie[event.source.user_id] = text
        return True
    
    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_menu(self, event):
        Message = json.load(open('main_menu.json', 'r', encoding='utf-8'))
        reply_token = event.reply_token
        send_flex_message(reply_token, "open menu", Message)
        #send_text_message(reply_token, "8787878787")

    def on_enter_now_playing(self, event):
        temp = json.load(open('view_movie.json', 'r', encoding='utf-8'))
        data = api.get_now_playing()
        reply_token = event.reply_token
        for i in range(0, 5):
        #i = 0
            temp['contents'][i]['hero']['url'] = 'https://image.tmdb.org/t/p/w500' + data[i][6]
            temp['contents'][i]['body']['contents'][0]['text'] = str(data[i][0])
            temp['contents'][i]['footer']['contents'][0]['text'] += (': ' +  str(data[i][1]))
            temp['contents'][i]['footer']['contents'][1]['text'] += (': ' + str(data[i][2]))
            temp['contents'][i]['footer']['contents'][2]['text'] += (': ' + str(data[i][3]))
            temp['contents'][i]['footer']['contents'][3]['text'] += (': ' + str(data[i][4]))
            temp['contents'][i]['footer']['contents'][4]['action']['text'] = str(data[i][0])
        
        send_flex_message(reply_token, "now_playing", temp)

    def on_enter_overview(self, event):
        overview = ""
        reply_token = event.reply_token

        data = api.get_now_playing()
        for movie in data:
            if movie[0] == cur_movie[event.source.user_id] and overview == "":
                overview = movie[5]
                break
        
        data = api.get_now_playing()
        for movie in data:
            if movie[0] == cur_movie[event.source.user_id] and overview == "":
                overview = movie[5]
                break

        data = api.get_top_rated()
        for movie in data:
            if movie[0] == cur_movie[event.source.user_id] and overview == "":
                overview = movie[5]
                break

        data = api.get_upcoming()
        for movie in data:
            if movie[0] == cur_movie[event.source.user_id] and overview == "":
                overview = movie[5]
                break
        
        send_text_message(reply_token, overview)

    def on_enter_popular(self, event):
        reply_token = event.reply_token
        temp = json.load(open('view_movie.json', 'r', encoding='utf-8'))
        data = api.get_popular()
        reply_token = event.reply_token
        for i in range(0, 5):
        #i = 0
            temp['contents'][i]['hero']['url'] = 'https://image.tmdb.org/t/p/w500' + data[i][6]
            temp['contents'][i]['body']['contents'][0]['text'] = str(data[i][0])
            temp['contents'][i]['footer']['contents'][0]['text'] += (': ' +  str(data[i][1]))
            temp['contents'][i]['footer']['contents'][1]['text'] += (': ' + str(data[i][2]))
            temp['contents'][i]['footer']['contents'][2]['text'] += (': ' + str(data[i][3]))
            temp['contents'][i]['footer']['contents'][3]['text'] += (': ' + str(data[i][4]))
            temp['contents'][i]['footer']['contents'][4]['action']['text'] = str(data[i][0])
        
        send_flex_message(reply_token, "popular", temp)

    def on_enter_top_rated(self, event):
        reply_token = event.reply_token
        temp = json.load(open('view_movie.json', 'r', encoding='utf-8'))
        data = api.get_top_rated()
        reply_token = event.reply_token
        for i in range(0, 5):
        #i = 0
            temp['contents'][i]['hero']['url'] = 'https://image.tmdb.org/t/p/w500' + data[i][6]
            temp['contents'][i]['body']['contents'][0]['text'] = str(data[i][0])
            temp['contents'][i]['footer']['contents'][0]['text'] += (': ' +  str(data[i][1]))
            temp['contents'][i]['footer']['contents'][1]['text'] += (': ' + str(data[i][2]))
            temp['contents'][i]['footer']['contents'][2]['text'] += (': ' + str(data[i][3]))
            temp['contents'][i]['footer']['contents'][3]['text'] += (': ' + str(data[i][4]))
            temp['contents'][i]['footer']['contents'][4]['action']['text'] = str(data[i][0])
        
        send_flex_message(reply_token, "top_rated", temp)

    def on_enter_upcoming(self, event):
        reply_token = event.reply_token
        temp = json.load(open('view_movie.json', 'r', encoding='utf-8'))
        data = api.get_upcoming()
        reply_token = event.reply_token
        for i in range(0, 5):
        #i = 0
            temp['contents'][i]['hero']['url'] = 'https://image.tmdb.org/t/p/w500' + data[i][6]
            temp['contents'][i]['body']['contents'][0]['text'] = str(data[i][0])
            temp['contents'][i]['footer']['contents'][0]['text'] += (': ' +  str(data[i][1]))
            temp['contents'][i]['footer']['contents'][1]['text'] += (': ' + str(data[i][2]))
            temp['contents'][i]['footer']['contents'][2]['text'] += (': ' + str(data[i][3]))
            temp['contents'][i]['footer']['contents'][3]['text'] += (': ' + str(data[i][4]))
            temp['contents'][i]['footer']['contents'][4]['action']['text'] = str(data[i][0])
        
        send_flex_message(reply_token, "upcoming", temp)

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        temp = json.load(open('fsm.json', 'r', encoding='utf-8'))
        send_flex_message(reply_token, "fsm", temp)



    
