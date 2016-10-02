#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import db


class Post(db.Model):
    __tablename__ = 'post'
    __searchable__ = ['title', 'content', 'path']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    path = db.Column(db.String(255))


