from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Group, Member

# Basic

app = Flask(__name__)
app.config.from_object(__name__)

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CORS(app, resources={r'/*': {'origins': '*'}})


# CODE START


# (GET) get a specific list of member inside a group, (POST) add new member to a specific group , 
#(PUT) update a specific group and members detail , (DELETE) delete group


@app.route('/group/<group_ids>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def menuItemJSON(group_ids):
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





# (get) get all the groups , (post)add new group
@app.route('/groups', methods=['GET', 'POST'])
def all_books():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    response_object = {'status': 'success'}


    # add new group

    if request.method == 'POST':
        post_data = request.get_json()
        # details of the group
        group1 = Group(title=post_data.get('title'), run=post_data.get('run'))
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


    # all the groups

    if request.method == 'GET':
        items = session.query(Group).all()
        response_object['groups'] = [i.serialize for i in items]
        # return jsonify(Group=[i.id for i in items])
    return jsonify(response_object)





# (put) edit a specific member, (delete) delete a specific member and updeat the rest fo the group automatic
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




# CODE END


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
