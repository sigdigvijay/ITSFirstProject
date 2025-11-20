def append_statistics(filepath, num_of_posts, followers, following):

    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information["statistics"].append({
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "num_of_posts": num_of_posts,
        "followers": followers,
        "following": following,

    })

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=2)