import asana
from Integrations.credentials import asanaToken
from Integrations.credentials import asanaWorkspace
# from credentials import asanaToken
# from credentials import asanaWorkspace
client = asana.Client.access_token(asanaToken)

def getProjects():
    result = client.projects.get_projects({'opt_fields': ['name'], 'workspace':asanaWorkspace}, opt_pretty=True)
    result=list(result)    
    return result

def getTasksByProject(project):    
    result = client.tasks.get_tasks_for_project(project, {'opt_fields': ['name','completed']}, opt_pretty=True)
    result=list(result)
    return result

# print(getTasksByProject('1203537349306106'))
# print(getProjects())