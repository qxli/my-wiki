#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web import app, idx
from flask import (render_template, flash, redirect, url_for, request, Blueprint, g)
from flask.ext.login import (LoginManager, login_required, current_user,
                             login_user, logout_user)

from web import wiki, users, protect, loginmanager, URLForm, EditorForm, LoginForm, SearchForm, Processors
from map import contents

site = Blueprint('site', __name__, template_folder='templates', static_folder='static')

@loginmanager.user_loader
def load_user(name):
    return users.get_user(name)


@site.route('/')
@protect
def home():
    # page = wiki.get('start')
    # if page:
    #     return display('start')
    return render_template('home.html', contents=contents)


@site.route('/index/')
@protect
def index():
    pages = wiki.index()
    return render_template('index.html', pages=pages)


@site.route('/<path:url>/')
@protect
def display(url):
    page = wiki.get_or_404(url)
    return render_template('page.html', page=page)


@site.route('/create/', methods=['GET', 'POST'])
@login_required
@protect
def create():
    form = URLForm()
    if form.validate_on_submit():
        return redirect(url_for('site.edit', url=form.clean_url(form.url.data)))
    return render_template('create.html', form=form)


@site.route('/edit/<path:url>/', methods=['GET', 'POST'])
@login_required
@protect
def edit(url):
    page = wiki.get(url)
    form = EditorForm(obj=page)
    if form.validate_on_submit():
        if not page:
            page = wiki.get_bare(url)
        form.populate_obj(page)
        page.save()
        flash('"%s" was saved.' % page.title, 'success')
        return redirect(url_for('site.display', url=url))
    return render_template('editor.html', form=form, page=page)


@site.route('/preview/', methods=['POST'])
@login_required
@protect
def preview():
    a = request.form
    data = {}
    processed = Processors(a['body'])
    data['html'], data['body'], data['meta'] = processed.out()
    return data['html']


@site.route('/move/<path:url>/', methods=['GET', 'POST'])
@login_required
@protect
def move(url):
    page = wiki.get_or_404(url)
    form = URLForm(obj=page)
    if form.validate_on_submit():
        newurl = form.url.data
        wiki.move(url, newurl)
        return redirect(url_for('site.display', url=newurl))
    return render_template('move.html', form=form, page=page)


@site.route('/delete/<path:url>/')
@login_required
@protect
def delete(url):
    page = wiki.get_or_404(url)
    wiki.delete(url)
    flash('Page "%s" was deleted.' % page.title, 'success')
    return redirect(url_for('site.home'))


@site.route('/tags/')
@protect
def tags():
    tags = wiki.get_tags()
    return render_template('tags.html', tags=tags)


@site.route('/tag/<string:name>/')
@protect
def tag(name):
    tagged = wiki.index_by_tag(name)
    return render_template('tag.html', pages=tagged, tag=name)


@site.route('/search/', methods=['GET', 'POST'])
@protect
def search():
    # form = SearchForm()
    # if form.validate_on_submit():
    kw = request.form['keyword']
    if kw:
        results = idx.search(kw)
        # results = wiki.search(kw)
        return render_template('search.html', search=True, results=results, keyword=kw)
    return render_template('search.html', search=False)


@site.route('/user/login/', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get_user(form.name.data)
        login_user(user)
        user.set('authenticated', True)
        flash('Login successful.', 'success')
        return redirect(request.args.get("next") or url_for('site.home'))
    return render_template('login.html', form=form)


@site.route('/user/logout/')
@login_required
def user_logout():
    current_user.set('authenticated', False)
    logout_user()
    flash('Logout successful.', 'success')
    return redirect(url_for('site.home'))


@site.route('/user/')
@login_required
def user_index():
    pass


@site.route('/user/create/')
@login_required
def user_create():
    users.add_user("qxli", "123")
    pass


@site.route('/user/<int:user_id>/')
@login_required
def user_admin(user_id):
    pass


@site.route('/user/delete/<int:user_id>/')
@login_required
def user_delete(user_id):
    pass


"""
    Error Handlers
    ~~~~~~~~~~~~~~
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
