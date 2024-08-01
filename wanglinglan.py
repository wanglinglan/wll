"'wanglinglan 的网站'"
import  streamlit as st
from PIL import Image,ImageOps,ImageFilter
import matplotlib as plt

if st.button('音乐'):
    audio_file = open('霞光.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
else:
    st.write("祝您阅读愉快！")

col2,col3 = st.columns([4,7])
with col2:
    st.write(":blue[网页介绍]")
    st.write(" ")
    st.write("网站是我经六天努力完成的，还有很多不完善的地方，望众位海涵。")
    
    st.write(":blue[本人介绍]")
    st.write(" ")
    st.write("我是一名初中生，不太爱出门，但非常爱看课外书尤其是探案和冒险类的，也会看一些综艺节目")
    st.write("在此，祝福所有看到这儿的人一帆风顺，二龙腾飞，三羊开泰，四季平安，五福临门，六六大顺，七星高照，八方来财，九九同心，十全十美！！")
    st.image("读书.jpg")
with col3:
    st.write(":blue[喜欢的网站]")
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

    st.write(":blue[喜欢的游戏]")
    st.write(" ")
    st.write("推荐大家去233乐园，里面的游戏很全")
    
    st.write(":blue[喜欢的电视]")
    st.write(" ")
    st.write("密室大逃脱，奔跑吧，欢乐喜剧人第1季....")
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (b,g,r)
    return img
st.write(":sunglasses:改图专区:sunglasses:")
uploaded_file = st.file_uploader("上传图片",type=["png","jpg","jpeg"])
if uploaded_file:
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size
    img = Image.open(uploaded_file)
s = ["原图","改图1","改图2","改图3","灰度图","反色","高斯模糊","颜色减淡"]
ch = st.toggle('反色滤镜')
bw = st.toggle('原图')
co = st.toggle('换色')
mn = st.toggle('灰度图')
cn = st.toggle('高斯模糊')
hl = st.toggle('颜色减淡')

if ch:
    img_gray = img.convert('L')
    img_invert = ImageOps.invert(img_gray)
    st.image(img_invert)
if bw:
    st.image(img)
if co:
    st.image(img_change(img,1,2,0))
    st.image(img_change(img,0,2,1))
    st.image(img_change(img,1,0,2))
if mn:
    img_gray = img.convert('L')
    st.image(img_gray)
if cn:
    img_gray = img.convert('L')
    img_invert = ImageOps.invert(img_gray)
    img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
    st.image(img_gaussian)
if hl:
    width,height = img.size
    img_gray = img.convert('L')
    img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
    for x in range(width):
        for y in range(height):
            pos = (x,y)
            A = img_gray.getpixel(pos)
            B = img_gaussian.getpixel(pos)
            img_gray.putpixel(pos,min(int(A+A*B/(255-B)),255))
    st.image(img_gray)
col10,col11 = st.columns([3,3])
with col10:
    st.write("我的小作文")
    msg_lst = ['作文1.jpg', '作文2.jpg', '作文3.jpg', '作文4.jpg', '作文5.jpg', '作文6.jpg', '作文7.jpg', '作文8.jpg']
    begin, end = st.slider('选择显示的作文页数：', 1, len(msg_lst), (1, len(msg_lst)))
    for i in range(begin-1, end):
        st.image(msg_lst[i])
with col11:
    st.write("专业英语查词")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(7988):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in  times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
            with open("check_out_times.txt","w",encoding="utf-8")as f:
                message = ""
                for k,v in times_dict.items():
                    message += str(k) + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)
        st.write("查询次数：",times_dict[n])
        if word == "wang":
            st.code('''
                    #恭喜你触发彩蛋，这是一行Python代码
                    print("祝你万事顺利，福寿永年")''')
            st.balloons()
        if word =="π":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="qing":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="tan":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="yin":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="ming":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="fangpi":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="agirl":
            st.write("恭喜你触发彩蛋!")
            st.snow()
col12,col13 = st.columns([5,4])
with col12:
    st.write("我的旅游照片")
    st.image("旅游1.jpg")
    st.image("2.jpg")
    st.image("3.jpg")
    st.image("4.jpg")
    st.image("5.jpg")
    st.image("6.jpg")
    st.image("7.jpg")
    st.image("8.jpg")
with col13:
    st.write("音乐视频")
    with open("解密.mp4","rb") as f:
            mymp4 = f.read()
    st.write("周深——解密")
    st.video(mymp4)
    with open("轻音乐.mp4","rb") as f:
        mymp4_2 = f.read()
    st.write("一首轻音乐送你，放松一下疲劳的双耳吧")
    st.video(mymp4_2)
    st.write("想自己放首歌吗？来来来，往下看")
    st.write(":sunglasses:点歌小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传歌曲")
    if uploaded_file:
        st.audio(uploaded_file)
        
col14,col15 = st.columns([6,5])
with col14:
    st.write ("你知道如何解摩斯电码吗？")
    st.write("小编正在努力更新中....,暂不开放")
with col15:
    st.write("解秘方法")
    st.write("小编正在努力更新中....,暂不开放")


st.write('我的留言区')
with open("leave_messages.txt","r",encoding="utf-8")as f:
    messages_list = f.read().split("\n")
for i in range(len(messages_list)):
    messages_list[i] = messages_list[i].split("#")
for i in messages_list:
    if i[1] == "阿短":
        with st.chat_message("🍭"):
            st.write(i[1]+i[2])
    elif i[1] == "编程猫":
        with st.chat_message("🎇"):
            st.write(i[1]+i[2])
    elif i[1] == "学霸":
        with st.chat_message("🏆"):
            st.write(i[1]+i[2])
    elif i[1] == "神秘人":
        with st.chat_message("❔"):
            st.write(i[1]+i[2])
    elif i[1] == "富翁":
        with st.chat_message("💸"):
            st.write(i[1]+i[2])
    elif i[1] == "花季少女":
        with st.chat_message("💮"):
            st.write(i[1]+i[2])
    elif i[1] == "美女":
        with st.chat_message("😜"):
            st.write(i[1]+i[2])
    elif i[1] == "帅哥":
        with st.chat_message("😎"):
            st.write(i[1]+i[2])
    elif i[1] == "现代版福尔摩斯":
        with st.chat_message("🕵️‍♀️"):
            st.write(i[1]+i[2])
            
name = st.selectbox("我是.......",["阿短","现代版福尔摩斯","编程猫","学霸","神秘人","美女","帅哥","富翁","花季少女"])
new_message = st.text_input("想要说的话.....")
if st.button("留言"):
    messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
    with open("leave_messages.txt","w",encoding="utf-8")as f:
            message = ""
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] +"\n"
            message = message[:-1]
            f.write(message)
    