#!/usr/bin/python3

from users.util import sha256
from projects.project import Project

class Dreamer():
    def __init__(self, name, email, password_plain='', password_encrypted='', id='', create_time='', last_update='', phone_no='', user_level=0, description=''):
        self.name = name
        self.email = email.lower()
        if password_encrypted == '':
            self.password_encrypted = sha256(password_plain)
        else:
            self.password_encrypted = password_encrypted
        self.id = id
        self.phone_no = phone_no
        self.user_level = user_level
        self.description = description
        self.create_time = create_time
        self.last_update = last_update
        self.level_text='Entry'
        if self.user_level >= 20: self.level_text='Expert'
        elif self.user_level >= 10: self.level_text='Professional'
        elif self.user_level >= 5: self.level_text='Senior'
        elif self.user_level >= 3: self.level_text='Medium'


    @staticmethod
    def login(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            return Dreamer(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description']).info()
        return None

    @staticmethod
    def is_email_exist(conn, email):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        return result.rowcount

    @staticmethod
    def getObject(conn, email):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        return Dreamer(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description'])

    def collaborators_recommdation(self, conn):
        owner = self.id
        roles_needed = {}
        proj_role_collaborator_list = []
        query = "SELECT project_role.ID as roleID, project_role.projectID as proj_ID, project_role.skill as ski, project_role.experience as exp, project_role.education as edu FROM project, project_role WHERE project.ID = project_role.projectID and project.dreamerID = " + str(owner) + " ORDER BY project_role.ID asc;"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        for i in range(result.rowcount):
            row = result.fetchone()
            roles_needed[row['roleID']] = (row['proj_ID'], row['ski'], row['exp'], row['edu'],)
        #strict matching
        strict_matching_count = 0
        for role_i in roles_needed:
            print(roles_needed[role_i])
            query = "select collaborator.ID as ID, name, email, phone_no, education, skill, experience, user_level, description from collaborator, skills where collaborator.ID = skills.collaboratorID and skill = " + str(roles_needed[role_i][1]) + " and experience = " + str(roles_needed[role_i][2]) + " and education = " + str(roles_needed[role_i][3]) + " ORDER BY ID;"
            result = conn.execute(query)
            if result.rowcount != 0:
                for j in range(result.rowcount):
                    row = result.fetchone()
                    collabor = (row['ID'],row['name'],row['email'],row['phone_no'],row['education'],row['skill'],row['experience'],row['user_level'],row['description'])
                    proj_role_info = Project.get_by_id_skill(conn, roles_needed[role_i][0], roles_needed[role_i][1])
                    proj_role_collaborator_list.append((proj_role_info, collabor))
                    strict_matching_count += 1
        #relaxing matching
        relaxing_matching_count = 0
        for role_i in roles_needed:
            print(roles_needed[role_i])
            query = "select collaborator.ID as ID, name, email, phone_no, education, skill, experience, user_level, description from collaborator, skills where collaborator.ID = skills.collaboratorID and skill = " + str(roles_needed[role_i][1]) + " and experience >= " + str(roles_needed[role_i][2] - 1) + " and education >= " + str(roles_needed[role_i][3] - 1) + " ORDER BY experience Desc, education Desc;"
            result = conn.execute(query)
            if result.rowcount != 0:
                for j in range(result.rowcount):
                    row = result.fetchone()
                    collabor = (row['ID'],row['name'],row['email'],row['phone_no'],row['education'],row['skill'],row['experience'],row['user_level'],row['description'])
                    proj_role_info = Project.get_by_id_skill(conn, roles_needed[role_i][0], roles_needed[role_i][1])
                    proj_role_collaborator_list.append((proj_role_info, collabor))
                    relaxing_matching_count += 1
        if len(proj_role_collaborator_list) == 0: return None
        return {'project-role-collaborator': proj_role_collaborator_list, 'strict matching count': strict_matching_count, 'relaxing matching count': relaxing_matching_count}

    @staticmethod
    def check_password(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            return True
        return False
    
    @staticmethod
    def commit_newpassword(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        if password_encrypted == '':
            new_pass = sha256(password_plain)
        else:
            new_pass = password_encrypted
        query = "UPDATE dreamer set password = \'" + new_pass + "\' where email = \'" + email + "\';"
        conn.execute(query)
    

    def info(self):
        return {'role': 'Dreamer', 'name': self.name, 'email': self.email, 'id': self.id, 'creation_time': self.create_time, 'last_update': self.last_update, 'phone_no': self.phone_no, 'user_level': self.level_text, 'description': self.description}


    def commit(self, conn):
        query = "INSERT INTO dreamer (name, email, password, phone_no, user_level, description) VALUES (\'" + self.name + "\', \'" + self.email + "\', \'" + self.password_encrypted + "\', \'" + self.phone_no + "\', " + str(self.user_level) + ", \'" + self.description + "\') ON DUPLICATE KEY UPDATE `name`= \'" + self.name + "\', `password` = \'" + self.password_encrypted + "\', `phone_no` = \'" + self.phone_no + "\', `user_level` = " + str(self.user_level) + ", `description` = \'" + self.description + "\';"
        conn.execute(query)
