from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('postgresql://catalog:udacity2018@localhost/capp')
# engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

Item1 = Item(user_id=1, name="Soccer cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category1)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Soccer Jersey", description="Just do it and win.",
                 category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Goalkeeper gloves", description="Don't let them score a single goal!",
                 category=category1)

session.add(Item4)
session.commit()

# Items for Baseball

category2 = Category(user_id=1, name="Baseball")

session.add(category2)
session.commit()

Item1 = Item(user_id=1, name="Baseball cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category2)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,name="Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Baseball Jersey", description="Just do it and win.",
                 category=category2)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Baseball glove", description="Don't let them score and catch that ball!",
                 category=category2)

session.add(Item4)
session.commit()

# Items for Basketball

category3 = Category(user_id=1, name="Basketball")

session.add(category3)
session.commit()

Item1 = Item(user_id=1, name="Basketball shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category3)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,name="Basketball", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category3)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1,name="Basketball Jersey", description="Just do it and win.",
                 category=category3)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Basketball socks", description="Don't let them score! Fly high!",
                 category=category3)

session.add(Item4)
session.commit()

# Itmes for Cycling

category4 = Category(user_id=1, name="Cycling")

session.add(category4)
session.commit()

Item1 = Item(user_id=1,name="Cycling shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Ride Explosive.",
                 category=category4)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Cycling shorts", description="Always Be Prepared For The Season With our Cycling shorts.",
                 category=category4)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Cycling Jersey", description="Just do it and win.",
                 category=category4)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Cycling gloves", description="Don't let them win, be a winner!",
                 category=category4)

session.add(Item4)
session.commit()

# Items for Hockey

category5 = Category(user_id=1, name="Hockey")

session.add(category5)
session.commit()

Item1 = Item(user_id=1, name="Hockey skates", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category5)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Hockey Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category5)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Hockey Jersey", description="Just do it and win.",
                 category=category5)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Hockey gloves", description="Don't let them score and catch that thing!",
                 category=category5)

session.add(Item4)
session.commit()

# Items for Boxing

category6 = Category(user_id=1, name="Boxing")

session.add(category6)
session.commit()

Item1 = Item(user_id=1, name="Boxing gloves", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Hit Explosive.",
                 category=category6)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Cup protector", description="Always Be Prepared For The biggest fight of your life with our Sporting Goods.",
                 category=category6)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Boxing shorts", description="Just do it and win.",
                 category=category6)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Boxing rope", description="Walk into the ring like a winner!",
                 category=category6)

session.add(Item4)
session.commit()

# Items for Running

category7 = Category(user_id=1, name="Running")

session.add(category7)
session.commit()

Item1 = Item(user_id=1, name="Running shoes", description="Unleash The Speed In The Exclusive Initiator Pack. Run Fast. Run Explosive.",
                 category=category7)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Running shorts", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category7)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Running shirt", description="Just do it and win.",
                 category=category7)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Running socks", description="Don't stop running!",
                 category=category7)

session.add(Item4)
session.commit()

# Items for Swimming

category8 = Category(user_id=1, name="Swimming")

session.add(category8)
session.commit()

Item1 = Item(user_id=1, name="Swimming shorts", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Swim Explosive.",
                 category=category8)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Swimming cap", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category8)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Swimming goggles", description="Just do it and swim.",
                 category=category8)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Swimming rope", description="Swim to win!",
                 category=category8)

session.add(Item4)
session.commit()

# Items for Rock Climbing

category9 = Category(user_id=1, name="Rock Climbing")

session.add(category9)
session.commit()

Item1 = Item(user_id=1, name="Climbing cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Climb Explosive.",
                 category=category9)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Climbing chalk", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category9)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Climbing Jersey", description="Just do it and Climb to the top.",
                 category=category9)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Climbing rope", description="Don't let go, use the best ropes!",
                 category=category9)

session.add(Item4)
session.commit()

print "Items added!"
