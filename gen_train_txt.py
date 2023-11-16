import os

def gen_txt():
    with open("filelists/genshin.txt", "w", encoding='utf-8') as f:
        for root, dirs, files in os.walk("raw"):
            for file in files:
                if file.endswith(".lab"):
                    file_name = file.split(".")[0]
                    speak_name = root.split("\\")[1]
                    wav_path = './dataset/' + speak_name + '/' + file_name + ".wav"
                    with open(os.path.join(root, file), "r", encoding='utf-8') as fp:
                        text = fp.readline()
                        # print(wav_path, text)
                        content = wav_path + '|' + speak_name + '|ZH|' + text
                        f.write(content + "\n")

def get_speak_names():
    speak_list = []
    for root,  dirs, files in os.walk("raw"):
        for dir in dirs:
            speak_list.append(dir)
    speak_list = list(set(speak_list))
    speak_dict = str(dict(zip(speak_list, range(len(speak_list))))).replace('\'', '\"')
    return speak_dict

if __name__ == "__main__":
    print(get_speak_names())