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
                    collabor = {'collaboratorID':row['ID'],'Name':row['name'],'Email':row['email'],'Phone_no':row['phone_no'],'skill':row['skill'],'experience':row['experience'],'education':row['education'],'user_level':row['user_level'],'description':row['description']}
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
                    collabor = {'collaboratorID':row['ID'],'Name':row['name'],'Email':row['email'],'Phone_no':row['phone_no'],'skill':row['skill'],'experience':row['experience'],'education':row['education'],'user_level':row['user_level'],'description':row['description']}
                    proj_role_info = Project.get_by_id_skill(conn, roles_needed[role_i][0], roles_needed[role_i][1])
                    proj_role_collaborator_list.append((proj_role_info, collabor))
                    relaxing_matching_count += 1
        if len(proj_role_collaborator_list) == 0: return None
        return {'project-role-collaborator': proj_role_collaborator_list, 'strict matching count': strict_matching_count, 'relaxing matching count': relaxing_matching_count}

    @staticmethod
    def update_user_level(conn, user_type, count, user_level, user_ID):
        if user_type == 'D':
            table_to_update = 'dreamer'
        if user_type == 'C':
            table_to_update = 'collaborator'
        if count >= 1 and count <= 3 and user_level != 1:
            query = "UPDATE " + str(table_to_update) + " set user_level = 1 where ID = " + str(user_ID) + ";"
            conn.execute(query)
        if count > 3 and count <= 5 and user_level != 2:
            query = "UPDATE " + str(table_to_update) + " set user_level = 2 where ID = " + str(user_ID) + ";"
            conn.execute(query)
        if count > 5 and count <= 8 and user_level != 3:
            query = "UPDATE " + str(table_to_update) + " set user_level = 3 where ID = " + str(user_ID) + ";"
            conn.execute(query)
        if count > 8 and count <= 15 and user_level != 4:
            query = "UPDATE " + str(table_to_update) + " set user_level = 4 where ID = " + str(user_ID) + ";"
            conn.execute(query)
        if count > 15 and user_level != 5:
            query = "UPDATE " + str(table_to_update) + " set user_level = 5 where ID = " + str(user_ID) + ";"
            conn.execute(query)

    @staticmethod
    def total_project_finished_by_collabor(conn, collabor_ID):
        query_1 = "select count(*) as count_1 from application where status = 9 and applicant = " + str(collabor_ID) + ";"
        result_1 = conn.execute(query_1)
        row_1 = result_1.fetchone()
        query_2 = "select count(*) as count_2 from invitation where status = 9 and invitee = " + str(collabor_ID) + ";"
        result_2 = conn.execute(query_2)
        row_2 = result_2.fetchone()
        return row_1['count_1'] + row_2['count_2']

    @staticmethod
    def finish_a_project(conn, proj_ID, dreamer_ID):
        # update project_status = 9 as finished
        query = "UPDATE project set project_status = 9 where dreamerID = " + str(dreamer_ID) + " ID = " + str(proj_ID) + ";"
        conn.execute(query)
        #update applicant status as finish coorporation for application table
        query = "UPDATE application set status = 9 where ID = " + str(proj_ID) + ";"
        conn.execute(query)
        #update invitation status as finish coorporation for invitation table
        query = "UPDATE invitation set status = 9 where ID = " + str(proj_ID) + ";"
        conn.execute(query)

        #further update user_level for dreamer based on the statistic count;
        query_1 = "select count(*) as count from project where dreamerID = " + str(dreamer_ID) + " and project_status = 9;"
        result_1 = conn.execute(query_1)
        count_dreamer_finished_proj = result_1.fetchone()
        query_2 = "select user_level from dreamer where ID= " + str(dreamer_ID) + ";"
        result_2 = conn.execute(query_2)
        dreamer_level = result_2.fetchone()
        update_user_level(conn, 'D', count_dreamer_finished_proj, dreamer_level, dreamer_ID)

        #further update user_level for all collaborators of this project based on the statistic count;
        query_3 = "select applicant from application where projectID = "+ str(proj_ID) + ";"
        result_3 = conn.execute(query_3)
        for i in range(result_3.rowcount):
            row_3 = result_3.fetchone()
            count_collabor_finished_proj = total_project_finished_by_collabor(conn, row_3['applicant'])
            query_4 = "select user_level from collaborator where ID= " + str(row_3['applicant']) + ";"
            result_4 = conn.execute(query_4)
            collabor_level = result_4.fetchone()
            update_user_level(conn, 'C', count_collabor_finished_proj, collabor_level, row_3['applicant'])
            
                    
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
