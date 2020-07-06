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
    
    
    @staticmethod
    def get_by_aid(conn, application_id):
        query = "SELECT * FROM application where ID = " + str(application_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        application= Collaborator.get_by_id(conn,row['applicant'])
        if len(application) == 0: return None
        application['general_text'] = row['general_text']
        application['apply_status'] = row['status']
        return application

    @staticmethod
    def get_by_pid_rid(conn, project_id,role_id):
        query = "SELECT * FROM application where projectID = " + str(project_id) + " AND role_applied = " + str(role_id) + ";"
        result = conn.execute(query)
        all_application = {}
        if result.rowcount == 0:
            return None
        for i in range(result.rowcount):
            row = result.fetchone()
            application= Collaborator.get_by_id(conn,row['applicant'])
            application['general_text'] = row['general_text']
            application['apply_status'] = row['status']
            all_application['appicant'+str(i+1)] = application
        if len(application) == 0: return None
        return all_application

    @staticmethod
    def is_all_members_recruited(conn, proj_ID, role_ID):
        query_1 = "select count(*) as count_1 from application where projectID = " + str(proj_ID) + " and role_applied " + str(role_ID) + " and status = 1;"
        result_1 = conn.execute(query_1)
        row_1 = result_1.fetchone()
        query_2 = "select count(*) as count_2 from invitation where projectID = " + str(proj_ID) + " and role_invited " + str(role_ID) + " and status = 1;"
        result_2 = conn.execute(query_2)
        row_2 = result_2.fetchone()
        query_3 = "select amount from project_role where projectID = " + str(proj_ID) + " and ID " + str(role_ID) + ";"
        result_3 = conn.execute(query_3)
        row_3 = result_3.fetchone()
        if row_1['count_1'] + row_2['count_2'] == row_3['amount']:
            return True
        return False

    @staticmethod
    def approve_an_application(conn, application_id):
        #get the application;
        curr_application = Application.get_by_aid(conn, application_id)
        proj_ID = curr_application['project_id']
        role_ID = curr_application['role_apply']
        # update the application status as 1 - application approved;
        query_1 = "UPDATE application set status = 1 where ID = " + str(application_id) + ";"
        conn.execute(query_1)       
        #check if all members have been recruited for the same project role;
        is_member_full = Application.is_all_members_recruited(conn, proj_ID, role_ID)
        #decline all other applications/invitations for the same project if all members have been recruited; 
        if is_member_full:
            query_2 = "UPDATE application set status = 0 where projectID = " + str(proj_ID) + " and role_applied " + str(role_ID) + ";"
            conn.execute(query_2)
            query_3 = "UPDATE invitation set status = 0 where projectID = " + str(proj_ID) + " and role_applied " + str(role_ID) + ";"
            conn.execute(query_3)
        #return approved application;
        return Application.get_by_aid(conn, application_id)
        
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
