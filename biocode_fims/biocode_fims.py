import requests
import json

API_BASE = 'http://biscicol.org/biocode-fims/rest/v1.1/'

def list_projects(format='titles'):
    """Lists all of the *public* projects on the Biocode FIMS"""

    params = {'includePublic':'true'}
    project_list_url = API_BASE + 'projects/'
    r = requests.get(project_list_url, params=params)
    all_projects = r.json()
    if format == 'raw':
        return all_projects
    elif format == 'titles':
        project_dict = {project['projectTitle']: project['projectId'] for project in all_projects}
        return project_dict
    else:
        return 

def list_datasets(project_id, format='code_list'):
    """Lists all of the datasets for a given project"""

    list_url = '{}projects/{}/expeditions'.format(API_BASE, project_id)
    r = requests.get(list_url)
    datasets = r.json()
    if format == 'raw':
        return datasets
    elif format == 'code_list':
        code_list = [ds['expeditionCode'] for ds in datasets]
        return code_list

def dataset_contents(project_id, code_list, format='list_of_dicts'):
    """Returns the full dataset contents for a list of datasets."""

    dataset_code_string = ','.join(code_list)
    dataset_url = '{}projects/query/json'.format(API_BASE)
    dataset_payload = {'projectId': project_id,
                       'expeditions': dataset_code_string,
                       'limit':'100000'}
    dataset_r = requests.get(dataset_url, params=dataset_payload)
    dataset_json = dataset_r.json()
    if format == 'raw':
        return dataset_json
    elif format == 'list_of_dicts':
        return dataset_json['content']

if __name__ == "__main__":
    print(list_projects())
    sibn_datasets = list_datasets(12)
    print(sibn_datasets[:5])
    print(len(dataset_contents (12, sibn_datasets[:5])))