#!/usr/bin/python3

from flask_restplus import reqparse
from projects.project import Project
from projects.role import Role
from users.collaborator import Collaborator

# ================== Parsers ====================
search_condition_parser = reqparse.RequestParser()
search_condition_parser.add_argument('description', type=str)
search_condition_parser.add_argument('category', type=str)
search_condition_parser.add_argument('order_by', choices=['last_update', 'project_title'],default='last_update')
search_condition_parser.add_argument('sorting', choices=['ascending', 'descending'], default='descending')
search_condition_parser.add_argument('page', type=int, default=1)

prediction_parser = reqparse.RequestParser()
# ================== Parsers ====================

args = search_condition_parser.parse_args()
description = args.get('description')
category = args.get('category')

def getProjectsBySkill(conn, collaborator_id):
    edu = Collaborator.info.education
    skills = Collaborator.getSkills(conn, collaborator_id)
    project_dict = {}
    proj_count = 0
    for sk in skills:
        # get related projectID based on education, skill and experience;
        query  = "select project_ID from project_role where educartion = \'" + edu + "\'  and skill = \'" + sk + "\' and experience = \'" + skills[sk] + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            continue
        # get detail of each project_ID
        for i in range(result.result.rowcount):
            proj.id = result.fetchone()
            proj = Project.get_by_id(conn, proj.id)
            if proj == None:
                continue
            proj_count += 1
            project_list = []
            row = result.fetchone()
            proj = Project(row['ID'],row['project_title'],row['description'],row['category'],row['dreamerID'],row['project_status'],row['is_hidden'],row['hidden_reason'],row['is_modified_after_hidden'],row['create_time'],row['last_update'])
            project_list.append(proj.info())
            project_dict[proj_count] = project_list
    return project_dict


def getProjectsByKeyword(conn, description, category):
    description  = "%" + description + "%"
    category = "%" + category + "%"
    if description != '' and category != '':
        query = "select * from project where description like \'" + description + "\' and category like \'" + category + "\' and project_status = 1 order by last_update descending;"
    elif description != '' and category == '':
        query = "select * from project where description like \'" + description + "\' and project_status = 1 order by last_update descending;"
    elif description == '' and category != '':
        query = "select * from project where category like \'" + category + "\' and project_status = 1 order by last_update descending;"
    else:
        query = "select * from project where project_status = 1 order by last_update descending;"

    result = conn.execute(query)
    if result.rowcount == 0:
        return None
    project_dict = {}
    for i in range(result.rowcount):
        project_list = []
        row = result.fetchone()
        proj = Project(row['ID'],row['project_title'],row['description'],row['category'],row['dreamerID'],row['project_status'],row['is_hidden'],row['hidden_reason'],row['is_modified_after_hidden'],row['create_time'],row['last_update'])
        project_list.append(proj.info())
        project_dict[i] = project_list
    return project_dict


