import yt_dlp  
import os
class Cat:
    def __init__(self,url,height='1080',output_path='small_cat',title='%(title)s',is_upload=False):
        self.url=url
        self.height=height
        self.output_path=output_path
        self.is_upload=is_upload
        self.title=title
    def get_video_title(self):
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.url, download=False)
            return info_dict.get('title', None)
    def download_video(self):  
        ydl_opts = {  
            'format': f"bestvideo[height<={self.height}]+bestaudio/best", 
            'outtmpl': f'{self.output_path}/{self.title}.%(ext)s',     
        }  
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  
            ydl.download([self.url]) 
        if self.title=='%(title)s':
            title=self.get_video_title()
            self.output_path=f'D:/python/{self.output_path}/{title}.webm'
        else:
            self.output_path=f'D:/python/{self.output_path}/{self.title}.webm'


class BiliUpload:

    def __init__(self,video_title,video_type,video_path,main_partition,minor_partition,video_tag=True):
        self.partition={
            '生活':{
                'origin':'//*[@class="f-item-content" and text()="生活"]',
                '搞笑':'//*[@class="item-main" and text()="搞笑"]',
                '亲子':'//*[@class="item-main" and text()="亲子"]',
                '出行':'//*[@class="item-main" and text()="出行"]',
                '三农':'//*[@class="item-main" and text()="三农"]',
                '家居房产':'//*[@class="item-main" and text()="家具房产"]',
                '手工':'//*[@class="item-main" and text()="手工"]',
                '绘画':'//*[@class="item-main" and text()="绘画"]',
                '日常':'//*[@class="item-main" and text()="日常"]',
                },
            '游戏':{
                'origin':'//*[@class="f-item-content" and text()="游戏"]',
                '单机游戏':'//*[@class="item-main" and text()="单机游戏"]',
                '网络游戏':'//*[@class="item-main" and text()="网络游戏"]',
                '手机游戏':'//*[@class="item-main" and text()="手机游戏"]',
                '电子竞技':'//*[@class="item-main" and text()="电子竞技"]',
                '桌游棋牌':'//*[@class="item-main" and text()="桌游棋牌"]',
                '音游':'//*[@class="item-main" and text()="音游"]',
                'GMV':'//*[@class="item-main" and text()="GMV"]',
                'Mugen':'//*[@class="item-main" and text()="Mugen"]',
            },
            '娱乐':{
                'origin':'//*[@class="f-item-content" and text()="娱乐"]',
                '娱乐杂谈':'//*[@class="item-main" and text()="娱乐杂谈"]',
                'CP安利':'//*[@class="item-main" and text()="CP安利"]',
                '颜值安利':'//*[@class="item-main" and text()="颜值安利"]',
                '娱乐粉丝创作':'//*[@class="item-main" and text()="娱乐粉丝创作"]',
                '娱乐资讯':'//*[@class="item-main" and text()="娱乐资讯"]',
                '明星综合':'//*[@class="item-main" and text()="明星综合"]',
                '综艺':'//*[@class="item-main" and text()="综艺"]',        
            },
            '知识':{
                'origin':'//*[@class="f-item-content" and text()="知识"]',
                '科学科普':'//*[@class="item-main" and text()="科学科普"]',
                '社科·法律·心理':'//*[@class="item-main" and text()="社科·法律·心理"]',
                '人文历史':'//*[@class="item-main" and text()="人文历史"]',
                '财经商业':'//*[@class="item-main" and text()="财经商业"]',
                '校园学习':'//*[@class="item-main" and text()="校园学习"]',
                '设计·创意':'//*[@class="item-main" and text()="设计·创意"]',
                '野生技能协会':'//*[@class="item-main" and text()="野生技能协会"]', 
            }
        }
        self.video_title=video_title
        self.video_tag=video_tag
        self.video_type=video_type
        self.video_path=video_path
        if main_partition in self.partition:
            self.main_partition=self.partition[main_partition]['origin']
        if minor_partition in self.partition[main_partition]:
            self.minor_partition=self.partition[main_partition][minor_partition]
        
