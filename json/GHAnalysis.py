import os
import json
import sys
import getopt
import argparse



def get_json(path_to_data):
    file_list = os.listdir(path_to_data)
    jsfile = open('js_data.json', 'w', encoding = 'utf-8')
    for file in file_list:
        new_file = path_to_data + '\\' + file
        data_file = open(new_file, 'r', encoding = 'utf-8')
        for line in data_file:
            data = json.loads(line)
            jsfile.write(line)
    jsfile.close()
    data_file.close()
    return


def get_result(jsdata_list, user, event, repo):
    '''获取最终结果的函数'''
    result = 0
    i = 0
    # print(f'{user}')
    # print(f'{event}')
    for jsdata in jsdata_list:
        if len(user) != 0 and len(repo) == 0:
            if user == jsdata['actor']['login'] and jsdata['type'] == event:
                result += 1
            else:
                pass
        elif len(user) == 0 and len(repo) != 0:
            if repo == jsdata['repo']['name'] and jsdata['type'] == event:
                result += 1
            else:
                pass
        elif len(user) != 0 and len(repo) != 0:
            if repo == jsdata['repo']['name'] and jsdata['type'] == event and user == jsdata['actor']['login']:
                result += 1
            else:
                pass
    print(result)


def main():
    '''命令行参数的函数'''
    user = 'cdupuis'
    event = 'PushEvent'
    repo = 'atomist/automation-client'
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', default = '')
    parser.add_argument('-u', '--user', default = '')
    parser.add_argument('-r', '--repo', default = '')
    parser.add_argument('-e', '--event', default = '')
    args = parser.parse_args()
    path = args.init
    if len(path) != 0:
        get_json(path)
    user = args.user
    event = args.event
    repo = args.repo
    jsdata_list = []
    data = open('js_data.json', 'r', encoding = 'utf-8')
    for da in data:
        jsdata_list.append(json.loads(da))
    get_result(jsdata_list, user, event, repo)


if __name__ == "__main__":
    main()
