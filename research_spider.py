#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Title: Research Spider for Anthology

  Author: wangleyi
  Date: 2019-04-16 13:37
  Update: Last update 2019-04-16
  Email: leyiwang.cn@gmail.com
"""
import time

from nlp_research.anthology_spider import AnthologySpider
from utils.log import logger


def main(keywords, years, events):
    start_time = time.time()
    acl_spider = AnthologySpider(keywords, years, events)
    acl_spider.run()
    cost = time.time() - start_time
    logger.info("Done! Seconds cost: {:.2f}".format(cost))


if __name__ == '__main__':
    years = (2016, 2021)
    keywords_list = ['fraud','telecommunication','detection']
    events = ['ACL', 'CL', 'COLING', 'EACL', 'EMNLP', 'LREC', 'NAACL']
    main(keywords_list, years, events)
