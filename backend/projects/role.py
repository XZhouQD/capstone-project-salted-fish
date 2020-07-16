#!/usr/bin/python3
import yaml
from projects.project import Project

class Role():
    education_list = ['Null', 'Other', 'Bachelor', 'Master', 'PhD']
    skills_list = ['Null'] + yaml.load(open('projects/project.config', 'r', encoding='utf-8').read(), Loader=yaml.FullLoader)['Role']['Skills']

    def __init__(self, project_id, title, amount, skill, experience, education, general_enquiry=''):
        self.project_id = project_id
        self.title = title
        self.amount = amount
        self.skill = skill
        self.experience = experience
        self.education = education
        self.general_enquiry = general_enquiry
        # no input warning
        self.id = -1

    @staticmethod
    def get_object_by_id(conn, role_id):
        query = "SELECT * FROM project_role where ID = " + str(role_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
        role.id = row['ID']
        return role

    @staticmethod
    def get_by_id(conn, role_id):
        query = "SELECT * FROM project_role where ID = " + str(role_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
        role.id = row['ID']
        return role.info()

    @staticmethod
    def get_text_by_id(conn, role_id):
        query = "SELECT * FROM project_role where ID = " + str(role_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
        role.id = row['ID']
        return role.text_info()

    @staticmethod
    # get by one type role of project (project id + skill)
    def get_by_id_skill(conn, proj_id, skill):
        query = "SELECT * FROM project_role where projectID = " + str(proj_id) + " and skill = " + str(skill) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
        role.id = row['ID']
        return role.info()

    @staticmethod
    def get_by_proj_id(conn, proj_id):
        query = "SELECT * FROM project_role where projectID = " + str(proj_id) + ";"
        result = conn.execute(query)
        roles = []
        if result.rowcount == 0:
            return roles
        for i in range(result.rowcount):
            row = result.fetchone()
            role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
            role.id = row['ID']
            roles.append(role.info())
        return roles

    @staticmethod
    def get_text_by_proj_id(conn, proj_id):
        query = "SELECT * FROM project_role where projectID = " + str(proj_id) + ";"
        result = conn.execute(query)
        roles = []
        if result.rowcount == 0:
            return roles
        for i in range(result.rowcount):
            row = result.fetchone()
            role = Role(row['projectID'], row['title'], row['amount'], row['skill'], row['experience'], row['education'], general_enquiry=row['general_enquiry'])
            role.id = row['ID']
            roles.append(role.info())
        return role.text_info()

    def info(self):
        return {'id': self.id, 'title': self.title, 'amount': self.amount, 'skill': self.skill, 'experience': self.experience, 'education': self.education, 'general_enquiry': self.general_enquiry, 'project_id': self.project_id}

    def text_info(self):
        print(self.skill, self.education)
        return {'id': self.id, 'title': self.title, 'amount': self.amount, 'skill': self.skills_list[self.skill], 'experience': self.experience, 'education': self.education_list[self.education], 'general_enquiry': self.general_enquiry, 'project_id': self.project_id}

    def duplicate_check(self, conn):
        query = "SELECT * FROM project_role where projectID = " + str(self.project_id) + " AND title = \'" + self.title + "\' AND skill = " + str(self.skill) + " AND experience = " + str(self.experience) + " AND education = " + str(self.education) + ";"
        result = conn.execute(query)
        if result.rowcount > 0:
            return True
        return False

    def create(self, conn):
        if self.duplicate_check(conn):
            return None
        query = "INSERT INTO project_role (projectID, title, amount, skill, experience, education, general_enquiry) VALUES (" + str(self.project_id) + ", \'" + self.title + "\', " + str(self.amount) + ", " + str(self.skill) + ", " + str(self.experience) + ", " + str(self.education) + ", \'" + self.general_enquiry + "\');"
        conn.execute(query)
        query = "SELECT * FROM project_role where projectID = " + str(self.project_id) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        return self

    def patch(self, conn):
        #Check project status, no more updates allowed if project is finished;
        proj = Project.get_by_id(conn, self.project_id)
        if proj['status'] != 1:
            return 99 
        query = "UPDATE project_role SET title = \'" + self.title + "\', amount = " + str(self.amount) + ", skill = " + str(self.skill) + ", experience = " + str(self.experience) + ", education = " + str(self.education) + ", general_enquiry = \'" + self.general_enquiry + "\' WHERE ID = " + str(self.id) + ";"
        print(query)
        conn.execute(query)
        return self
