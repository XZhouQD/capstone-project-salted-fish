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
            project_list.append(proj.info())
        return project_list

    @staticmethod
    def check_owner(conn, proj_id, owner_id):
        query = "SELECT * FROM project WHERE ID = " + str(proj_id) + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            row = result.fetchone()
            if row['dreamerID'] == owner_id: return True
        return False

    def info(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'owner': self.owner, 'category': self.category, 'status': self.project_status, 'is_hidden': self.is_hidden, 'hidden_reason': self.hidden_reason, 'is_modified_after_hidden': self.is_modified_after_hidden, "roles": self.roles}

    def duplicate_check(self, conn):
        query = "SELECT * FROM project WHERE project_title = \'" + self.title + "\' AND dreamerID = " + str(self.owner) + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def create(self, conn):
        if self.duplicate_check(conn):
            return None
        query = "INSERT INTO project (project_title, description, category, dreamerID) VALUES (\'" + self.title + "\', \'" + self.description + "\', " + str(self.category) + ", " + str(self.owner) + ");"
        conn.execute(query)
        query = "SELECT * FROM project WHERE dreamerID = " + str(self.owner) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        return self

