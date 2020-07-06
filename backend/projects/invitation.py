#!/usr/bin/python3
from users.collaborator import Collaborator
from users.dreamer import Dreamer

class Invitation():
    def __init__(self, project_id, role_invite, invitor, invitee, general_text = '', status = -1):
        self.project_id = project_id
        self.role_invite = role_invite
        self.invitor = invitor
        self.invitee = invitee
        self.general_text = general_text
        self.status = -1
        # no input warning
        self.id = -1

    @staticmethod
    def get_by_iid(conn, invitation_id):
        query = "SELECT * FROM invitation where ID = " + str(invitation_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        invitation = Collaborator.get_by_id(conn,row['invitee'])
        if len(invitation) == 0: return None
        invitation['general_text'] = row['general_text']
        invitation['apply_status'] = row['status']
        return invitation

    @staticmethod
    def get_by_pid_rid(conn, project_id,role_id):
        query = "SELECT * FROM invitation where projectID = " + str(project_id) + " AND role_applied = " + str(role_id) + ";"
        result = conn.execute(query)
        invitees = []
        if result.rowcount == 0:
            return None
        for i in range(result.rowcount):
            row = result.fetchone()
            invitee = Collaborator.get_by_id(conn,row['invitee'])
            invitees.append(invitee)
        if len(invitees) == 0: return None
        return {'invitees': invitees, 'amount': result.rowcount}

    @staticmethod
    def get_by_invitee(conn, invitee_id):
        query = "SELECT * FROM invitation where invitee = " + str(invitee_id) + " AND status = -1;"
        result = conn.execute(query)
        invitations = []
        for i in range(result.rowcount):
            row = result.fetchone()
            invitation = Invitation(row['projectID'], row['role_invited'], row['invitor'], row['invitee'], row['general_text'], row['status'])
            invitation.id = row['ID']
            invitations.append(invitation)
        return {'invitations': invitations, 'amount': result.rowcount}

    @staticmethod
    #
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
    def accept_an_invitation(conn, invitation_id):
        #get the application;
        curr_invitation = Invitation.get_by_iid(conn, invitation_id)
        proj_ID = curr_invitation['project_id']
        role_ID = curr_invitation['role_invite']
        # update the invitation status as 1 -  accepte the invitaiton;
        query_1 = "UPDATE invitation set status = 1 where ID = " + str(invitation_id) + ";"
        conn.execute(query_1)       
        #check if all members have been recruited for the same project role;
        is_member_full = Invitation.is_all_members_recruited(conn, proj_ID, role_ID)
        #decline all other applications/invitation for the same project role if all members have been recruited; 
        if is_member_full:
            query_2 = "UPDATE application set status = 0 where projectID = " + str(proj_ID) + " and role_applied " + str(role_ID) + ";"
            conn.execute(query_2)
            query_3 = "UPDATE invitation set status = 0 where projectID = " + str(proj_ID) + " and role_applied " + str(role_ID) + ";"
            conn.execute(query_3)
        #return the accepted invitation;
        return Invitation.get_by_iid(conn, invitation_id)

    @staticmethod
    def decline_an_invitation(conn, invitation_id):
        # update the invitation status as 0 -  decline the invitaiton;
        query_1 = "UPDATE invitation set status = 0 where ID = " + str(invitation_id) + ";"
        conn.execute(query_1)       
        #return the accepted invitation;
        return Invitation.get_by_iid(conn, invitation_id)
        
    def info(self):
        return {'id': self.id, 'project_id': self.project_id, 'role_invite': self.role_invite, 'invitor': self.invitor, 'invitee': self.invitee,  'general_text': self.general_text, 'status': self.status}

    def duplicate_check(self, conn):
        query = "SELECT * FROM invitation where projectID = " + str(self.project_id) + " AND role_applied = " + str(self.role_invite) + " AND invitee = " + str(self.invitee)  + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def check_project_role(self,conn):
        query = "SELECT * FROM project_role where projectID = " + str(self.project_id) + " AND ID = " + str(self.role_invite) + " ;"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def create(self, conn):
        if not self.check_project_role(conn):
            return None
        if self.duplicate_check(conn):
            return None
        query = "INSERT INTO invitation (projectID, role_invited, invitor, invitee, general_text) VALUES (" + str(self.project_id) + ", " + str(self.role_invite) + ", " + str(self.invitor) + ", " + str(self.invitee) +  ", \'" + self.general_text + "\');"
        conn.execute(query)
        query = "SELECT * FROM invitation where projectID = " + str(self.project_id) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        return self
