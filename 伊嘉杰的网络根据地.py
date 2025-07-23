import streamlit as st
from PIL import Image,ImageMath
import datetime
page = st.sidebar.radio("我的主页",["自我介绍","兴趣推荐","图片处理","智能词典","程序分享","聊天社区","网页日志"])

st.markdown(
    """
    <style>
    /* 全局背景设置 */
    body, .stApp {
        background-color: #f5f9ff !important;  /* 深蓝色背景 */
        background-image: linear-gradient(160deg, #000000 0%, #FFFFFF 100%);
        color: white;
    }


    /* 侧边栏背景 */
    section[data-testid="stSidebar"] {
        background-color: #AFF3FF !important;  /* 深蓝色背景 */
        background-image: linear-gradient(160deg, #BBBBBB 0%, #FFFFFF 100%);
        color: white;
    }

    /* 按钮容器悬停效果 */
    .stButton>button:hover {
        background-color: #FFA05F !important;
        transform: scale(1.05);
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

def page1():
    #自我介绍
    st.title("自我介绍")
    today = datetime.datetime.today()
    year = today.year
    sui = int(year) - 2014
    sui = str(sui)
    st.image("中国国旗.png")
    st.write("你好 我叫伊嘉杰 今年",sui,"岁")
    st.write("来自中华人民共和国 北京 石景山")
    st.write("我喜欢编程")
    st.write("下面是我的网络根据地")

def page2():
    #兴趣推荐
    st.title("兴趣推荐")
    t1,t2,t3 = st.tabs(["华为","波兰球","我的世界"])
    with t1:
        st.write(":red[华为]")
        with open("华为.MP3","rb") as f:
            mp3 = f.read()
        st.audio(mp3,format="audio/mp3",start_time = 0)
        st.image("华为.png")
        st.write("相关词条:国货之光,遥遥领先,HarmonyOS,Kirin")
    with t2:
        st.write(":red[波兰球]")
        with open("波兰球.MP3","rb") as f:
            mp3 = f.read()
        st.audio(mp3,format="audio/mp3",start_time = 0)
        st.image("波兰球.png")
        st.write("相关词条:国家球,国家形象,国际关系,幽默诙谐")
    with t3:
        st.write(":red[我的世界]")
        with open("我的世界.MP3","rb") as f:
            mp3 = f.read()
        st.audio(mp3,format="audio/mp3",start_time = 0)
        st.image("我的世界.png")
        st.write("相关词条:沙盒式建造游戏,收集资源,与敌对生物战斗,合成新的方块")

def i_c (img,rc,gc,bc):
    w,h = img.size
    i_a = img.load()
    for x in range(w):
        for y in range(h):
            r = i_a[x,y][rc]
            g = i_a[x,y][gc]
            b = i_a[x,y][bc]
            i_a[x,y] = (r,g,b)
    return img

def page3():
    #图片处理
    st.title("图片处理小程序")
    u_f = st.file_uploader("上传图片",type = ["png","jpeg","jpg"])
    if u_f:
        f_n = u_f.name
        f_t = u_f.type
        f_s = u_f.size
        img = Image.open(u_f)
        st.write("改色")
        t1,t2,t3,t4,t5,t6 = st.tabs(["红绿蓝","红蓝绿","绿红蓝","绿蓝红","蓝红绿","蓝绿红"])
        with t1:
            st.image(i_c(img,0,1,2))
        with t2:
            st.image(i_c(img,0,2,1))
        with t3:
            st.image(i_c(img,1,0,2))
        with t4:
            st.image(i_c(img,1,2,0))
        with t5:
            st.image(i_c(img,2,0,1))
        with t6:
            st.image(i_c(img,2,1,0))

def page4():
    #智能词典
    st.title("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        w_l = f.read().split("\n")
    for i in range(len(w_l)):
        w_l[i] = w_l[i].split("#")
    w_d = {}
    for i in w_l:
        w_d[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        t_l = f.read().split("\n")
    for i in range(len(t_l)):
        t_l[i] = t_l[i].split("#")
    t_d = {}
    for i in t_l:
        t_d[int(i[0])] = int(i[1])
    w = st.text_input("输入要查询的英文单词")
    if w:
        if w in w_d:
            st.write(w_d[w][1])
            n = w_d[w][0]
            if n in t_d:
                t_d[n] += 1
            else:
                t_d[n] = 1

            with open("check_out_times.txt","w",encoding="utf-8") as f:
                m = ""
                for k,v in t_d.items():
                    m += str(k)+"#"+str(v)+"\n"
                m = m[:-1]
                f.write(m)  
            st.write("查询次数：",t_d[n])
                
            if w == "python":
                st.write('''#恭喜你触发彩蛋，下面是一行python代码:print("Hello world")''')
                
            if w == "balloon":
                st.write("恭喜你触发彩蛋")
                st.balloons()
                
            if w == "snow":
                st.write("恭喜你触发彩蛋")
                st.snow()

            if w == "name":
                st.write("恭喜你触发彩蛋,这个网站的作者是伊嘉杰")

        else:
            st.write("没有查询到输入的单词")

def page5():
    #程序分享
    st.title("程序分享")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.link_button("合集", "https://pan.baidu.com/s/10ZBuITR0l51AGP63rlKkqw 提取码: base")
        st.link_button("植物大战僵尸", "https://pan.baidu.com/s/1oBziTKK1BPXq40SPB0x1oA?pwd=base 提取码: base")
        st.link_button("平台类游戏","https://pan.baidu.com/s/1ZFwzWjn-4i0LRpT0a8BsGA?pwd=base 提取码: base")
        st.link_button("我的世界（2D简易）","https://pan.baidu.com/s/1qmnN23qjWYS3pMcVbCmJaA?pwd=base 提取码: base")
        st.link_button("物理炸弹","https://pan.baidu.com/s/1GzPdGAjEunOD0xg014RRNA?pwd=base 提取码: base")
        st.link_button("我的世界 (2D高级)","https://pan.baidu.com/s/1Rdb7Oahgp7lfxXzjB6ux4A?pwd=base 提取码: base")
    with col2:
        st.link_button("简化分数","https://pan.baidu.com/s/1n0ud8wdqGkxhAAH54GupMg?pwd=base 提取码: base")
        st.link_button("代码雨","https://pan.baidu.com/s/1yMG-IVBb0v-0noCf-0ZdQw?pwd=base 提取码: base")
        st.link_button("超级玛丽","https://pan.baidu.com/s/1YVD22YYkvrwgVD4MmfP37w?pwd=base 提取码: base")
        st.link_button("PythonSuperMario","https://pan.baidu.com/s/1k-8UVH3vQ9PqyOQmsAx9rQ?pwd=base 提取码: base")
        st.link_button("病毒","https://pan.baidu.com/s/1H1hTBqMSaNnlJpEFD65b4g?pwd=base 提取码: base")
        st.link_button("HTML太阳系3D模拟实现方案","https://pan.baidu.com/s/18FfRxiNkBV-8Fmy9ATM71w?pwd=base 提取码: base")
def page6():
    #聊天社区
    st.title("聊天社区")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        m_l = f.read().split("\n")
    for i in range(len(m_l)):
        m_l[i] = m_l[i].split("#")
    for i in m_l:
        st.write(i[1],":",i[2])
    name = st.text_input("留言者：")
    n_m = st.text_input("想要说的话：")
    if st.button("留言"):
        m_l.append([str(int(m_l[-1][0])+1),name,n_m])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            m = ""
            for i in m_l:
                m += i[0]+ "#" + i[1] + "#" + i[2] + "\n"
            m = m[:-1]
            f.write(m)

def page7():
    st.title("网页日志")
    st.text("2025/7/17")
    st.write("网站开始开发")
    st.text("2025/7/22")
    st.write("网站上传到公网")
    
if page == "自我介绍":
    page1()
if page == "兴趣推荐":
    page2()
if page == "图片处理":
    page3()
if page == "智能词典":
    page4()
if page == "程序分享":
    page5()
if page == "聊天社区":
    page6()
if page == "网页日志":
    page7()