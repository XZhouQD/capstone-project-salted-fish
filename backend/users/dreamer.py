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

    @staticmethod
    def collaborators_recommdation(self, conn):
        owner = self.id
        #fetch all project owned by dreamer;
        query_1 = "SELECT ID as proj_ID, project_title, description, category, dreamerID, project_status, is_hidden, hidden_reason, is_modified_after_hidden FROM project WHERE dreamerID = " + str(owner) + " and project_status = 1 ORDER BY ID;"
        result_1 = conn.execute(query_1)
        if result_1.rowcount == 0:
            return None
        project_role_recomm_collabors_list = []
        for i in range(result_1.rowcount):
            row_1 = result_1.fetchone()
            #fetch roles for each project;
            query_2 = "SELECT ID as role_ID, title, amount, skill, experience, education, general_enquiry FROM project_role WHERE projectID = " + str(row_1['proj_ID']) + " ORDER BY ID;"
            result_2 = conn.execute(query_2)
            if result_2.rowcount == 0:
                continue
            #macthing collabors based on the requirements of each role;
            else:
                role_recomm_collabors_list = []
                for j in range(result_2.rowcount):
                    row_2 = result_2.fetchone()
                    collaborator_list = [] 
                    strict_matching_count = 0
                    relaxing_matching_count = 0
                    #1.strict matching
                    query_3 = "select collaborator.ID as ID, name, email, phone_no, education, skill, experience, user_level, description from collaborator, skills where collaborator.ID = skills.collaboratorID and skill = " + str(row_2['skill']) + " and experience = " + str(row_2['experience']) + " and education = " + str(row_2['education']) + " ORDER BY ID;"
                    result_3 = conn.execute(query_3)
                    if result_3.rowcount != 0:
                        for k in range(result_3.rowcount):
                            row_3 = result_3.fetchone()
                            collabor = {'CollaboratorID':row_3['ID'],'Name':row_3['name'],'Email':row_3['email'],'Phone_no':row_3['phone_no'],'Skill':row_3['skill'],'Experience':row_3['experience'],'Education':row_3['education'],'User_level':row_3['user_level'],'Description':row_3['description']}
                            collaborator_list.append(collabor)
                            strict_matching_count += 1
                    #2.relaxing matching
                    query_4 = "select collaborator.ID as ID, name, email, phone_no, education, skill, experience, user_level, description from collaborator, skills where collaborator.ID = skills.collaboratorID and skill = " + str(row_2['skill']) + " and experience >= " + str(row_2['experience'] - 1) + " and education >= " + str(row_2['education'] - 1) + " ORDER BY ID;"
                    result_4 = conn.execute(query_4)
                    if result_4.rowcount != 0:
                        for l in range(result_4.rowcount):
                            row_4 = result_4.fetchone()
                            collabor = {'CollaboratorID':row_4['ID'],'Name':row_4['name'],'Email':row_4['email'],'Phone_no':row_4['phone_no'],'Skill':row_4['skill'],'Experience':row_4['experience'],'Education':row_4['education'],'User_level':row_4['user_level'],'Description':row_4['description']}
                            if collabor not in collaborator_list:
                                collaborator_list.append(collabor)
                            relaxing_matching_count += 1
                    #role info + recommendation collabor list
                    role_recomm_collabors = {'Role_ID':row_2['role_ID'], 'Title':row_2['title'], 'Amount':row_2['amount'], 'Skill':row_2['skill'], 'Experience':row_2['experience'], 'Education':row_2['education'], 'General_enquiry':row_2['general_enquiry'],'Strict_matching_count':strict_matching_count, 'Relaxing_matching_count':relaxing_matching_count, 'Collaborator_list':collaborator_list}
                    role_recomm_collabors_list.append(role_recomm_collabors)
            #project info + role info + recommendation collabor list
            project_role_recomm_collabors = {'Project_ID':row_1['proj_ID'], 'Project_title':row_1['project_title'], 'Description':row_1['description'], 'Category':row_1['category'], 'DreamerID':row_1['dreamerID'], 'Project_status':row_1['project_status'], 'Is_hidden':row_1['is_hidden'], 'Hidden_reason':row_1['hidden_reason'], 'Is_modified_after_hidden':row_1['is_modified_after_hidden'], 'Role_recomm_collabors_list':role_recomm_collabors_list}
            project_role_recomm_collabors_list.append(project_role_recomm_collabors)
        if len(project_role_recomm_collabors_list) == 0: return None
        return project_role_recomm_collabors_list

    def collaborators_recommdation_1(self, conn):
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
                    collabor = {'CollaboratorID':row['ID'],'Name':row['name'],'Email':row['email'],'Phone_no':row['phone_no'],'Skill':row['skill'],'Experience':row['experience'],'Education':row['education'],'User_level':row['user_level'],'Description':row['description']}
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
                    collabor = {'CollaboratorID':row['ID'],'Name':row['name'],'Email':row['email'],'Phone_no':row['phone_no'],'Skill':row['skill'],'Experience':row['experience'],'Education':row['education'],'User_level':row['user_level'],'Description':row['description']}
                    proj_role_info = Project.get_by_id_skill(conn, roles_needed[role_i][0], roles_needed[role_i][1])
                    proj_role_collaborator_list.append((proj_role_info, collabor))
                    relaxing_matching_count += 1
        if len(proj_role_collaborator_list) == 0: return None
        return {'project_role_collaborator': proj_role_collaborator_list, 'strict matching count': strict_matching_count, 'relaxing matching count': relaxing_matching_count}

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
