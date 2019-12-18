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
#copy from git

#(GET) get a specific list of member inside a group, (POST) add new member to a specific group ,
#(PUT) update a specific group and members detail , (DELETE) delete group
@app.route('/group/<group_ids>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def FUCK(group_ids):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}


    #delete group

    if request.method == 'DELETE':
        #delte group
        groupD = session.query(Group).filter_by(id = group_ids).one()
        session.delete(groupD)
        session.commit()
        #delte all members of the group
        membersD = session.query(Member).filter_by(group_id = group_ids).all()
        #print(membersD)
        for member in membersD:
            #print("name: " + member.name)
            #member.id = str(member.id)
            #print("id: " + member.id)
            session.delete(member)
            session.commit()
        response_object['message'] = 'Group deleted!!'



    # update a specific group and members detail

    if request.method == 'PUT':
        group1 = session.query(Group).filter_by(id=group_ids).one()
        group1.run += 1
        session.add(group1)
        session.commit()
        post_data = request.get_json()

        indexs = post_data.get('index')
        #ALSO change fl
        if post_data.get('fairrandom') == True:
            member1 = session.query(Member).filter_by(group_id=group_ids).all()
            for num in range(len(indexs)):
                place = 0
                for item in member1:
                    if place == num:
                        item.index = indexs[num]
                        if item.index == 0 or item.index == (len(indexs) -1):
                            item.fl += 1
                        session.add(item)
                        session.commit()
                        break
                    if place > num:
                        break
                    else:
                        place += 1
        #NOT change fl
        else:
            member1 = session.query(Member).filter_by(group_id=group_ids).all()
            for num in range(len(indexs)):
                place = 0
                for item in member1:
                    if place == num:
                        item.index = indexs[num]
                        #if item.index == 0 or item.index == (len(indexs) - 1):
                            #item.fl += 1
                        session.add(item)
                        session.commit()
                        break
                    if place > num:
                        break
                    else:
                        place += 1

        response_object['message'] = 'Mambers and Group Updated!!'



    #add new member to a specific group

    if request.method == 'POST':
        post_data = request.get_json()
        itemA = Member(group_id=group_ids)
        items = session.query(Member).filter_by(group_id=group_ids).all()
        for item in items:
            item.index += 1
            session.add(item)
            session.commit()
        itemA.name = post_data.get('name')
        itemA.fl = post_data.get('fl')
        itemA.index = post_data.get('index')
        session.add(itemA)
        session.commit()

        response_object['message'] = 'Mamber added!'



    # get a specific list of member inside a group

    if request.method == 'GET':
        items = session.query(Member).filter_by(group_id=group_ids).all()
        indexs = []
        for item in items:
            indexs.append(item.index)
        # to orginaze by sort index
        j = sorted(indexs)
        name = []
        for cuc in range(len(j)):
            for item in items:
                if item.index == j[cuc]:
                    name.append(item.serialize)
                    break
        response_object['Member'] = name
    return jsonify(response_object)



#(post) update the login state (put) updat user detail?
@app.route('/login', methods=['POST', 'PUT'])
def login():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    #update the login state
    if request.method == 'POST':
        post_data = request.get_json()
        try:

            if post_data.get('login') == 'True':
                #updat login state to TRUE
                user1 = session.query(User).filter_by(username=post_data.get('username')).one()
                if user1.password == post_data.get('password'):
                    user1.login = post_data.get('login')
                    session.add(user1)
                    session.commit()
                    response_object['userInfo'] = user1.id

                else:
                    #worng password
                    response_object['message'] = 'wrong password'

            else:
                #update login state to FALSE
                user1 = session.query(User).filter_by(id = post_data.get('id')).one()
                user1.login = 'False'
                session.add(user1)
                session.commit()
                response_object['message'] = 'user logout'


        except:
            #worng username/ ERROR
            response_object['message'] = 'not vaild username'

    ## updat user detail
    # if request.method == 'PUT':
    #     post_data = request.get_json()
    #     try:
    #         user1 = session.query(User).filter_by(username=post_data.get('old_username')).one()
    #         user1.username = post_data.get('new_username')
    #         #always?
    #         user1.password = post_data.get('password')
    #         #always?
    #         user1.email = post_data.get('email')
    #         session.add(user1)
    #         session.commit()
    #         #response_object update yeee
    #     except:
    #         pass
    #         #response_object worng username / ERROR


    return jsonify(response_object)




#(get) groups of a user

@app.route('/groups/<user1_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def groups(user1_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    #groups of a user
    if request.method == 'GET':
        try:

            items = session.query(Group).filter_by(user_id = user1_id).all()
            #not serialize by index;
            response_object['groups'] = [i.serialize for i in items]

        except:
            response_object['id_error'] = True

    return jsonify(response_object)



#(get) the state of the user, #(post) add group to the user -only rache to that if the user login,

@app.route('/user/<user1_id>' , methods= ['GET', 'POST'])
def menuItemJSON(user1_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    #get the state of the user
    if request.method == 'GET':

        try:
            user1 = session.query(User).filter_by(id = user1_id).one()
            if user1.login == 'False':

                response_object['login'] = 'False'
                #response_object he is logout so.....
            if user1.login == 'True':

                response_object['login'] = 'True'
                #response_object list of the group
            else:

                response_object['data_error'] = True
                #response_object need rastart to the data
        except:

            response_object['id_error'] = True
            #response_object worng id / ERROR


    #add group to the user
    if request.method == 'POST':
        post_data = request.get_json()
        try:
            user1 = session.query(User).filter_by(id = user1_id).one()
            # details of the group
            group1 = Group(user_id = user1_id , title=post_data.get('title'), run=post_data.get('run'))
            session.add(group1)
            session.commit()
            #DO YOU NEED THAT?
            # details of the members
            names = (post_data.get('name'))
            fls = (post_data.get('fl'))
            indexs = (post_data.get('index'))

            for num in range(len(names)):
                member1 = Member(name=names[num], group=group1, group_id=group1.id, fl=fls[num], index=indexs[num])
                session.add(member1)
                session.commit()
            response_object['message'] = 'Group added!'


        except:
            response_object['id_error/informison past'] = True
            #response_object worng id / ERROR



    return jsonify(response_object)




# (PUT) edit a specific member, (DELETE) delete a specific member and updeat the rest fo the group automatic
@app.route('/group/<member_ids>/member', methods=['PUT', 'DELETE'])
def updet_member(member_ids):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}


    # edit a specific member

    if request.method == 'PUT':
        # specific the group
        item = session.query(Member).filter_by(id=member_ids).one()
        post_data = request.get_json()
        # details of the member
        if post_data.get('name'):
            item.name = post_data.get('name')
        if post_data.get('fl'):
            item.fl = post_data.get('fl')
        if post_data.get('index'):
            item.index = post_data.get('index')
        session.add(item)
        session.commit()
        response_object['message'] = 'Group added!'


    # delete a specific member and updeat the rest fo the group automatic

    if request.method == 'DELETE':
        ditem = session.query(Member).filter_by(id=member_ids).one()
        idG = ditem.group_id
        amout = ditem.index
        #delete a specific member
        session.delete(ditem)
        session.commit()
        items = session.query(Member).filter_by(group_id = idG).all()
        #updeat the rest fo the group automatic
        for item in items:
            if amout < item.index:
                item.index -= 1
                session.add(item)
                session.commit()

        response_object['message'] = 'Member removed!'


    return jsonify(response_object)


# check if username or email is valid or not whan SIGN UP
@app.route('/check', methods=['GET', 'POST'])
def check():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}

    if request.method == 'GET':
        response_object['message'] = None

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




#(post) add new user
@app.route('/users', methods=['POST'])
def noname():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}



    if request.method == 'POST':
        try:
            post_data = request.get_json()
            user1 = User(username= post_data.get('username'))
            user1.password = post_data.get('password')
            user1.email = post_data.get('email')
            user1.id = uuid.uuid4().hex
            session.add(user1)
            session.commit()

            response_object['userInfo'] = user1.id


        except:
            response_object['message'] = 'User canont add...'


    return jsonify(response_object)


#CODE END


if __name__ == '__main__':
    app.debug = True
    app.run()