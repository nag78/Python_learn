import requests


# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Анализ информации об репозиториях
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Анализ информации о репозиториях
for repo_dict in repo_dicts:
    print("\nSelected information about each repository:")
    print('Name: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repository: ', repo_dict['html_url'])
    print('Created: ', repo_dict['created_at'])
    print('Update: ', repo_dict['updated_at'])
    print('Description: ', repo_dict['description'])
