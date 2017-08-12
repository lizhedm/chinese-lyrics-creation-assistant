pinyin_chinese_dic = {}

shengdiao_dic = {'ā':'a','á':'a','ǎ':'a','à':'a',
                  'ē':'e','é':'e','ě':'e','è':'e',
                  'ī':'i','í':'i','ǐ':'i','ì':'i',
                  'ō':'o','ó':'o','ǒ':'o','ò':'o',
                  'ū':'u','ú':'u','ǔ':'u','ù':'u'
                }

def initialData():
    pingyin_txt = open("kHanyuPinlu.txt","r").read()
    code_pingyin_chinese_list = pingyin_txt.split('\n')
    pinyin_list = []
    chinese_list = []
    for item in code_pingyin_chinese_list:
        pinyin_chinese_list = item.split(':')
        temp_list = pinyin_chinese_list[1].split('#')
        pinyin_str = temp_list[0].strip()
        for shengdiao_character in shengdiao_dic.keys():
            if shengdiao_character in pinyin_str:
                pinyin_str = pinyin_str.replace(shengdiao_character,shengdiao_dic[shengdiao_character])
        chinese_str = temp_list[1].strip()
        if pinyin_str in pinyin_chinese_dic:
            pinyin_chinese_dic[pinyin_str].append(chinese_str)
        else:
            pinyin_chinese_dic[pinyin_str] = [chinese_str]
    print(len(pinyin_chinese_dic))
    print(type(pinyin_chinese_dic))
    
def searchPinyin(search_str):
    result_list = []
    str_len = len(search_str)
    for pinyin_key in pinyin_chinese_dic.keys():
#         still have bugs
        if search_str == pinyin_key[-str_len:]:
            result_list.append(pinyin_chinese_dic[pinyin_key])
    return(result_list)

initialData()
search_str = input('What do you want to search? ')
searchPinyin(search_str)