from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.models import posts
from . import admin_bp
from .forms import PostForm

@admin_bp.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)

        return redirect(url_for('public.index'))
    return render_template("admin/post_form.html", form=form) 