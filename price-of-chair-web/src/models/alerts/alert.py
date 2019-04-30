import uuid


class Alert(object):
    def __init__(self, user, price_limit, item, _id=None):
        self.user = user
        self.price_limit = price_limit
        self.item = item
        self._id = uuid.uuid4().hex if not _id else _id

#one of good practice is also to define how the class looks like printed out
#what is their string representation
    def __repr__(self):
        return "<Alert for {} on item {} with price {}".format(self.user.email, self.item.name, self.price_limit)