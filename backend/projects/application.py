#!/usr/bin/python3
from users.collaborator import Collaborator

class Application():
    def __init__(self, project_id, role_apply, applicant,general_text = '',status = -1):
        self.project_id = project_id
        self.role_apply = role_apply
        self.applicant = applicant
        self.general_text = general_text
        self.status = -1
        # no input warning
        self.id = -1
    
    
    def get_by_id(conn, project_id,role_id):
        query = "SELECT * FROM application where projectID = " + str(project_id) + " AND role_applied = " + str(role_id) + ";"
        result = conn.execute(query)
        application_list = []
        if result.rowcount == 0:
            return None
        for i in range(result.rowcount):
            row = result.fetchone()
            application= Collaborator.get_by_id(conn,row['applicant'])
            application_list.append(application)
        if len(application_list) == 0: return None
        return {'application': application_list, 'amount': result.rowcount}


    def info(self):
        return {'id': self.id, 'project_id': self.project_id, 'role_apply': self.role_apply, 'applicant': self.applicant, 'general_text': self.general_text}

    def duplicate_check(self, conn):
        query = "SELECT * FROM application where projectID = " + str(self.project_id) + " AND role_applied = " + str(self.role_apply) + " AND applicant = " + str(self.applicant)  + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False
    
    def check_project_role(self,conn):
        query = "SELECT * FROM project_role where projectID = " + str(self.project_id) + " AND ID = " + str(self.role_apply) + " ;"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def create(self, conn):
        if not self.check_project_role(conn):
            return None
        if self.duplicate_check(conn):
            return None
        query = "INSERT INTO application (projectID, role_applied, applicant, general_text) VALUES (" + str(self.project_id) + ", " + str(self.role_apply) + ", " + str(self.applicant) + ", \'" + self.general_text + "\');"
        conn.execute(query)
        query = "SELECT * FROM application where projectID = " + str(self.project_id) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        return self
