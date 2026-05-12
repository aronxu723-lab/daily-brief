"""HackerNews 新闻源"""

import requests
import logging
from typing import List, Dict, Any
from datetime import datetime
import pytz
from ..news_collector import NewsSource


class HackerNewsSource(NewsSource):
    """从 HackerNews 获取新闻"""
    
    API_BASE = 'https://hacker-news.firebaseio.com/v0'
    STORIES_URL = f'{API_BASE}/topstories.json'
    ITEM_URL = f'{API_BASE}/item'
    TIMEOUT = 10
    
    def __init__(self, config: Dict[str, Any], logger: logging.Logger):
        super().__init__(config, logger)
        self.timezone = pytz.timezone(config.get('timezone', 'Asia/Shanghai'))
    
    def _get_item(self, item_id: int) -> Dict[str, Any]:
        """获取单个 HN 项目"""
        try:
            url = f'{self.ITEM_URL}/{item_id}.json'
            response = requests.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.warning(f"获取 HN 项目 {item_id} 失败: {e}")
            return {}
    
    def fetch(self) -> List[Dict[str, Any]]:
        """获取 HackerNews 热门新闻"""
        try:
            # 获取热门故事 ID
            response = requests.get(self.STORIES_URL, timeout=self.TIMEOUT)
            response.raise_for_status()
            story_ids = response.json()[:30]  # 获取前 30 个
            
            news_list = []
            
            for story_id in story_ids:
                item = self._get_item(story_id)
                
                if not item or item.get('type') != 'story':
                    continue
                
                # 只要有 URL 的项目
                if not item.get('url'):
                    continue
                
                # 转换时间戳
                timestamp = datetime.fromtimestamp(
                    item.get('time', 0),
                    tz=self.timezone
                )
                
                news = {
                    'title': item.get('title', ''),
                    'url': item.get('url', ''),
                    'description': f"HackerNews 热度: {item.get('score', 0)}",
                    'timestamp': timestamp,
                    'source': 'HackerNews',
                }
                
                news_list.append(news)
            
            self.logger.info(f"HackerNews: 获取 {len(news_list)} 条新闻")
            return news_list
            
        except Exception as e:
            self.logger.error(f"HackerNews 采集失败: {e}")
            return []
