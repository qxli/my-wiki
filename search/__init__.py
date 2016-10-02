#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from whoosh import index
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
import json
from whoosh.qparser import QueryParser


def to_unicode(string):
    if isinstance(string, str):
        value = string.decode('utf-8')
    else:
        value = string
    return value


class Index(object):
    def __init__(self, dir):
        self.dir = dir
        analyzer = ChineseAnalyzer()
        self.schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True),
                    content=TEXT(stored=True, analyzer=analyzer))

    def build(self, title, content, path):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
            ix = index.create_in(self.dir, self.schema)
        else:
            ix = index.open_dir(self.dir)
        writer = ix.writer()
        writer.add_document(title=to_unicode(title), path=to_unicode(path), content=to_unicode(content))
        writer.commit()

    def search(self, kw):
        ix = index.open_dir(self.dir)
        searcher = ix.searcher()
        results = searcher.find("content", to_unicode(kw))
        # qp = QueryParser("content", schema=self.schema)
        # q = qp.parse(to_unicode(kw))
        # results = searcher.search(q)
        res = []
        for r in results:
            field = r.fields()
            # jsondoc = json.dumps(firstdoc, ensure_ascii=False)
            doc = {
                'title': field['title'],
                'path': field['path'],
                'desc': r.highlights("content")
            }
            res.append(doc)
        return res
