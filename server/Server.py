from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_setup import Base, Group, Member, User
import uuid

# Basic

app = Flask(__name__)
app.config.from_object(__name__)

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CORS(app, resources={r'/*': {'origins': '*'}})


# CODE START


<<<<<<< HEAD
=======
# (GET) get a specific list of member inside a group, (POST) add new member to a specific group , 
#(PUT) update a specific group and members detail , (DELETE) delete group
>>>>>>> 2aa50a513852bf11e01fe8282a0501f4466d81e6

# check if username or email is valid or not
@app.route('/check', methods=['POST'])
def check():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        #check for email
        if post_data.get('gmail') == True:
            #post_data = request.get_json()
            try:

                # check if the user exists
                user1 = session.query(User).filter_by(email= post_data.get('email')).one()
                response_object['email'] = False
            # error
            except:
                response_object['email'] = True

        #check for username
        if post_data.get('name') == True:

            #post_data = request.get_json()
            try:

                # check if the user exists
                user1 = session.query(User).filter_by(username=post_data.get('username')).one()
                response_object['name'] = False
            # error
            except:
                response_object['name'] = True
    return jsonify(response_object)




# (get) all the users , (post) add new user
@app.route('/users', methods=['GET', 'POST'])
def noname():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    if request.method == 'POST':
        #try:
            post_data = request.get_json()
            print(post_data.get('username'))
            print(post_data.get('password'))
            print(post_data.get('email'))
            user1 = User(username= post_data.get('username'))
            user1.password = post_data.get('password')
            user1.email = post_data.get('email')
            user1.id = uuid.uuid4().hex
            session.add(user1)
            session.commit()

            response_object['message'] = 'User add!!'

        #except:
            #response_object['message'] = 'User canont add... meaby worng input?'

    if request.method == 'GET':
        users = session.query(User).all()
        response_object['users'] = [i.serialize for i in users]

    return jsonify(response_object)




# (get) get all the groups of a user , (post)add new group to user
@app.route('/groups', methods=['GET', 'POST'])
def all_books():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}
    post_data = request.get_json()


    # add new group

    if request.method == 'POST' and post_data.get('add') == True:
        post_data = request.get_json()
        # details of the group
        group1 = Group(user_id = post_data.get('id'), title=post_data.get('title'), run=post_data.get('run'))
        session.add(group1)
        session.commit()
        # details of the members
        names = (post_data.get('name'))
        #print(names)
        fls = (post_data.get('fl'))
        indexs = (post_data.get('index'))

        for num in range(len(names)):
            member1 = Member(name=names[num], group=group1, group_id=group1.id, fl=fls[num], index=indexs[num])
            session.add(member1)
            session.commit()
        response_object['message'] = 'Group added!'



    # all the groups of a user

    if request.method == 'POST' and post_data.get('get') == True:
        print(post_data.get('username'))
        print(post_data.get('password'))
        try:

            #check if the user exists
            user1 = session.query(User).filter_by(username = post_data.get('username')).one()

            #check if the password is corcct
            if user1.password == post_data.get('password'):

                #getAction
                items = session.query(Group).filter_by(user_id = user1.id).all()
                response_object['groups'] = [i.serialize for i in items]
            else:
                response_object['message'] = 'worng password'

        #error
        except:
            response_object['message'] = 'not vaild useranme'


    return jsonify(response_object)


# CODE END


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)