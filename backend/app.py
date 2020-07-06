#!/usr/bin/python3

'''
UNSW COMP9900 20T2
Capstone Project
Team Salted Fish
Members
Xiaowei Zhou    z5108173
Keyu Yang       z5177443
Lisha Jing      z5243620
Nan Zhao        z5225777
Qingbei Wu      z5222641
'''

import json, yaml
from functools import wraps
from flask import Flask, request
from flask_restplus import Api, abort, fields, inputs, reqparse, marshal
from itsdangerous import JSONWebSignatureSerializer, BadSignature

from db import create_conn
from auth_token import AuthToken
from util import check_email, CorsResource

from users.admin import Admin
from users.dreamer import Dreamer
from users.collaborator import Collaborator

from projects.project import Project
from projects.role import Role
from projects.application import Application
from projects.invitation import Invitation

# Load config
f = open('projects/project.config', 'r', encoding='utf-8')
config = yaml.load(f.read(), Loader=yaml.FullLoader)

# Flask App
app = Flask(__name__)
api = Api(app, authorizations={
    'API-KEY': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'AUTH_KEY'
    },
}, security='API-KEY', default='Dream_Matchmaker', title='Dream Matchmaker', description='Dream Matchmaker, a project posting and collaborator finding system')

# Auth Token
SECRET = "DREAM MATCHMAKER, POWERED BY TEAM SALTED FISH"
expires = 3600
auth = AuthToken(SECRET, expires)

# Auth decorator
def require_auth(f):
    @wraps(f)
    def func(*args, **kwargs):
        token = request.headers.get('AUTH_KEY')
        if not token:
            abort(401, 'Auth Token Missing')
        try:
            userinfo = auth.validate(token)
        except Exception as e:
            abort(401, e)
        return f(*args, **kwargs)

    return func

# Get Parsers
projects_parser = reqparse.RequestParser()
projects_parser.add_argument('description', type=str, default='')
projects_parser.add_argument('category', type=int, default=-1) # -1 for all categories
projects_parser.add_argument('order_by', choices=['last_update','project_title'], default='last_update')
projects_parser.add_argument('sorting', choices=['ASC','DESC'], default='DESC')

# Post Models
login_model = api.model('Login', {
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'role': fields.String(required=True, description='Admin, Dreamer, Collaborator', enum=['Admin','Dreamer','Collaborator'])
})

dreamer_register_model = api.model('Dreamer_Register', {
    'name': fields.String(required=True, description='Your name'),
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'repeat_password': fields.String(required=True, description='Repeat your password', min_length=8),
    'phone_no': fields.String(required=False, description='Phone number (optional)')
})

collaborator_register_model = api.model('Collaborator_Register', {
    'name': fields.String(required=True, description='Your name'),
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'repeat_password': fields.String(required=True, description='Repeat your password', min_length=8),
    'phone_no': fields.String(required=False, description='Phone number (optional)'),
    'education': fields.Integer(required=False, description='Education, 1=Other, 2=Bachelor, 3=Master, 4=PhD'),
    'skills': fields.String(required=False, description='skills(as integer). Format: skill1,skill2,skill3,...', example='2,3,1'),
    'experience': fields.String(required=False, description='experience (in years). Format: exp1,exp2,exp3,...', example='3,2,1')
})

project_post_model = api.model('Project_Post', {
    'title': fields.String(required=True, description='Project title'),
    'description': fields.String(required=True, description='Project description'),
    'category': fields.Integer(required=False, description='Project Category ID')
})

role_post_model = api.model('Role_Post', {
    'title': fields.String(required=True, description='Role title'),
    'amount': fields.Integer(required=True, description='Amount required'),
    'skill': fields.Integer(required=True, description='Skill id'),
    'experience': fields.Integer(required=True, description='Experience required in years'),
    'education': fields.Integer(required=True, description='Education required'),
    'general_enquiry': fields.String(required=False, description='other enquiry')
})

role_patch_model = api.model('Role_Patch', {
    'title': fields.String(required=False, description='Role title'),
    'amount': fields.Integer(required=False, description='Amount required'),
    'skill': fields.Integer(required=False, description='Skill id'),
    'experience': fields.Integer(required=False, description='Experience required in years'),
    'education': fields.Integer(required=False, description='Education required'),
    'general_enquiry': fields.String(required=False, description='other enquiry')
})

change_password_model = api.model('Change_Password', {
    'original_password': fields.String(required=True, description='Your original password', min_length=8),
    'new_password': fields.String(required=True, description='Your new password', min_length=8)
})

apply_role_model = api.model('Apply_Role', {
    'general_text': fields.String(required=True, description='Apply description')
})

invite_role_model = api.model('Invite_Role', {
    'collaborator_id': fields.Integer(required=True, description='Invitee ID'),
    'general_text': fields.String(required=True, description='Invite description')
})

# API
@api.route('/admin')
class AdminAPI(CorsResource):
    @api.response(200, 'Success')
    @api.response(401, 'Auth Failed')
    @api.doc(description="Get Admin data")
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        admin_email = userinfo['email']
        admin_id = userinfo['id']
        admin_role = userinfo['role']
        if admin_role != 'Admin':
            return {'message': 'You are not logged in as admin'}, 401
        return {'email': admin_email}, 200

@api.route('/categories')
class Categories(CorsResource):
    @api.response(200, 'Success')
    @api.doc(description="Get project categories list")
    def get(self):
        return {"categories": config['Project']['Categories'], "description": config['Project']['Categories_description']}, 200

@api.route('/skills')
class Skills(CorsResource):
    @api.response(200, 'Success')
    @api.doc(description="Get collaborator skills list")
    def get(self):
        return {"skills": config['Role']['Skills']}, 200

@api.route('/projects')
class ProjectsList(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.doc(description="Get projects list filtered by arguments")
    @api.expect(projects_parser, validate=True)
    def get(self):
        args = projects_parser.parse_args()
        desc = args.get('description')
        category = args.get('category')
        order_by = args.get('order_by')
        sorting = args.get('sorting')
        result = Project.search_list(conn, desc, category, order_by, sorting)
        if result is None:
            return {'projects': [], 'message': 'No matching projects were found.'}, 200
        return result, 200

@api.route('/dreamer/my_projects')
class DreamerOwnProjectsList(CorsResource):
    @api.response(200, 'Success')
    @api.response(401, 'Auth Failed')
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        my_user_id = Dreamer.getObject(conn, userinfo['email']).info()['id']
        result = Project.get_by_owner(conn, my_user_id)
        if result is None:
            return {'projects': [], 'message': 'You have not create any projects'}, 200
        return {'projects': result}, 200

@api.route('/collaborator/projects')
class CollaboratorProjectsList(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.response(401, 'Auth Failed')
    @api.expect(projects_parser, validate=True)
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 401
        email = userinfo['email']
        my_user = Collaborator.getObject(conn, email)
        args = projects_parser.parse_args()
        desc = args.get('description')
        category = args.get('category')
        order_by = args.get('order_by')
        sorting = args.get('sorting')
        result = my_user.search_list(conn, desc, category, order_by, sorting)
        if result is None:
            return {'projects': [], 'message': 'No matching projects were found.'}, 200
        return result, 200

@api.route('/collaborator/recommendation')
class ProjectsRecommendation(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.response(401, 'Auth Failed')
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 401
        email = userinfo['email']
        my_user = Collaborator.getObject(conn, email)
        result = my_user.projects_recommdation(conn)
        if result is None:
            return {'projects': [], 'message': 'No matching projects were found.'}, 200
        return result, 200

@api.route('/dreamer/recommendation')
class CollaboratorsRecommendation(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.response(401, 'Auth Failed')
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        email = userinfo['email']
        my_user = Dreamer.getObject(conn, email)
        result = my_user.collaborators_recommdation(conn)
        if result is None:
            return {'collaborators': [], 'message': 'No matching collaborators were found.'}, 200
        return result, 200

@api.route('/project/<int:id>/finish')
@api.param('id', 'The project id')
class DreamerFinishProject(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Failed to finish the project')
    @api.response(401, 'Auth Failed')
    @api.response(404, 'Project not found')
    @api.doc(description='Finish a project')
    def get(self, id):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        #email = userinfo['email']
        #my_user = Dreamer.getObject(conn, email)
        dreamer_id = userinfo['id']
        result1 = Project.get_by_id(conn, int(id))
        if result1 is None:
            return {'message': 'Requesting non-existing project information'}, 404
        result = Project.finish_a_project(conn, int(id), dreamer_id)
        if result['status'] != 9:
            return {'message': 'Failed to finish the project'}, 400
        return result, 200

@api.route('/collaborator/invitations')
class InvitationsReceived(CorsResource):
    @api.response(200, 'Success')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Show invitations I received')
    @require_auth
    def get(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        collaborator_id = userinfo['id']
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 401
        result = Invitation.get_by_invitee(conn, collaborator_id)
        return result, 200

@api.route('/project/<int:pID>/role/<int:rID>/invitation')
@api.param('pID', 'The project id')
@api.param('rID', 'The project_role id')
class InviteRole(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Invite a collaborator for a role')
    @api.expect(invite_role_model, validate=True)
    @require_auth
    def post(self, pID, rID):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        invite_info = request.json
        try:
            general_text = invite_info['general_text']
        except:
            general_text = ''
        new_invite = Invitation(int(pID), int(rID), dreamer_id, invite_info['collaborator_id'], general_text=general_text).create(conn)
        if new_invite == None:
            return {'message': 'invite role duplicate'}, 400
        return {'message': 'role invite success', 'project_id': int(pID), 'project_role_id': int(rID), 'invitation_id': new_invite.info()['id']}, 200

@api.route('/project/<int:pid>/role/<int:rid>/invitation/<int:iid>/accept')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
@api.param('iid', 'The invitation id')
class AcceptAnInvitation(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Auth Failed')
    @api.response(401, 'Invitation not found')
    @api.response(404, 'Failed to accept an invitation')
    @api.doc(description='Accept an invitation')
    def get(self, pid, rid, iid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 400
        result_1 = Invitation.get_by_iid(conn, int(iid))
        if result_1 is None:
            return {'message': 'Invitation not found'}, 401
        result = Invitation.accept_an_invitation(conn, int(iid))
        if result['invite_status'] != 1:
            return {'message': 'Failed to accept an invitation'}, 404            
        return result, 200

@api.route('/project/<int:pid>/role/<int:rid>/invitation/<int:iid>/decline')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
@api.param('iid', 'The invitation id')
class DeclineAnInvitation(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Auth Failed')
    @api.response(401, 'Invitation not found')
    @api.response(404, 'Failed to decline an invitation')
    @api.doc(description='Decline an invitation')
    def get(self, pid, rid, iid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 400
        result_1 = Invitation.get_by_iid(conn, int(iid))
        if result_1 is None:
            return {'message': 'Invitation not found'}, 401
        result = Invitation.decline_an_invitation(conn, int(iid))
        if result['invite_status'] != 0:
            return {'message': 'Failed to decline an invitation'}, 404            
        return result, 200

@api.route('/project/<int:pid>/role/<int:rid>/appllication')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
class ApplyRole(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Apply a new role for the project')
    @api.expect(apply_role_model, validate=True)
    @require_auth
    def post(self, pid, rid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        collaborator_id = userinfo['id']
        if userinfo['role'] != 'Collaborator':
            return {'message': 'You are not logged in as collaborator'}, 401
        apply_info = request.json
        try:
            general_text = apply_info['general_text']
        except:
            general_text = ''
        new_apply = Application(int(pid), int(rid), collaborator_id,general_text=general_text).create(conn)
        if new_apply == None:
            return {'message': 'apply role duplicate'}, 400
        return {'message': 'role apply success', 'project id': int(pid),'project_role_id': int(rid), 'apply_id': new_apply.info()['id']}, 200

@api.route('/project/<int:pid>/role/<int:rid>/application/<int:aid>')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
@api.param('aid', 'The application id')
class ViewSingleApplication(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.response(404, 'Application not found')
    @api.doc(description=' View applications for each role')
    def get(self, pid,rid,aid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        if not Project.check_owner(conn, pid, dreamer_id):
            return {'message': 'You are not the owner of the project'}, 400
        result = Application.get_by_aid(conn, int(aid))
        if result is None:
            return {'message': 'Application not found'}, 404
        return result, 200
    
@api.route('/project/<int:pid>/role/<int:rid>/application')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
class ViewAllApplication(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.response(404, 'Application not found')
    @api.doc(description=' View applications for each role')
    def get(self, pid,rid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        if not Project.check_owner(conn, pid, dreamer_id):
            return {'message': 'You are not the owner of the project'}, 400
        result = Application.get_by_pid_rid(conn,int(pid),int(rid))
        if result is None:
            return {'message': 'Application not found'}, 404
        return result, 200

@api.route('/project/<int:pid>/role/<int:rid>/application/<int:aid>/approve')
@api.param('pid', 'The project id')
@api.param('rid', 'The project_role id')
@api.param('aid', 'The application id')
class ApproveAnApplication(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.response(404, 'Application not found')
    @api.response(405, 'Failed to approve an application')
    @api.doc(description='Approve an application')
    def get(self, pid, rid, aid):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if userinfo['role'] != 'Dreamer':
            return {'message': 'You are not logged in as dreamer'}, 401
        if not Project.check_owner(conn, pid, dreamer_id):
            return {'message': 'You are not the owner of the project'}, 400
        result_1 = Application.get_by_aid(conn, int(aid))
        if result_1 is None:
            return {'message': 'Application not found'}, 404
        result = Application.approve_an_application(conn, int(aid))
        if result['apply_status'] != 1:
            return {'message': 'Failed to approve an application'}, 405            
        return result, 200
    
@api.route('/project/<int:id>')
@api.param('id', 'The project id')
class GetProject(CorsResource):
    @api.response(200, 'Success')
    @api.response(404, 'Project not found')
    @api.doc(description='Get project information')
    def get(self, id):
        result = Project.get_by_id(conn, int(id))
        if result is None:
            return {'message': 'Requesting non-existing project information'}, 404
        return result, 200

@api.route('/project/<int:id>/role')
@api.param('id', 'The project id')
class PostRole(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Post a new role for the project')
    @api.expect(role_post_model, validate=True)
    @require_auth
    def post(self, id):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if not Project.check_owner(conn, int(id), dreamer_id):
            return {'message': 'You are not the owner of the project'}, 400
        role_info = request.json
        try:
            general_enquiry = role_info['general_enquiry']
        except:
            general_enquiry = ''
        new_role = Role(int(id), role_info['title'], role_info['amount'], role_info['skill'], role_info['experience'], role_info['education'], general_enquiry=general_enquiry).create(conn)
        if new_role == None:
            return {'message': 'role create duplicate'}, 400
        return {'message': 'role create success', 'project_id': int(id), 'role_id': new_role.info()['id']}, 200

@api.route('/project/<int:pID>/role/<int:rID>')
@api.param('pID', 'The project id')
@api.param('rID', 'The role id')
class PatchRole(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Update a role information')
    @api.expect(role_patch_model, validate=True)
    @require_auth
    def patch(self, pID, rID):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        if not Project.check_owner(conn, int(pID), dreamer_id):
            return {'message': 'You are not the owner of the project'}, 400
        role_info = request.json
        cursor_role = Role.get_object_by_id(conn, int(rID))
        try:
            cursor_role.title = role_info['title']
        except:
            pass
        try:
            cursor_role.amount = role_info['amount']
        except:
            pass
        try:
            cursor_role.skill = role_info['skill']
        except:
            pass
        try:
            cursor_role.experience = role_info['experience']
        except:
            pass
        try:
            cursor_role.education = role_info['education']
        except:
            pass
        try:
            cursor_role.general_enquiry = role_info['general_enquiry']
        except:
            pass
        result = cursor_role.patch(conn).info()
        return {'message': 'Patch success', 'info': result}, 200

@api.route('/project')
class PostProject(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Post a new project')
    @api.expect(project_post_model, validate=True)
    @require_auth
    def post(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        dreamer_id = userinfo['id']
        project_info = request.json
        new_project = Project(project_info['title'], project_info['description'], dreamer_id, project_info['category']).create(conn)
        if new_project == None:
            return {'message': 'project create request duplicate'}, 400
        return {'message': 'project create success', 'project_id': new_project.info()['id']}, 200

@api.route('/collaborator/register')
class CollaboratorRegister(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Register Failed')
    @api.doc(description='Register a new collaborator')
    @api.expect(collaborator_register_model, validate=True)
    def post(self):
        register_info = request.json
        name = register_info['name']

        email = register_info['email']
        if not check_email(email):
            return {'message': 'Email not valid.'}, 400

        if Collaborator.is_email_exist(conn, email):
            return {'message': 'Email already registered.'}, 400

        password = register_info['password']
        if password != register_info['repeat_password']:
            return {'message': 'Passwords not match.'}, 400

        try:
            phone_no = register_info['phone_no']
        except:
            phone_no = ''

        try:
            education = register_info['education']
        except:
            education = -1

        skill_dict = {}
        try:
            skills = register_info['skills'].split(',')
            exps = register_info['experience'].split(',')
            print(skills, exps)
            if not (len(skills) == len(exps)): return {'message': 'Skills and experience have different length.'}, 400
            for i in range(len(skills)):
                skill_dict[skills[i]]=exps[i]
        except:
            skill_dict = {}
        print(skill_dict)
        Collaborator(name, email, password_plain=password, phone_no=phone_no, education=education, skill_dict=skill_dict).commit(conn)

        return {'message': 'Register success'}, 200

@api.route('/dreamer/register')
class DreamerRegister(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Register Failed')
    @api.doc(description='Register a new dreamer')
    @api.expect(dreamer_register_model, validate=True)
    def post(self):
        register_info = request.json
        name = register_info['name']

        email = register_info['email']
        if not check_email(email):
            return {'message': 'Email not valid.'}, 400

        if Dreamer.is_email_exist(conn, email):
            return {'message': 'Email already registered.'}, 400

        password = register_info['password']
        if password != register_info['repeat_password']:
            return {'message': 'Passwords not match.'}, 400

        try:
            phone_no = register_info['phone_no']
        except:
            phone_no = ''

        Dreamer(name, email, password_plain=password, phone_no=phone_no).commit(conn)

        return {'message': 'Register success'}, 200

@api.route('/login')
class Login(CorsResource):
    @api.response(200, 'Success')
    @api.response(401, 'Login Failed')
    @api.doc(description='Login with email and password, receive an auth token')
    @api.expect(login_model, validate=True)
    def post(self):
        login_info = request.json
        email = login_info['email']
        password = login_info['password']
        # try login based on role
        role = login_info['role']
        if role == 'Admin':
            user = Admin.login(conn, email, password)
        elif role == 'Dreamer':
            user = Dreamer.login(conn, email, password)
        elif role == 'Collaborator':
            user = Collaborator.login(conn, email, password)
        # login failed
        if user is None:
            return {'message': 'Login failed for incorrect credentials.'}, 401
        else:
            token = auth.token(user).decode()
            return {'token': token}, 200

@api.route('/changepassword')
class ChangePassword(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Validate Failed')
    @api.response(401, 'Auth Failed')
    @api.doc(description='Change your password')
    @api.expect(change_password_model, validate=True)
    @require_auth
    def post(self):
        token = request.headers.get('AUTH_KEY')
        userinfo = auth.decode(token)
        role = userinfo['role']
        email = userinfo['email']
        password_info = request.json
        original_password = password_info['original_password']
        new_password = password_info['new_password']
        if original_password == new_password:
            return {'message': 'new password should be different'}, 400
        if role == 'Admin':
            if not Admin.check_password(conn, email, original_password):
                return {'message': 'Your original_password is incorrect'}, 400
            Admin.commit_newpassword(conn,email,new_password)
        elif role == 'Dreamer':
            if not Dreamer.check_password(conn, email, original_password):
                return {'message': 'Your original_password is incorrect'}, 400
            Dreamer.commit_newpassword(conn,email,new_password)
        elif role == 'Collaborator':
            if not Collaborator.check_password(conn, email, original_password):
                return {'message': 'Your original_password is incorrect'}, 400
            Collaborator.commit_newpassword(conn,email,new_password)
        return {'message': 'change password success'}, 200


if __name__ == '__main__':
    conn = create_conn()
    app.run(debug=True)
