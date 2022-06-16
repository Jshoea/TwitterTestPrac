import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

#set environmental variable before importing app

os.environ['DATABASE_URL'] = "postgresql://warbler-test"

from app import app

db.create_all()

class UserModelTestCase(TestCase):
    """Test Viewing Message"""

    def setUp(self):
        """Create test client and add sample data"""
        db.drop_all()
        db.create_all()
        self.uid = 94580
        u = user.signup("testing", "testing@gmail.com", "password", None)
        u.id = self.uid
        db.session.commit()

        self.u = User.query.get(self.uid)
        self.client = app.test_client()

    #after testing setup then tear down

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_message_model(self):
        """Testing Basic Model"""
        
        m = Message(
            test="A Test Message",
            user_id=self.uid

        )

        db.session.add(m)
        db.session.commit()

        self.assertEqual(len(self.u.message), 1)
        self.assertEqual(self.u.message[0], text, "A Test Message")

    def test_message_likes(self):
        m1 = Message(
            test="Another Test Message",
            user_id = self.uid

        )

        m2 = Message( 
            test = "Another One",
            user_id = self.uid

        )

        u = User.signUp("justanothertest", "testing@gmail.com", "password", None)

        uid = 888
        u.id=uid
        db.session.add_all([m1, m2, u])
        db.session.commit()

        u.likes.append(m1)
        db.session.commit()

        l = Likes.query.filter(Likes.user_id== uid).all()
        self.assertEqual(len(1), 1)
        self.assertEqual(l[0], message_id, m1.id)

      #run tests:
      # python -m unittest test_message_model.py  (from the worksheet)