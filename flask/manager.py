import os
from flask import Flask, render_template, session, redirect, url_for, flash ,make_response
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
import json
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from flask.ext.migrate import Migrate ,MigrateCommand
from flask.json import jsonify
from flask.ext.restful import Api,Resource,reqparse
import wx_login_2
import wx_login3
import threading

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
api =Api(app)


#api
class Index(Resource):
    def get(self):
        order = Group.query.order_by(Group.cnt.desc()).all()
        project = Spider.query.order_by(Spider.cnt.desc()).all()
        print order[9].name
        testJson = [
            [
                {
                    "name": order[0].name,
                    "votes": order[0].cnt 
                    },
                {
                    "name": order[1].name,
                    "votes": order[1].cnt 
                    },
                {
                    "name": order[2].name,
                    "votes": order[2].cnt  
                    },
                {
                    "name": order[3].name,
                    "votes": order[3].cnt 
                    },
                {
                    "name": order[4].name,
                    "votes": order[4].cnt  
                    },
                {
                    "name": order[5].name,
                    "votes": order[5].cnt 
                    },
                {
                    "name": order[6].name,
                    "votes": order[6].cnt  
                    },
                {
                    "name": order[7].name,
                    "votes": order[7].cnt  
                    },
                {
                    "name": order[8].name,
                    "votes": order[8].cnt  
                    },
                {
                    "name": order[9].name,
                    "votes": order[9].cnt 
                    }
                ],
            [
                {
                    "name": project[0].name,
                    "votes": project[0].cnt 
                    },
                {
                    "name": project[1].name,
                    "votes": project[1].cnt 
                    },
                {
                   "name": project[2].name,
                    "votes": project[2].cnt 
                    },
                {
                    "name": project[3].name,
                    "votes": project[3].cnt  
                    },
                {
                    "name": project[4].name,
                    "votes": project[4].cnt 
                    },
                {   
                    "name": project[5].name,
                    "votes": project[5].cnt 
                    },
                {
                    "name": project[6].name,
                    "votes": project[6].cnt  
                    },
                {
                    "name": project[7].name,
                    "votes": project[7].cnt  
                    },
                {
                    "name": project[8].name,
                    "votes": project[8].cnt 
                    },
                {
                    "name": project[9].name,
                    "votes": project[9].cnt 
                    }
                ]
            ]
        return jsonify(testJson)
class Team(Resource):
    def get(self):
            order = Group.query.order_by(Group.cnt.desc()).all()
            dicts = {}
            # print order[3].name
            for i in range(10):
                dicts.setdefault(order[i].name,order[i].cnt)
                # print(order[i].name)
            return dicts
api.add_resource(Index,'/index')
api.add_resource(Team,'/team')
#Model
class Spider(db.Model):
    __tablename__ = 'spider'
    id = db.Column(db.Integer,primary_key=True)
    num = db.Column(db.Integer)
    name = db.Column(db.String(64),index=True)
    cnt = db.Column(db.Integer)
    group = db.Column(db.String(64))
    intro = db.Column(db.String(128))

class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer,primary_key=True)
    num = db.Column(db.Integer)
    name = db.Column(db.String(64),index=True)
    cnt = db.Column(db.Integer)
    intro = db.Column(db.String(128))

#Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#Route
@app.route('/', methods=['GET', 'POST'])
def mobile():
    return render_template('index.html')

@app.route('/getData', methods=['get'])
def getData():
    order = Group.query.order_by(Group.cnt.desc()).all()
    project = Spider.query.order_by(Spider.cnt.desc()).all()
    print order[9].name
    testJsons = [
            [
                {
                    "name": order[0].name,
                    "votes": order[0].cnt 
                    },
                {
                    "name": order[1].name,
                    "votes": order[1].cnt 
                    },
                {
                    "name": order[2].name,
                    "votes": order[2].cnt  
                    },
                {
                    "name": order[3].name,
                    "votes": order[3].cnt 
                    },
                {
                    "name": order[4].name,
                    "votes": order[4].cnt  
                    },
                {
                    "name": order[5].name,
                    "votes": order[5].cnt 
                    },
                {
                    "name": order[6].name,
                    "votes": order[6].cnt  
                    },
                {
                    "name": order[7].name,
                    "votes": order[7].cnt  
                    },
                {
                    "name": order[8].name,
                    "votes": order[8].cnt  
                    },
                {
                    "name": order[9].name,
                    "votes": order[9].cnt 
                    }
                ],
            [
                {
                    "name": project[0].name,
                    "votes": project[0].cnt 
                    },
                {
                    "name": project[1].name,
                    "votes": project[1].cnt 
                    },
                {
                   "name": project[2].name,
                    "votes": project[2].cnt 
                    },
                {
                    "name": project[3].name,
                    "votes": project[3].cnt  
                    },
                {
                    "name": project[4].name,
                    "votes": project[4].cnt 
                    },
                {   
                    "name": project[5].name,
                    "votes": project[5].cnt 
                    },
                {
                    "name": project[6].name,
                    "votes": project[6].cnt  
                    },
                {
                    "name": project[7].name,
                    "votes": project[7].cnt  
                    },
                {
                    "name": project[8].name,
                    "votes": project[8].cnt 
                    },
                {
                    "name": project[9].name,
                    "votes": project[9].cnt 
                    }
                ]
            ]
           
    return jsonify(testJsons)



def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    t1 = threading.Thread(target=wx_login3.spider)
    t2 = threading.Thread(target=wx_login_2.spider)
    t2.start()
    t1.start()
    manager.run()
