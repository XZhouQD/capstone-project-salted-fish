#!/usr/bin/python3
from projects.role import Role

class Project():
    def __init__(self, title, description, owner, category, status=-1, hidden=0, hidden_reason=''):
        self.title = title
        self.description = description
        self.owner = owner
        self.category = category
        self.project_status = status
        self.is_hidden = hidden
        self.hidden_reason = hidden_reason
        # no input warning
        self.id = -1
        self.is_modified_after_hidden = 0
        self.roles = [] # role info instead of Role object in json format

    @staticmethod
    #general search for all visitors without registering or logining in;
    def search_list(conn, description, category, order_by, order):
        if description != '' and category != -1:
            query = "SELECT * FROM project WHERE description LIKE \'%%" + description + "%%\' AND category = " + str(category) + " AND project_status > 0 ORDER BY " + order_by + " " + order + ";"
        elif description != '':
            query = "SELECT * FROM project WHERE description LIKE \'%%" + description + "%%\' AND project_status > 0 ORDER BY " + order_by + " " + order + ";"
        elif category != -1:
            query = "SELECT * FROM project WHERE category = " + str(category) + " AND project_status > 0 ORDER BY " + order_by + " " + order + ";"
        else:
            query = "SELECT * FROM project WHERE project_status > 0 ORDER BY " + order_by + " " + order + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        project_list = []
        for i in range(result.rowcount):
            row = result.fetchone()
            proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
            proj.id = row['ID']
            proj.is_modified_after_hidden = row['is_modified_after_hidden']
            proj.roles = Role.get_by_proj_id(conn, proj.id)
            proj.create_time = row['create_time']
            proj.last_update = row['last_update']
            project_list.append(proj.info())
        return {'projects': project_list, 'amount': result.rowcount}

    @staticmethod
    def get_by_id(conn, proj_id):
        query = "SELECT * FROM project WHERE ID = " + str(proj_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
        proj.id = row['ID']
        proj.is_modified_after_hidden = row['is_modified_after_hidden']
        proj.roles = Role.get_by_proj_id(conn, proj_id)
        proj.create_time = row['create_time']
        proj.last_update = row['last_update']
        return proj.info()

    @staticmethod
    #return a Project object with project generail info without roles;
    def get_by_proj_id(conn, proj_id):
        query = "SELECT * FROM project WHERE ID = " + str(proj_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
        proj.id = row['ID']
        proj.is_modified_after_hidden = row['is_modified_after_hidden']
        return proj

    @staticmethod
    #search by project id and role skill for one type of role 
    def get_by_id_skill(conn, proj_id, skill):
        query = "SELECT * FROM project WHERE ID = " + str(proj_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
        proj.id = row['ID']
        proj.is_modified_after_hidden = row['is_modified_after_hidden']
        proj.roles = Role.get_by_id_skill(conn, proj.id, skill)
        proj.create_time = row['create_time']
        proj.last_update = row['last_update']
        return proj.info()

    @staticmethod
    def get_by_title(conn, project_title):
        query = "SELECT * FROM project WHERE project_title = " + project_title + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
        proj.id = row['ID']
        proj.is_modified_after_hidden = row['is_modified_after_hidden']
        proj.roles = Role.get_by_proj_id(conn, proj.id)
        proj.create_time = row['create_time']
        proj.last_update = row['last_update']
        return proj.info()

    @staticmethod
    def get_by_owner(conn, owner_id):
        query = "SELECT * FROM project WHERE dreamerID = " + str(owner_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        project_list = []
        for i in range(result.rowcount):
            row = result.fetchone()
            proj = Project(row['project_title'],row['description'],row['dreamerID'],row['category'],status=row['project_status'],hidden=row['is_hidden'],hidden_reason=row['hidden_reason'])
            proj.id = row['ID']
            proj.is_modified_after_hidden = row['is_modified_after_hidden']
            proj.roles = Role.get_by_proj_id(conn, proj.id)
            proj.create_time = row['create_time']
            proj.last_update = row['last_update']
            project_list.append(proj.info())
        return project_list
    
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
        query_1 = "UPDATE project set project_status = 9 where dreamerID = " + str(dreamer_ID) + " and ID = " + str(proj_ID) + ";"
        conn.execute(query_1)
        #update applicant status as finish coorporation for application table
        query_2 = "UPDATE application set status = 9 where projectID = " + str(proj_ID) + ";"
        conn.execute(query_2)
        #update invitation status as finish coorporation for invitation table
        query_3 = "UPDATE invitation set status = 9 where projectID = " + str(proj_ID) + ";"
        conn.execute(query_3)

        #further update user_level for dreamer based on the statistic count;
        query_1 = "select count(*) as count from project where dreamerID = " + str(dreamer_ID) + " and project_status = 9;"
        result_1 = conn.execute(query_1)
        row_1 = result_1.fetchone()
        query_2 = "select user_level from dreamer where ID= " + str(dreamer_ID) + ";"
        result_2 = conn.execute(query_2)
        row_2 = result_2.fetchone()
        Project.update_user_level(conn, 'D', row_1['count'], row_2['user_level'], dreamer_ID)

        #further update user_level for all collaborators of this project based on the statistic count;
        query_3 = "select applicant from application where projectID = "+ str(proj_ID) + ";"
        result_3 = conn.execute(query_3)
        for i in range(result_3.rowcount):
            row_3 = result_3.fetchone()
            count_collabor_finished_proj = Project.total_project_finished_by_collabor(conn, row_3['applicant'])
            query_4 = "select user_level from collaborator where ID= " + str(row_3['applicant']) + ";"
            result_4 = conn.execute(query_4)
            row_4 = result_4.fetchone()
            Project.update_user_level(conn, 'C', count_collabor_finished_proj, row_4['user_level'], row_3['applicant'])

        #finally return the updated project info;
        return Project.get_by_id(conn, proj_ID)
            
    @staticmethod
    def follow_a_project(conn, proj_ID, user_role, user_ID):
        if user_role == 'Dreamer':
            #check if the user has subscribed the project or not;
            query_1 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and d_subscriber = " + str(user_ID) + ";"
            result = conn.execute(query_1)
            if result.rowcount == 0:
                #user has not subscribed this project, proceed to subscribe it;
                query = "INSERT INTO subscription (projectID, is_dreamer, d_subscriber) VALUES (" + str(proj_ID) + ", " + str(1) + ", " + str(user_ID) + ");"
                conn.execute(query)
                #query one more time to return the subscription info;
                query_2 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and d_subscriber = " + str(user_ID) + ";"
                result = conn.execute(query_2)
            row = result.fetchone()
            userid = row['d_subscriber']  
        else:
            #check if the user has subscribed the project or not;
            query_1 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and c_subscriber = " + str(user_ID) + ";"
            result = conn.execute(query_1)
            if result.rowcount == 0:
                #user has not subscribed this project, proceed to subscribe it;
                query = "INSERT INTO subscription (projectID, is_dreamer, c_subscriber) VALUES (" + str(proj_ID) + ", " + str(0) + ", " + str(user_ID) + ");"
                conn.execute(query)
                #query one more time to return the subscription info;
                query_2 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and c_subscriber = " + str(user_ID) + ";"
                result = conn.execute(query_2)
            row = result.fetchone()
            userid = row['c_subscriber']  
        return {'projectID':row['projectID'], 'user_ID':userid}

    @staticmethod
    def unfollow_a_project(conn, proj_ID, user_role, user_ID):
        if user_role == 'Dreamer':
            query = "DELETE FROM subscription WHERE projectID = " + str(proj_ID) + " and d_subscriber = " + str(user_ID) + ";"
            conn.execute(query)
            #query one more time to return the subscription info;
            query_1 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and d_subscriber = " + str(user_ID) + ";"
            result = conn.execute(query_1)
            if result.rowcount == 0:
                return True
        else:
            query = "DELETE FROM subscription WHERE projectID = " + str(proj_ID) + " and c_subscriber = " + str(user_ID) + ";"
            conn.execute(query)
            #query one more time to return the subscription info;
            query_1 = "SELECT * FROM subscription WHERE projectID = " + str(proj_ID) + " and c_subscriber = " + str(user_ID) + ";"
            result = conn.execute(query_1)
            if result.rowcount == 0:
                return True        
        return False
            
    @staticmethod
    def check_owner(conn, proj_id, owner_id):
        query = "SELECT * FROM project WHERE ID = " + str(proj_id) + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            row = result.fetchone()
            if row['dreamerID'] == owner_id: return True
        return False

    def info(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'owner': self.owner, 'category': self.category, 'status': self.project_status, 'is_hidden': self.is_hidden, 'hidden_reason': self.hidden_reason, 'is_modified_after_hidden': self.is_modified_after_hidden, "roles": self.roles, "create_time": str(self.create_time), "last_update": str(self.last_update)}

    def duplicate_check(self, conn):
        query = "SELECT * FROM project WHERE project_title = \'" + self.title + "\' AND dreamerID = " + str(self.owner) + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def patch(self, conn):
        query = "UPDATE project SET project_title = \'" + self.title + "\', description = \'" + self.description + "\', category = " + str(self.category) + " WHERE id = " + str(self.id) + ";"
        print(query)
        result = conn.execute(query)
        return self

    def create(self, conn):
        if self.duplicate_check(conn):
            return None
        query = "INSERT INTO project (project_title, description, category, dreamerID) VALUES (\'" + self.title + "\', \'" + self.description + "\', " + str(self.category) + ", " + str(self.owner) + ");"
        conn.execute(query)
        query = "SELECT * FROM project WHERE dreamerID = " + str(self.owner) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        self.create_time = row['create_time']
        self.last_update = row['last_update']
        return self

