#!/usr/bin/python3

from users.util import sha256
from projects.project import Project

class Collaborator():
    def __init__(self, name, email, password_plain='', password_encrypted='', id='', create_time='', last_update='', phone_no='', user_level=0, description='', education=-1, skill_dict={}):
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
        if self.user_level >= 15: self.level_text='Expert'
        elif self.user_level >= 8: self.level_text='Professional'
        elif self.user_level >= 5: self.level_text='Senior'
        elif self.user_level >= 3: self.level_text='Medium'
        self.education = education
        self.education_text='Default'
        if self.education == 1: self.education_text='Other'
        elif self.education == 2: self.education_text='Bachelor'
        elif self.education == 3: self.education_text='Master'
        elif self.education == 4: self.education_text='PhD'
        self.skill_dict = skill_dict

    @staticmethod
    def getSkills(conn, id):
        skills = {}
        query = "select skill, experience from skills where collaboratorID = " + str(id) + ";"
        result = conn.execute(query)
        if result.rowcount != 0:
            for i in range(result.rowcount):
                row = result.fetchone()
                skills[row['skill']] = row['experience']
        return skills

    @staticmethod
    def is_email_exist(conn, email):
        email = email.lower()
        query = "select * from collaborator where email = \'" + email + "\';"
        result = conn.execute(query)
        return result.rowcount

    @staticmethod
    def login(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from collaborator where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            skills = Collaborator.getSkills(conn, row['ID'])
            return Collaborator(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description'], education=row['education'], skill_dict=skills).info()
        return None

    @staticmethod
    def getObject(conn, email):
        email = email.lower()
        query = "select * from collaborator where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        skills = Collaborator.getSkills(conn, row['ID'])
        return Collaborator(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description'], education=row['education'], skill_dict=skills)

    @staticmethod
    def check_password(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from collaborator where email = \'" + email + "\';"
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
        query = "UPDATE collaborator set password = \'" + new_pass + "\' where email = \'" + email + "\';"
        conn.execute(query)

    def search_list(self, conn, description, category, order_by, order):
        skills = self.skill_dict
        edu = self.education
        project_list = []
        for skill, exp in skills.items():
            print(skill, exp, edu)
            if category == -1:
                query = "SELECT project.ID as pID, project_role.ID as rID, project_title, project.last_update as last_update FROM project, project_role WHERE project.ID = projectID AND description LIKE \'%%" + description + "%%\' AND skill = " + str(skill) + " AND experience <= " + str(exp) + " AND education <= " + str(edu) + " ORDER BY " + order_by + " " + order + ";"
            else:
                query = "SELECT project.ID as pID, project_role.ID as rID, project_title, project.last_update as last_update FROM project, project_role WHERE project.ID = projectID AND description LIKE \'%%" + description + "%%\' AND category = " + str(category) + " AND skill = " + str(skill) + " AND experience <= " + str(exp) + " AND education <= " + str(edu) + " ORDER BY " + order_by + " " + order + ";"
            result = conn.execute(query)
            for i in range(result.rowcount):
                row = result.fetchone()
                proj = Project.get_by_id(conn, row['pID'])
                is_exist = False
                for project in project_list:
                    if project['id'] == proj['id']: is_exist = True
                if not is_exist:
                    project_list.append(proj)
        if len(project_list) == 0: return None
        return {'projects': project_list, 'amount': result.rowcount}

    def projects_recommdation(self, conn):
        skills = self.skill_dict
        edu = self.education
        project_list = []
        #strict matching
        strict_matching_count = 0
        for skill, exp in skills.items():
            query = "SELECT projectID as pID FROM project_role WHERE skill = " + str(skill) + " AND experience = " + str(exp) + " AND education = " + str(edu) + " ORDER BY experience;"
            result = conn.execute(query)
            for i in range(result.rowcount):
                row = result.fetchone()
                proj = Project.get_by_id_skill(conn, row['pID'])
                is_exist = False
                for project in project_list:
                    if project['id'] == proj['id'] and skill == proj['roles.skill']: 
                        is_exist = True
                if not is_exist:
                    project_list.append(proj)
                    strict_matching_count += 1
        #relaxing matching
        relaxing_matching_count = 0
        for skill, exp in skills.items():
            query = "SELECT projectID as pID FROM project_role WHERE skill = " + str(skill) + " AND experience >= " + str(exp - 1) + " AND education >= " + str(edu - 1) + " ORDER BY experience, education;"
            result = conn.execute(query)
            for i in range(result.rowcount):
                row = result.fetchone()
                proj = Project.get_by_id(conn, row['pID'])
                is_exist = False
                for project in project_list:
                    if project['id'] == proj['id'] and skill == proj['roles.skill']:
                        is_exist = True
                if not is_exist:
                    project_list.append(proj)
                    relaxing_matching_count += 1
        if len(project_list) == 0: return None
        return {'projects': project_list, 'strict matching count': strict_matching_count, 'relaxing matching count': relaxing_matching_count}

    def info(self):
        return {'role': 'Collaborator', 'name': self.name, 'email': self.email, 'id': self.id, 'creation_time': self.create_time, 'last_update': self.last_update, 'phone_no': self.phone_no, 'user_level': self.level_text, 'description': self.description, 'education': self.education_text, 'skills': self.skill_dict}

    def commit_skills(self, conn):
        query = "DELETE FROM skills where `collaboratorID` = " + str(self.id) + ";"
        conn.execute(query)
        for k, v in self.skill_dict.items():
            query = "INSERT INTO skills (skill, experience, collaboratorID) VALUES (" + str(k) + ", " + str(v) + ", " + str(self.id) + ");"
            conn.execute(query)

    def commit(self, conn):
        query = "INSERT INTO collaborator (name, email, password, phone_no, education, user_level, description) VALUES (\'" + self.name + "\', \'" + self.email + "\', \'" + self.password_encrypted + "\', \'" + self.phone_no + "\', " + str(self.education) + ", " + str(self.user_level) + ", \'" + self.description + "\') ON DUPLICATE KEY UPDATE `name`= \'" + self.name + "\', `password` = \'" + self.password_encrypted + "\', `phone_no` = \'" + self.phone_no + "\', `education` = " + str(self.education) + ", `user_level` = " + str(self.user_level) + ", `description` = \'" + self.description + "\';"
        conn.execute(query)
        # register check - ID error
        if self.id == '':
            query = "select ID from collaborator where `email` = \'" + self.email + "\';"
            result = conn.execute(query)
            row = result.fetchone()
            self.id = row['ID']
        # register skills
        self.commit_skills(conn)
