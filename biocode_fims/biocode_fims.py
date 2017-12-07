import requests
import pandas as pd

API_BASE = 'http://biscicol.org/biocode-fims/rest/v1.1/'


def list_projects(format='titles'):
    """Lists all of the *public* projects on the Biocode FIMS"""

    params = {'includePublic': 'true'}
    project_list_url = API_BASE + 'projects/'
    r = requests.get(project_list_url, params=params)
    all_projects = r.json()
    if format == 'raw':
        return all_projects
    elif format == 'titles':
        project_dict = {project['projectTitle']: project['projectId'] \
                        for project in all_projects}
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
        code_list = sorted([ds['expeditionCode'] for ds in datasets])
        return code_list


def dataset_contents(project_id, code_list, format='filtered_dicts'):
    """Returns the full dataset contents for a list of datasets."""

    dataset_code_string = ','.join(code_list)
    dataset_url = '{}projects/query/json'.format(API_BASE)
    dataset_payload = {'projectId': project_id,
                       'expeditions': dataset_code_string,
                       'limit': '100000'}
    dataset_r = requests.get(dataset_url, params=dataset_payload)
    dataset_json = dataset_r.json()
    if format == 'raw':
        return dataset_json['content']
    elif format == 'filtered_dicts':
        filtered_contents = [{k: v for k, v in record.items() if v} \
                                for record in dataset_json['content']]
        return filtered_contents
    elif format == 'dataframe':
        filtered_contents = [{k: v for k, v in record.items() if v} \
                                for record in dataset_json['content']]
        df = pd.DataFrame(filtered_contents)
        df = df.dropna(axis=1, how='all')
        well_order = []
        for number in range(1, 13):
            well_column = str(number).zfill(2)
            for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                well = letter + well_column
                well_order.append(well)
        df['extractionWell'] = df['extractionWell'].astype('category')
        df['extractionWell'] = df['extractionWell'].cat.set_categories(well_order, 
                                                                       ordered=True)
        df = df.sort_values(['extractionPlateID', 'extractionWell'])
        return df


if __name__ == "__main__":
    print(list_projects())
    sibn_datasets = list_datasets(12)
    print(sibn_datasets[:20])
    print(len(dataset_contents(12, sibn_datasets[:5])))
