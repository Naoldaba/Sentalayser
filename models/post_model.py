class Post:
    def __init__(self, post_id, content, sentiment):
        self.id = post_id
        self.content = content
        self.sentiment = sentiment

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'sentiment': self.sentiment
        }

    @staticmethod
    def from_dict(item):
        return Post(
            post_id=item.get('id'),
            content=item.get('content'),
            sentiment=item.get('sentiment')
        )
