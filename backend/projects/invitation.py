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
    def get_by_id(conn, project_id,role_id):
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

    def info(self):
        return {'id': self.id, 'project_id': self.project_id, 'role_invite': self.role_invite, 'invitor': self.invitor, 'invitee': self.invitee,  'general_text': self.general_text, 'status': self.status}

    def duplicate_check(self, conn):
        query = "SELECT * FROM invitation where projectID = " + str(self.project_id) + " AND role_applied = " + str(self.role_apply) + " AND invitee = " + str(self.invitee)  + ";"
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