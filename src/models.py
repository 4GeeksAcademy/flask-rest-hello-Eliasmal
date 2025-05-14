
from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    Username: Mapped[str] = mapped_column(String(80), nullable=False)
    firstname: Mapped[str] = mapped_column(String(80), nullable=False)
    lastname: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    follower_from: Mapped[List["Follower"]] = relationship(back_populates="user_from")
    follower_to: Mapped[List["Follower"]] = relationship(back_populates="user_to")

    comment: Mapped[List["Comment"]] = relationship(back_populates="user")

    Post: Mapped[List["Post"]] = relationship(back_populates="post")


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comment")

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="post")

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(120), nullable=False)
    url: Mapped[str] = mapped_column(String(120), nullable=False)

    Post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="media")

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    comment: Mapped[List["Comment"]] = relationship(back_populates="post")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="post")

    media: Mapped[List["Media"]] = relationship(back_populates="post")


class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_from: Mapped["User"] = relationship(back_populates="followers_from")

    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to: Mapped["User"] = relationship(back_populates="followers_to")
