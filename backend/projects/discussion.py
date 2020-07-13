#!/usr/bin/python3
from users.collaborator import Collaborator
from users.dreamer import Dreamer
from projects.project import Project
from projects.role import Role

class Discussion():
    def __init__(self, projectID, parent_discussion_ID, is_dreamer, d_author = '',c_author = '',text = ''):
        self.projectID = projectID
        self.parent_discussion_ID = parent_discussion_ID
        self.is_dreamer = is_dreamer
        self.d_author = d_author
        self.c_author = c_author
        self.text = text
        # no input warning
        self.id = -1

    @staticmethod
    def get_by_did(conn, discussion_id):
        query = "SELECT * FROM discussion where ID = " + str(discussion_id) + ";"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        discussion_info = {'discussion_id':discussion_id,'parent_id':row['parent_discussion_ID'],'content':row['text']}
        if row['is_dreamer'] == 2:
            author = Dreamer.get_by_id(conn,row['d_author'])
            discussion_info['is_owner'] = 'Yes'
            discussion_info['author_id'] = author['id']
            discussion_info['author_name'] = author['name']
            discussion_info['author_role'] = 'dreamer'
        elif row['is_dreamer'] == 1:
            author = Dreamer.get_by_id(conn, row['d_author'])
            discussion_info['is_owner'] = 'No'
            discussion_info['author_id'] = author['id']
            discussion_info['author_name'] = author['name']
            discussion_info['author_role'] = 'dreamer'
        else:
            author = Collaborator.get_by_id(conn, row['c_author'])
            discussion_info['is_owner'] = 'No'
            discussion_info['author_id'] = author['id']
            discussion_info['author_name'] = author['name']
            discussion_info['author_role'] = 'collaborator'
        return discussion_info

    @staticmethod
    def get_by_pid(conn, project_id):
        query = "SELECT * FROM discussion where projectID = " + str(project_id) + ";"
        result = conn.execute(query)
        all_discussion = {}
        discussion_list = []
        if result.rowcount == 0:
            return None
        for i in range(result.rowcount):
            row = result.fetchone()
            discussion_info = {'discussion_id':row['ID'],'parent_id': row['parent_discussion_ID'], 'content': row['text']}
            if row['is_dreamer'] == 2:
                author = Dreamer.get_by_id(conn, row['d_author'])
                discussion_info['is_owner'] = 'Yes'
                discussion_info['author_id'] = author['id']
                discussion_info['author_name'] = author['name']
                discussion_info['author_role'] = 'dreamer'
            elif row['is_dreamer'] == 1:
                author = Dreamer.get_by_id(conn, row['d_author'])
                discussion_info['is_owner'] = 'No'
                discussion_info['author_id'] = author['id']
                discussion_info['author_name'] = author['name']
                discussion_info['author_role'] = 'dreamer'
            else:
                author = Collaborator.get_by_id(conn, row['c_author'])
                discussion_info['is_owner'] = 'No'
                discussion_info['author_id'] = author['id']
                discussion_info['author_name'] = author['name']
                discussion_info['author_role'] = 'collaborator'
            discussion_list.append(discussion_info)
        all_discussion['discussion_info'] = discussion_list
        return all_discussion


    def info(self):
        return {'id': self.id, 'project_id': self.projectID, 'parent_discussion_id': self.parent_discussion_ID,'content': self.text, 'is_dreamer': self.is_dreamer}

    def owner_reply(self, conn):
        query = "SELECT * FROM discussion where ID = " + str(self.parent_discussion_ID) + " ;"
        result = conn.execute(query)
        row = result.fetchone()
        if row['is_dreamer'] == 2 or row['is_dreamer'] == 1:
            query = "INSERT INTO dreamer_notification (dreamer_ID, notification_text, is_viewed) VALUES (" + str(row['d_author']) + ", \'" + self.text + "\', " + str(0) + ");"
            conn.execute(query)
        else:
            query = "INSERT INTO collaborator_notification (collaborator_ID, notification_text, is_viewed) VALUES (" + str(row['c_author']) + ", \'" + self.text + "\', " + str(0) + ");"
            conn.execute(query)


    def create_by_dreamer(self, conn):
        if self.parent_discussion_ID == 0:
            query = "INSERT INTO discussion (projectID, text, is_dreamer, d_author) VALUES (" + str(self.projectID) + ", \'" + self.text + "\', " + str(self.is_dreamer) + ", " + str(self.d_author) + ");"
        else:
            query = "INSERT INTO discussion (projectID, parent_discussion_ID, text, is_dreamer, d_author) VALUES (" + str(self.projectID) + ", " + str(self.parent_discussion_ID) + ", \'" + self.text + "\', " + str(self.is_dreamer) + ", " + str(self.d_author) + ");"
            if self.is_dreamer == 2:
                self.owner_reply(conn)
        conn.execute(query)
        query = "SELECT * FROM discussion where projectID = " + str(self.projectID) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']
        return self

    def create_by_collaborator(self, conn):
        if self.parent_discussion_ID == 0:
            query = "INSERT INTO discussion (projectID, text, is_dreamer, c_author) VALUES (" + str(self.projectID) + ", \'" + self.text + "\', " + str(self.is_dreamer) + ", " + str(self.c_author) + ");"
        else:
            query = "INSERT INTO discussion (projectID, parent_discussion_ID, text, is_dreamer, c_author) VALUES (" + str(self.projectID) + ", " + str(self.parent_discussion_ID) + ", \'" + self.text + "\', " + str(self.is_dreamer) + ", " + str(self.c_author) + ");"
        conn.execute(query)
        query = "SELECT * FROM discussion where projectID = " + str(self.projectID) + " ORDER BY create_time DESC;"
        result = conn.execute(query)
        row = result.fetchone()
        self.id = row['ID']

        return self