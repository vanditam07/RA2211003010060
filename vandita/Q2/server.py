from fastapi import FastAPI, HTTPException, Query
import aiohttp
import asyncio
from collections import defaultdict
from datetime import datetime, timedelta

app = FastAPI()

BASE_API_URL = "http://20.244.56.144/test"

CACHE_EXPIRY = timedelta(minutes=5)
cache = {"users": None, "posts": None, "comments": None, "last_updated": None}

async def fetch_json(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 401:
                raise HTTPException(status_code=401, detail="Unauthorized API access")
            else:
                return None
    except Exception:
        return None

async def refresh_cache():
    if cache["last_updated"] and datetime.utcnow() - cache["last_updated"] < CACHE_EXPIRY:
        return  

    async with aiohttp.ClientSession() as session:
        users_data = await fetch_json(session, f"{BASE_API_URL}/users")
        if not users_data or "users" not in users_data:
            raise HTTPException(status_code=500, detail="Failed to fetch users")

        users = users_data["users"]
        posts = []

        for user_id in users.keys():
            user_posts = await fetch_json(session, f"{BASE_API_URL}/users/{user_id}/posts")
            if user_posts:
                posts.extend(user_posts)

        cache["users"] = users
        cache["posts"] = posts
        cache["last_updated"] = datetime.utcnow()

async def get_users():
    await refresh_cache()
    users = cache["users"]
    posts = cache["posts"]

    post_count = defaultdict(int)
    for post in posts:
        if isinstance(post, dict) and "userid" in post:
            post_count[str(post["userid"])] += 1

    top_users = sorted(users.items(), key=lambda u: post_count.get(u[0], 0), reverse=True)[:5]
    return [{"id": int(uid), "name": uname, "post_count": post_count.get(uid, 0)} for uid, uname in top_users]

async def get_user_posts(user_id: int):
    await refresh_cache()
    posts = cache["posts"]

    user_posts = [post for post in posts if post.get("userid") == user_id]
    if not user_posts:
        raise HTTPException(status_code=404, detail="No posts found for this user")

    return user_posts

async def get_post_comments(post_id: int):
    async with aiohttp.ClientSession() as session:
        comments_data = await fetch_json(session, f"{BASE_API_URL}/posts/{post_id}/comments")

    if not comments_data or "comments" not in comments_data:
        raise HTTPException(status_code=404, detail="No comments found for this post")

    return comments_data["comments"]

async def get_top_or_latest_posts(post_type: str):
    await refresh_cache()
    posts = cache["posts"]

    if post_type == "popular":
        comment_counts = {}
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_json(session, f"{BASE_API_URL}/posts/{post['id']}/comments") for post in posts]
            results = await asyncio.gather(*tasks)

        for post, comments in zip(posts, results):
            if comments and "comments" in comments:
                comment_counts[post["id"]] = len(comments["comments"])

        max_comments = max(comment_counts.values(), default=0)
        return [post for post in posts if comment_counts.get(post["id"], 0) == max_comments]

    elif post_type == "latest":
        return sorted(posts, key=lambda x: x.get("timestamp", ""), reverse=True)[:5]

    raise HTTPException(status_code=400, detail="Invalid post type. Use 'latest' or 'popular'.")

@app.get("/users")
async def top_users():
    return await get_users()

@app.get("/users/{user_id}/posts")
async def user_posts(user_id: int):
    return await get_user_posts(user_id)

@app.get("/posts/{post_id}/comments")
async def post_comments(post_id: int):
    return await get_post_comments(post_id)

@app.get("/posts")
async def posts(type: str = Query(..., description="Type of posts: 'latest' or 'popular'")):
    return await get_top_or_latest_posts(type)
