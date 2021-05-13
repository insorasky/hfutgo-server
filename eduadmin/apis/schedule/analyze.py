import re
DAY_CHINESE = {
    '周一': 1,
    '周二': 2,
    '周三': 3,
    '周四': 4,
    '周五': 5,
    '周六': 6,
    '周日': 7
}
CLASS_CHINESE = {
    '第一节': 1,
    '第二节': 2,
    '第三节': 3,
    '第四节': 4,
    '第五节': 5,
    '第六节': 6,
    '第七节': 7,
    '第八节': 8,
    '第九节': 9,
    '第十节': 10,
    '第十一节': 11
}


def analyze(string):
    strings = string.split(' ')
    time_str = strings[0]
    day_str = strings[1]
    class_str = strings[2].split('~')
    day = DAY_CHINESE[day_str]  # 星期
    # 节次
    class_nums = []
    for class_num in class_str:
        class_nums.append(CLASS_CHINESE[class_num.replace(';', '')])
    # 教室
    pattern = re.compile(r"^.*?[0-9]{1,3}")
    rooms = []
    if len(strings) > 3:
        rooms = [strings[3]] if len(strings) == 4 else re.findall(pattern, strings[4])
    # 时间
    pattern = re.compile(r"([0-9]+~?[0-9]*(\(.\))?)")
    week_infos = re.findall(pattern, time_str)
    pattern1 = re.compile(r"[0-9]+~?[0-9]*")
    weeks = []
    for week_info in week_infos:
        type_text = week_info[1]
        week_text = re.findall(pattern1, week_info[0])[0].split("~")
        if len(week_text) == 1:
            weeks.append(int(week_text[0]))
        else:
            week_this = int(week_text[0])
            weekend = int(week_text[1])
            while True:
                if week_this > weekend:
                    break
                if type_text == "(单)":
                    if (week_this % 2) != 1:
                        week_this += 1
                        continue
                if type_text == "(双)":
                    if (week_this % 2) != 0:
                        week_this += 1
                        continue
                weeks.append(week_this)
                week_this += 1
    if len(rooms) == 0:
        rooms = ['']
    return {
        'weeks': weeks,
        'day': day,
        'class': class_nums,
        'room': rooms[0].split('(')[0]
    }


if __name__ == '__main__':
    schedule_texts = '1~10,12~17周 周一 第三节~第四节 翡翠湖校区 翠五教104(201); \n1~10,12~17周 周三 第一节~第二节 翡翠湖校区 翠五教104(201); \n1~10,12~17周 周五 第三节~第四节 翡翠湖校区 翠五教104(201)'.split('; \n')
    schedules = []
    for text in schedule_texts:
        print(analyze(text))